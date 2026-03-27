# LLM.py
import os
import requests
import json
import time
import re
import pdfplumber
import pandas as pd
import concurrent.futures
from threading import Lock
from tqdm import tqdm
from dotenv import load_dotenv
from typing import List, Dict, Tuple, Any, Optional
from difflib import SequenceMatcher
import numpy as np
from abc import ABC, abstractmethod

# 加载环境变量
load_dotenv()

# 模型配置
MODEL_CONFIGS = {
    "deepseek-chat": {
        "api_url": "https://api.deepseek.com/v1/chat/completions",
        "env_key": "DEEPSEEK_API_KEY",
        "headers": lambda key: {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        }
    },
    "gpt-4": {
        "api_url": "https://api.gptsapi.net/v1/chat/completions",
        "env_key": "OPENAI_API_KEY",
        "headers": lambda key: {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        }
    },
    "gpt-4o": {
        "api_url": "https://api.gptsapi.net/v1/chat/completions",
        "env_key": "OPENAI_API_KEY",
        "headers": lambda key: {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        }
    },
    "claude-3-sonnet": {
        "api_url": "https://api.anthropic.com/v1/messages",
        "env_key": "ANTHROPIC_API_KEY",
        "headers": lambda key: {
            "x-api-key": key,
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01"
        }
    },
    "qwen-plus": {
        "api_url": "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation",
        "env_key": "ALIYUN_API_KEY",
        "headers": lambda key: {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        }
    }
}


class BaseLLMExtractor(ABC):
    """LLM提取器基类"""

    def __init__(self, model_name: str):
        self.model_name = model_name
        self.config = MODEL_CONFIGS.get(model_name)
        if not self.config:
            raise ValueError(f"不支持的模型: {model_name}")

        self.api_key = os.getenv(self.config["env_key"])
        if not self.api_key:
            raise ValueError(f"请在 .env 文件中配置 {self.config['env_key']}")

        self.api_url = self.config["api_url"]
        self.headers = self.config["headers"](self.api_key)

        self.stats = {
            "total": 0,
            "success": 0,
            "failed": 0,
            "errors": []
        }

    @abstractmethod
    def build_prompt(self, components: Dict[str, str], text: str) -> str:
        """构建提示词"""
        pass

    @abstractmethod
    def extract_with_prompt(self, text: str, prompt_components: Dict[str, str], max_retries: int = 3) -> Dict[str, Any]:
        """使用提示词提取信息"""
        pass

    def _make_api_request(self, payload: Dict, max_retries: int = 3) -> Optional[Dict]:
        """通用API请求方法"""
        for attempt in range(max_retries):
            try:
                response = requests.post(self.api_url, headers=self.headers, json=payload, timeout=120)

                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 429:
                    wait_time = 2 ** attempt
                    print(f"达到速率限制，等待 {wait_time} 秒后重试...")
                    time.sleep(wait_time)
                    continue
                else:
                    print(f"API请求失败: {response.status_code}")
                    print(f"错误信息: {response.text}")
                    break

            except Exception as e:
                print(f"请求异常: {e}")
                time.sleep(2 ** attempt)

        return None


class DeepSeekExtractor(BaseLLMExtractor):
    """DeepSeek模型提取器"""

    def __init__(self):
        super().__init__("deepseek-chat")

    def build_prompt(self, components: Dict[str, str], text: str) -> str:
        """为deepseek-reasoner优化的提示词"""
        cleaned_text = PDFTextExtractor.clean_text(text)
        if len(cleaned_text) > 8000:
            cleaned_text = cleaned_text[:8000] + "... [文本已截断]"

        prompt = f"""{components.get("role_context", "")}

请严格按照以下步骤分析腐蚀研究文献：

步骤1: 识别关键信息
- 缓蚀剂名称: {components.get('material_extraction', '')}
- 腐蚀对象: {components.get('corrosion_object_extraction', '')}  
- 实验环境: {components.get('corrosion_solution_extraction', '')}
- 缓蚀性能: {components.get('performance_extraction', '')}
- 测试方法: {components.get('numerical_emphasis', '')}

步骤2: 提取并结构化信息
步骤3: 输出最终JSON结果

【重要指令】
1. 先进行思考分析，然后输出最终JSON
2. 最终输出必须是纯JSON格式，不包含其他文本
3. JSON结构必须包含以下字段：
{{
  "Name of corrosion inhibitor": "缓蚀剂名称",
  "Corrosion Object Extraction": "腐蚀对象", 
  "experimental environment": "实验环境",
  "corrosion inhibition": "缓蚀性能",
  "test method": "测试方法"
}}

【文本内容】
{cleaned_text}
"""
        return prompt

    def extract_with_prompt(self, text, prompt_components, max_retries=3):
        """使用给定的提示词组件提取信息 - 针对deepseek-reasoner优化"""
        prompt = self.build_prompt(prompt_components, text)
        temperature = float(prompt_components.get("temperature", 0.1))

        payload = {
            "model": self.model_name,
            "messages": [
                {
                    "role": "system",
                    "content": "你是专业的材料科学文献解析助手。请先进行推理分析，然后输出最终的JSON结果。确保JSON格式正确且完整。"
                },
                {
                    "role": "user",
                    "content": prompt.strip()
                }
            ],
            "temperature": temperature,
            "max_tokens": 4000,
            "stream": False
        }

        result = self._make_api_request(payload, max_retries)
        if result:
            content = result["choices"][0]["message"]["content"]
            print(f"Debug - {self.model_name}原始响应: {content[:500]}...")

            extracted_data = self._extract_json_from_response_enhanced(content)
            if extracted_data and "error" not in extracted_data:
                fields = ["Name of corrosion inhibitor", "Corrosion Object Extraction",
                          "experimental environment", "corrosion inhibition", "test method"]
                for field in fields:
                    if field not in extracted_data:
                        extracted_data[field] = None
                return extracted_data
            else:
                print(f"未能从响应中提取有效JSON，尝试直接解析...")
                return self._construct_basic_json_from_response(content)

        return {"error": "提取失败"}

    # 保留原有的JSON处理方法
    def _extract_json_from_response_enhanced(self, content: str) -> Dict:
        """增强版JSON提取"""
        content = content.strip()
        print(f"Debug - 开始处理内容，长度: {len(content)}")

        if "思考过程" in content or "推理" in content or "步骤" in content:
            print("Debug - 检测到推理过程，尝试提取JSON部分")
            json_start_markers = ["```json", "JSON输出:", "最终结果:", "{", "```"]
            for marker in json_start_markers:
                if marker in content:
                    content_parts = content.split(marker)
                    if len(content_parts) > 1:
                        content = content_parts[-1].strip()
                        print(f"Debug - 使用标记 '{marker}' 分割后内容: {content[:200]}...")
                        break

        extraction_methods = [
            self._extract_json_block,
            self._extract_reasoner_json,
            self._extract_nested_json,
            self._extract_fallback_json
        ]

        for i, method in enumerate(extraction_methods):
            try:
                print(f"Debug - 尝试方法 {i + 1}: {method.__name__}")
                result = method(content)
                if result and "error" not in result:
                    print(f"Debug - 方法 {i + 1} 成功")
                    return result
            except Exception as e:
                print(f"Debug - 方法 {i + 1} 失败: {e}")
                continue

        print("Debug - 所有JSON提取方法都失败")
        return {"error": "所有JSON提取方法都失败"}

    def _extract_json_block(self, content: str) -> Dict:
        """提取代码块中的JSON"""
        json_block_match = re.search(r'```json\s*(.*?)\s*```', content, re.DOTALL)
        if json_block_match:
            json_str = json_block_match.group(1)
            try:
                return json.loads(self._clean_json_string(json_str))
            except json.JSONDecodeError:
                pass

        code_block_match = re.search(r'```\s*(.*?)\s*```', content, re.DOTALL)
        if code_block_match:
            json_str = code_block_match.group(1)
            try:
                return json.loads(self._clean_json_string(json_str))
            except json.JSONDecodeError:
                pass

        return None

    def _extract_reasoner_json(self, content: str) -> Dict:
        """专门处理reasoner的输出格式"""
        patterns = [
            r'最终结果[：:]?\s*```json\s*(.*?)\s*```',
            r'JSON输出[：:]?\s*(\{.*\})',
            r'思考过程.*?最终结果[：:]?\s*(\{.*\})',
            r'```json\s*(.*?)\s*```.*?思考结束',
            r'步骤3[：:].*?(\{.*\})',
        ]

        for pattern in patterns:
            match = re.search(pattern, content, re.DOTALL)
            if match:
                json_str = match.group(1)
                print(f"Debug - 模式匹配成功: {pattern}, 提取内容: {json_str[:100]}...")
                try:
                    return json.loads(self._clean_json_string(json_str))
                except Exception as e:
                    print(f"Debug - 模式匹配但解析失败: {e}")
                    continue

        return None

    def _extract_nested_json(self, content: str) -> Dict:
        """处理可能包含在复杂文本中的JSON"""
        stack = []
        start_index = -1
        json_objects = []

        for i, char in enumerate(content):
            if char == '{':
                if not stack:
                    start_index = i
                stack.append(char)
            elif char == '}':
                if stack:
                    stack.pop()
                    if not stack and start_index != -1:
                        json_str = content[start_index:i + 1]
                        json_objects.append(json_str)
                        start_index = -1

        json_objects.sort(key=len, reverse=True)
        for json_str in json_objects:
            print(f"Debug - 找到JSON对象，长度: {len(json_str)}, 内容: {json_str[:100]}...")
            try:
                return json.loads(self._clean_json_string(json_str))
            except Exception as e:
                print(f"Debug - JSON对象解析失败: {e}")
                continue

        return None

    def _extract_fallback_json(self, content: str) -> Dict:
        """回退提取方法"""
        content = content.strip()
        if content.startswith('{') and content.endswith('}'):
            try:
                return json.loads(self._clean_json_string(content))
            except:
                pass

        return None

    def _construct_basic_json_from_response(self, content: str) -> Dict:
        """从响应内容构建基本的JSON结构"""
        result = {
            "Name of corrosion inhibitor": None,
            "Corrosion Object Extraction": None,
            "experimental environment": None,
            "corrosion inhibition": None,
            "test method": None
        }

        lines = content.split('\n')
        current_field = None

        for line in lines:
            line_lower = line.lower().strip()

            if any(keyword in line_lower for keyword in ['缓蚀剂', 'inhibitor', 'extract', 'compound']):
                current_field = "Name of corrosion inhibitor"
            elif any(keyword in line_lower for keyword in ['腐蚀对象', 'steel', 'copper', 'aluminum', 'metal']):
                current_field = "Corrosion Object Extraction"
            elif any(keyword in line_lower for keyword in ['实验环境', 'environment', 'hcl', 'h2so4', 'h₂so₄', 'nacl']):
                current_field = "experimental environment"
            elif any(keyword in line_lower for keyword in ['缓蚀性能', 'efficiency', 'inhibition', '%', 'protection']):
                current_field = "corrosion inhibition"
            elif any(keyword in line_lower for keyword in ['测试方法', 'method', 'eis', 'pdp', 'weight loss']):
                current_field = "test method"

            if current_field and not result[current_field]:
                clean_line = re.sub(r'^[^a-zA-Z0-9]*', '', line.strip())
                clean_line = re.sub(r'[^a-zA-Z0-9].*$', '', clean_line)
                if clean_line and len(clean_line) > 2:
                    result[current_field] = clean_line

        return result

    def _clean_json_string(self, json_str: str) -> str:
        """清理JSON字符串中的常见问题"""
        if not json_str:
            return "{}"

        json_str = json_str.replace('\ufeff', '')

        if not json_str.strip().endswith('}'):
            last_brace = json_str.rfind('}')
            if last_brace != -1:
                json_str = json_str[:last_brace + 1]
            else:
                json_str = json_str + '}'

        if not json_str.strip().startswith('{'):
            first_brace = json_str.find('{')
            if first_brace != -1:
                json_str = json_str[first_brace:]
            else:
                json_str = '{' + json_str

        json_str = json_str.replace('\\"', '"')
        json_str = re.sub(r'([{,]\s*)([a-zA-Z_][a-zA-Z0-9_]*)(\s*:)', r'\1"\2"\3', json_str)
        json_str = json_str.replace("'", '"')
        json_str = re.sub(r'\s+', ' ', json_str)
        json_str = re.sub(r':\s*null\s*([,}])', r': null\1', json_str)

        return json_str.strip()


class OpenAIExtractor(BaseLLMExtractor):
    """OpenAI模型提取器（统一提示词版本）"""

    def __init__(self):
        super().__init__("gpt-4")

    def build_prompt(self, components: Dict[str, str], text: str) -> str:
        """采用与DeepSeek相同的提示词结构"""
        cleaned_text = PDFTextExtractor.clean_text(text)
        if len(cleaned_text) > 8000:
            cleaned_text = cleaned_text[:8000] + "... [文本已截断]"

        prompt = f"""{components.get("role_context", "")}

请严格按照以下步骤分析腐蚀研究文献：

步骤1: 识别关键信息
- 缓蚀剂名称: {components.get('material_extraction', '')}
- 腐蚀对象: {components.get('corrosion_object_extraction', '')}  
- 实验环境: {components.get('corrosion_solution_extraction', '')}
- 缓蚀性能: {components.get('performance_extraction', '')}
- 测试方法: {components.get('numerical_emphasis', '')}

步骤2: 提取并结构化信息
步骤3: 输出最终JSON结果

【重要指令】
1. 先进行思考分析，然后输出最终JSON
2. 最终输出必须是纯JSON格式，不包含其他文本
3. JSON结构必须包含以下字段：
{{
  "Name of corrosion inhibitor": "缓蚀剂名称",
  "Corrosion Object Extraction": "腐蚀对象", 
  "experimental environment": "实验环境",
  "corrosion inhibition": "缓蚀性能",
  "test method": "测试方法"
}}

【文本内容】
{cleaned_text}
"""
        return prompt

    def extract_with_prompt(self, text, prompt_components, max_retries=3):
        """使用与DeepSeek相同的提取逻辑"""
        prompt = self.build_prompt(prompt_components, text)
        temperature = float(prompt_components.get("temperature", 0.1))

        payload = {
            "model": self.model_name,
            "messages": [
                {
                    "role": "system",
                    "content": "你是专业的材料科学文献解析助手。请先进行推理分析，然后输出最终的JSON结果。确保JSON格式正确且完整。"
                },
                {
                    "role": "user",
                    "content": prompt.strip()
                }
            ],
            "temperature": temperature,
            "max_tokens": 4000,
            "response_format": {"type": "json_object"}
        }

        result = self._make_api_request(payload, max_retries)
        if result:
            content = result["choices"][0]["message"]["content"]
            print(f"Debug - {self.model_name}原始响应: {content[:500]}...")

            # 使用与DeepSeek相同的JSON提取逻辑
            extracted_data = self._extract_json_from_response_enhanced(content)
            if extracted_data and "error" not in extracted_data:
                fields = ["Name of corrosion inhibitor", "Corrosion Object Extraction",
                          "experimental environment", "corrosion inhibition", "test method"]
                for field in fields:
                    if field not in extracted_data:
                        extracted_data[field] = None
                return extracted_data
            else:
                print(f"未能从响应中提取有效JSON，尝试直接解析...")
                return self._construct_basic_json_from_response(content)

        return {"error": "提取失败"}

    # 复制DeepSeek的所有JSON处理方法
    _extract_json_from_response_enhanced = DeepSeekExtractor._extract_json_from_response_enhanced
    _extract_json_block = DeepSeekExtractor._extract_json_block
    _extract_reasoner_json = DeepSeekExtractor._extract_reasoner_json
    _extract_nested_json = DeepSeekExtractor._extract_nested_json
    _extract_fallback_json = DeepSeekExtractor._extract_fallback_json
    _construct_basic_json_from_response = DeepSeekExtractor._construct_basic_json_from_response
    _clean_json_string = DeepSeekExtractor._clean_json_string


class GPT4oExtractor(BaseLLMExtractor):
    """GPT-4o 模型提取器"""

    def __init__(self):
        super().__init__("gpt-4o")
        # 使用配置中的实际模型名称
        self.actual_model_name = "gpt-4o"

    def build_prompt(self, components: Dict[str, str], text: str) -> str:
        """为 GPT-4o 优化的提示词"""
        cleaned_text = PDFTextExtractor.clean_text(text)
        if len(cleaned_text) > 6000:
            cleaned_text = cleaned_text[:6000] + "... [文本已截断]"

        prompt = f"""{components.get("role_context", "")}

请从以下腐蚀研究文献中提取结构化信息：

【提取字段】
1. 缓蚀剂名称: {components.get('material_extraction', '')}
2. 腐蚀对象: {components.get('corrosion_object_extraction', '')}  
3. 实验环境: {components.get('corrosion_solution_extraction', '')}
4. 缓蚀性能: {components.get('performance_extraction', '')}
5. 测试方法: {components.get('numerical_emphasis', '')}

【输出要求】
请输出标准的JSON格式：
{{
  "Name of corrosion inhibitor": "缓蚀剂名称",
  "Corrosion Object Extraction": "腐蚀对象", 
  "experimental environment": "实验环境",
  "corrosion inhibition": "缓蚀性能",
  "test method": "测试方法"
}}

【文本内容】
{cleaned_text}
"""
        return prompt

    def extract_with_prompt(self, text, prompt_components, max_retries=3):
        """GPT-4o 提取方法"""
        prompt = self.build_prompt(prompt_components, text)
        temperature = float(prompt_components.get("temperature", 0.1))

        payload = {
            "model": self.actual_model_name,
            "messages": [
                {
                    "role": "user",
                    "content": prompt.strip()
                }
            ],
            "temperature": temperature,
            "max_tokens": 2000,
            "stream": False
        }

        print(f"🔧 使用模型: {self.actual_model_name}")

        for attempt in range(max_retries):
            try:
                print(f"🔄 尝试 {attempt + 1}/{max_retries}")
                response = requests.post(
                    self.api_url,
                    headers=self.headers,
                    json=payload,
                    timeout=60
                )

                print(f"📡 响应状态码: {response.status_code}")

                if response.status_code == 200:
                    result = response.json()
                    content = result["choices"][0]["message"]["content"]
                    print(f"✅ 收到响应，长度: {len(content)} 字符")

                    # 提取JSON
                    extracted_data = self._extract_json(content)
                    if extracted_data:
                        return extracted_data
                    else:
                        return self._create_fallback_result(content)

                elif response.status_code == 404:
                    print(f"❌ 404错误: 模型可能不可用")
                    # 如果 GPT-4o 不可用，回退到 GPT-4
                    if self.actual_model_name == "gpt-4o":
                        print("🔄 尝试回退到 gpt-4 模型")
                        self.actual_model_name = "gpt-4"
                        payload["model"] = "gpt-4"
                        continue
                    break
                else:
                    print(f"❌ HTTP错误 {response.status_code}")
                    if attempt < max_retries - 1:
                        wait_time = 2 ** attempt
                        print(f"等待 {wait_time} 秒后重试...")
                        time.sleep(wait_time)

            except requests.exceptions.RequestException as e:
                print(f"❌ 请求异常: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
            except Exception as e:
                print(f"❌ 未知异常: {e}")
                break

        return {"error": f"提取失败，已重试 {max_retries} 次"}

    def _extract_json(self, content: str):
        """提取JSON数据 - 复用DeepSeek的方法"""
        content = content.strip()

        # 尝试从代码块中提取JSON
        json_match = re.search(r'```json\s*(.*?)\s*```', content, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
            try:
                return json.loads(self._clean_json_string(json_str))
            except json.JSONDecodeError:
                pass

        # 尝试直接查找JSON对象
        brace_match = re.search(r'\{.*\}', content, re.DOTALL)
        if brace_match:
            json_str = brace_match.group(0)
            try:
                return json.loads(self._clean_json_string(json_str))
            except json.JSONDecodeError:
                pass

        return None

    def _create_fallback_result(self, content: str) -> Dict:
        """创建回退结果 - 复用DeepSeek的方法"""
        result = {
            "Name of corrosion inhibitor": None,
            "Corrosion Object Extraction": None,
            "experimental environment": None,
            "corrosion inhibition": None,
            "test method": None
        }

        # 简单的关键词匹配
        lines = content.split('\n')
        for line in lines:
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in ['inhibitor', 'extract', 'compound']):
                if not result["Name of corrosion inhibitor"]:
                    result["Name of corrosion inhibitor"] = line.strip()[:100]
            elif any(keyword in line_lower for keyword in ['steel', 'copper', 'aluminum', 'metal']):
                if not result["Corrosion Object Extraction"]:
                    result["Corrosion Object Extraction"] = line.strip()[:100]
            elif any(keyword in line_lower for keyword in ['hcl', 'h2so4', 'h₂so₄', 'nacl', 'acid']):
                if not result["experimental environment"]:
                    result["experimental environment"] = line.strip()[:100]
            elif any(keyword in line_lower for keyword in ['efficiency', 'inhibition', '%', 'protection']):
                if not result["corrosion inhibition"]:
                    result["corrosion inhibition"] = line.strip()[:100]
            elif any(keyword in line_lower for keyword in ['method', 'eis', 'pdp', 'weight loss']):
                if not result["test method"]:
                    result["test method"] = line.strip()[:100]

        return result

    def _clean_json_string(self, json_str: str) -> str:
        """清理JSON字符串 - 复用DeepSeek的方法"""
        json_str = json_str.strip()
        json_str = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', json_str)
        json_str = json_str.replace('\\"', '"')
        json_str = json_str.replace("'", '"')
        json_str = re.sub(r',\s*}', '}', json_str)
        json_str = re.sub(r',\s*]', ']', json_str)
        return json_str


class ClaudeExtractor(BaseLLMExtractor):
    """Claude模型提取器（统一提示词版本）"""

    def __init__(self):
        super().__init__("claude-3-sonnet")

    def build_prompt(self, components: Dict[str, str], text: str) -> str:
        """采用与DeepSeek相同的提示词结构"""
        cleaned_text = PDFTextExtractor.clean_text(text)
        if len(cleaned_text) > 8000:
            cleaned_text = cleaned_text[:8000] + "... [文本已截断]"

        prompt = f"""{components.get("role_context", "")}

请严格按照以下步骤分析腐蚀研究文献：

步骤1: 识别关键信息
- 缓蚀剂名称: {components.get('material_extraction', '')}
- 腐蚀对象: {components.get('corrosion_object_extraction', '')}  
- 实验环境: {components.get('corrosion_solution_extraction', '')}
- 缓蚀性能: {components.get('performance_extraction', '')}
- 测试方法: {components.get('numerical_emphasis', '')}

步骤2: 提取并结构化信息
步骤3: 输出最终JSON结果

【重要指令】
1. 先进行思考分析，然后输出最终JSON
2. 最终输出必须是纯JSON格式，不包含其他文本
3. JSON结构必须包含以下字段：
{{
  "Name of corrosion inhibitor": "缓蚀剂名称",
  "Corrosion Object Extraction": "腐蚀对象", 
  "experimental environment": "实验环境",
  "corrosion inhibition": "缓蚀性能",
  "test method": "测试方法"
}}

【文本内容】
{cleaned_text}
"""
        return prompt

    def extract_with_prompt(self, text, prompt_components, max_retries=3):
        """使用与DeepSeek相同的提取逻辑"""
        prompt = self.build_prompt(prompt_components, text)

        payload = {
            "model": self.model_name,
            "max_tokens": 4000,
            "messages": [
                {
                    "role": "user",
                    "content": prompt.strip()
                }
            ]
        }

        result = self._make_api_request(payload, max_retries)
        if result:
            content = result["content"][0]["text"]
            print(f"Debug - {self.model_name}原始响应: {content[:500]}...")

            # 使用与DeepSeek相同的JSON提取逻辑
            extracted_data = self._extract_json_from_response_enhanced(content)
            if extracted_data and "error" not in extracted_data:
                fields = ["Name of corrosion inhibitor", "Corrosion Object Extraction",
                          "experimental environment", "corrosion inhibition", "test method"]
                for field in fields:
                    if field not in extracted_data:
                        extracted_data[field] = None
                return extracted_data
            else:
                print(f"未能从响应中提取有效JSON，尝试直接解析...")
                return self._construct_basic_json_from_response(content)

        return {"error": "提取失败"}

    # 复制DeepSeek的所有JSON处理方法
    _extract_json_from_response_enhanced = DeepSeekExtractor._extract_json_from_response_enhanced
    _extract_json_block = DeepSeekExtractor._extract_json_block
    _extract_reasoner_json = DeepSeekExtractor._extract_reasoner_json
    _extract_nested_json = DeepSeekExtractor._extract_nested_json
    _extract_fallback_json = DeepSeekExtractor._extract_fallback_json
    _construct_basic_json_from_response = DeepSeekExtractor._construct_basic_json_from_response
    _clean_json_string = DeepSeekExtractor._clean_json_string


class QwenExtractor(BaseLLMExtractor):
    """通义千问模型提取器（统一提示词版本）"""

    def __init__(self):
        super().__init__("qwen-plus")

    def build_prompt(self, components: Dict[str, str], text: str) -> str:
        """采用与DeepSeek相同的提示词结构"""
        cleaned_text = PDFTextExtractor.clean_text(text)
        if len(cleaned_text) > 8000:
            cleaned_text = cleaned_text[:8000] + "... [文本已截断]"

        prompt = f"""{components.get("role_context", "")}

请严格按照以下步骤分析腐蚀研究文献：

步骤1: 识别关键信息
- 缓蚀剂名称: {components.get('material_extraction', '')}
- 腐蚀对象: {components.get('corrosion_object_extraction', '')}  
- 实验环境: {components.get('corrosion_solution_extraction', '')}
- 缓蚀性能: {components.get('performance_extraction', '')}
- 测试方法: {components.get('numerical_emphasis', '')}

步骤2: 提取并结构化信息
步骤3: 输出最终JSON结果

【重要指令】
1. 先进行思考分析，然后输出最终JSON
2. 最终输出必须是纯JSON格式，不包含其他文本
3. JSON结构必须包含以下字段：
{{
  "Name of corrosion inhibitor": "缓蚀剂名称",
  "Corrosion Object Extraction": "腐蚀对象", 
  "experimental environment": "实验环境",
  "corrosion inhibition": "缓蚀性能",
  "test method": "测试方法"
}}

【文本内容】
{cleaned_text}
"""
        return prompt

    def extract_with_prompt(self, text, prompt_components, max_retries=3):
        """使用与DeepSeek相同的提取逻辑"""
        prompt = self.build_prompt(prompt_components, text)

        payload = {
            "model": "qwen-plus",
            "input": {
                "messages": [
                    {
                        "role": "user",
                        "content": prompt.strip()
                    }
                ]
            },
            "parameters": {
                "result_format": "message"
            },
            "stream": False
        }

        result = self._make_api_request(payload, max_retries)
        if result:
            try:
                content = result["output"]["choices"][0]["message"]["content"]
                print(f"Debug - {self.model_name}原始响应: {content[:500]}...")

                # 使用与DeepSeek相同的JSON提取逻辑
                extracted_data = self._extract_json_from_response_enhanced(content)
                if extracted_data and "error" not in extracted_data:
                    fields = ["Name of corrosion inhibitor", "Corrosion Object Extraction",
                              "experimental environment", "corrosion inhibition", "test method"]
                    for field in fields:
                        if field not in extracted_data:
                            extracted_data[field] = None
                    return extracted_data
                else:
                    print(f"未能从响应中提取有效JSON，尝试直接解析...")
                    return self._construct_basic_json_from_response(content)
            except (KeyError, IndexError, TypeError) as e:
                print(f"响应结构异常: {e}")
                return {"error": "响应结构错误", "raw": result}

        return {"error": "API请求失败"}

    # 复制DeepSeek的所有JSON处理方法
    _extract_json_from_response_enhanced = DeepSeekExtractor._extract_json_from_response_enhanced
    _extract_json_block = DeepSeekExtractor._extract_json_block
    _extract_reasoner_json = DeepSeekExtractor._extract_reasoner_json
    _extract_nested_json = DeepSeekExtractor._extract_nested_json
    _extract_fallback_json = DeepSeekExtractor._extract_fallback_json
    _construct_basic_json_from_response = DeepSeekExtractor._construct_basic_json_from_response
    _clean_json_string = DeepSeekExtractor._clean_json_string


# 腐蚀文献提取器（兼容原有接口）
class CorrosionExtractor:
    def __init__(self, model_name="deepseek-chat"):
        """
        初始化腐蚀文献提取器

        Args:
            model_name: 模型名称，可选值:
                       "deepseek-reasoner", "gpt-4", "gpt-4o", "claude-3-sonnet", "qwen-plus"
        """
        self.model_name = model_name
        self.extractor = self._create_extractor(model_name)

        self.stats = {
            "total": 0,
            "success": 0,
            "failed": 0,
            "errors": []
        }

    def _create_extractor(self, model_name):
        """创建对应的模型提取器"""
        extractors = {
            "deepseek-chat": DeepSeekExtractor,
            "gpt-4": OpenAIExtractor,
            "gpt-4o": GPT4oExtractor,  # 新增 GPT-4o
            "claude-3-sonnet": ClaudeExtractor,
            "qwen-plus": QwenExtractor
        }

        if model_name not in extractors:
            raise ValueError(f"不支持的模型: {model_name}。支持: {list(extractors.keys())}")

        return extractors[model_name]()

    def extract_with_prompt(self, text, prompt_components, max_retries=3):
        """使用给定的提示词组件提取信息"""
        return self.extractor.extract_with_prompt(text, prompt_components, max_retries)

    def batch_process_with_prompt(self, texts, prompt_components, filenames=None, batch_delay=2.0):
        """使用给定的提示词组件批量处理文献"""
        results = []
        failed_count = 0

        if filenames is None:
            filenames = [f"文献_{i + 1}" for i in range(len(texts))]

        self.stats["total"] = len(texts)

        for i, (text, filename) in enumerate(tqdm(zip(texts, filenames),
                                                  desc=f"处理腐蚀文献 ({self.model_name})",
                                                  total=len(texts))):
            if not text or not text.strip():
                results.append({"filename": filename, "error": "空文本或提取失败"})
                failed_count += 1
                continue

            result = self.extract_with_prompt(text, prompt_components)
            result["filename"] = filename

            if "error" in result:
                failed_count += 1
                print(f"处理失败: {filename}")
            else:
                self.stats["success"] += 1

            results.append(result)

            if i < len(texts) - 1:
                time.sleep(batch_delay)

        self.stats["failed"] = failed_count
        print(f"处理完成！成功: {self.stats['success']}, 失败: {self.stats['failed']}")
        return results

    # 保留原有的评估方法
    def calculate_f1_score(self, extracted: Dict, gold: Dict) -> Tuple[float, float, float]:
        """F1分数计算"""
        fields = ["Name of corrosion inhibitor", "Corrosion Object Extraction",
                  "experimental environment", "corrosion inhibition", "test method"]

        total_precision = 0.0
        total_recall = 0.0
        total_f1 = 0.0
        evaluated_fields = 0

        for field in fields:
            if field not in gold or not gold[field]:
                continue

            gold_val = str(gold[field]).lower().strip()
            extracted_val = str(extracted.get(field, "")).lower().strip() if extracted.get(field) else ""

            precision, recall = self.calculate_simple_precision_recall(extracted_val, gold_val)

            if precision + recall > 0:
                f1 = 2 * (precision * recall) / (precision + recall)
            else:
                f1 = 0.0

            total_precision += precision
            total_recall += recall
            total_f1 += f1
            evaluated_fields += 1

        if evaluated_fields == 0:
            return 0.0, 0.0, 0.0

        avg_precision = total_precision / evaluated_fields
        avg_recall = total_recall / evaluated_fields
        avg_f1 = total_f1 / evaluated_fields

        return avg_precision, avg_recall, avg_f1

    def calculate_simple_precision_recall(self, extracted_val: str, gold_val: str) -> Tuple[float, float]:
        """精确率和召回率计算"""
        if not gold_val:
            return 0.0, 0.0

        if not extracted_val or extracted_val == "null":
            return 0.0, 0.0

        if extracted_val == gold_val:
            return 1.0, 1.0

        base_similarity = self.sequence_similarity(extracted_val, gold_val)
        base_similarity = max(0.0, min(1.0, base_similarity))

        gold_segments = self.extract_meaningful_segments(gold_val)
        extracted_segments = self.extract_meaningful_segments(extracted_val)

        if not gold_segments:
            return base_similarity, base_similarity

        matched_segments = 0
        for gold_segment in gold_segments:
            for extracted_segment in extracted_segments:
                if self.is_segment_match(gold_segment, extracted_segment, threshold=0.7):
                    matched_segments += 1
                    break

        if extracted_segments:
            precision = matched_segments / len(extracted_segments)
        else:
            precision = 0.0

        recall = matched_segments / len(gold_segments)

        precision_final = max(precision, base_similarity)
        recall_final = max(recall, base_similarity)

        precision_final = max(0.0, min(1.0, precision_final))
        recall_final = max(0.0, min(1.0, recall_final))

        return precision_final, recall_final

    def normalize_text(self, text: str) -> str:
        """文本标准化处理"""
        if not text:
            return ""

        text = text.lower()
        text = re.sub(r'\s+', ' ', text)

        replacements = {
            r'h2so4': 'h₂so₄',
            r'hcl': 'hcl',
            r'naoh': 'naoh',
            r'na2so4': 'na₂so₄',
            r'mg/l': 'mg/l',
            r'ppm': 'ppm',
            r'mol/l': 'mol/l',
            r'\bm\b': 'mol/l',
            r'wt\.?%': 'wt%',
            r'v/v%': 'v/v',
            r'°c': '°c',
            r'\bc\b': '°c'
        }

        for pattern, replacement in replacements.items():
            text = re.sub(pattern, replacement, text)

        return text.strip()

    def extract_meaningful_segments(self, text: str) -> List[str]:
        """提取有意义的文本片段"""
        if not text:
            return []

        segments = []

        punctuation_segments = re.split(r'[;,.]\s*', text)
        meaningful_segments = [s.strip() for s in punctuation_segments if len(s.strip()) > 3]
        segments.extend(meaningful_segments)

        number_unit_pattern = r'[±]?\d*\.?\d+\s*(?:ppm|mg/l|g/l|mol/l|m|%|wt%|v/v|°c|k|h|min|s|mm/year|ma/cm²|mv|v|ω)'
        number_matches = re.findall(number_unit_pattern, text, re.IGNORECASE)
        segments.extend(number_matches)

        technical_terms = re.findall(
            r'\b(?:hcl|h2so4|h₂so₄|nacl|naoh|eis|pdp|sem|xrd|xps|afm|ftir|uv-vis|nmr|tga|dsc|cv|ocp|weight\s+loss|potentiodynamic)\b',
            text, re.IGNORECASE)
        segments.extend(technical_terms)

        inhibitor_pattern = r'\b(?:[a-z][a-z\s]+\s+(?:extract|oil|leaf|root|stem|flower|seed|inhibitor))\b'
        inhibitor_matches = re.findall(inhibitor_pattern, text, re.IGNORECASE)
        segments.extend(inhibitor_matches)

        unique_segments = []
        for segment in segments:
            if segment and segment not in unique_segments and len(segment) > 2:
                unique_segments.append(segment)

        return unique_segments

    def is_segment_match(self, segment1: str, segment2: str, threshold: float = 0.7) -> bool:
        """片段匹配"""
        if segment1 == segment2:
            return True

        if segment1 in segment2 or segment2 in segment1:
            return True

        similarity = SequenceMatcher(None, segment1, segment2).ratio()
        return similarity >= threshold

    def sequence_similarity(self, text1: str, text2: str) -> float:
        """计算两个文本的序列相似度"""
        return SequenceMatcher(None, text1, text2).ratio()

    def save_results(self, results, filepath=None):
        """保存腐蚀文献提取结果到文件"""
        OUTPUT_DIR = f"{self.model_name}_results"
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        if filepath is None:
            json_path = os.path.join(OUTPUT_DIR, f"{self.model_name}_extraction_results.json")
        elif os.path.isabs(filepath):
            json_path = filepath
        else:
            json_path = os.path.join(OUTPUT_DIR, filepath)

        os.makedirs(os.path.dirname(json_path), exist_ok=True)

        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

        csv_filename = os.path.splitext(os.path.basename(json_path))[0] + ".csv"
        csv_path = os.path.join(os.path.dirname(json_path), csv_filename)

        csv_data = []
        for idx, result in enumerate(results):
            if "error" in result:
                csv_data.append({
                    "序号": idx + 1,
                    "文件名": result.get("filename", ""),
                    "缓蚀剂名称": "提取失败",
                    "腐蚀对象": "",
                    "实验环境": "",
                    "缓蚀性能": "",
                    "测试方法": "",
                    "错误信息": result["error"]
                })
            else:
                csv_data.append({
                    "文件名": result.get("filename", ""),
                    "缓蚀剂名称": result.get("Name of corrosion inhibitor", ""),
                    "腐蚀对象": result.get("Corrosion Object Extraction", ""),
                    "实验环境": result.get("experimental environment", ""),
                    "缓蚀性能": result.get("corrosion inhibition", ""),
                    "测试方法": result.get("test method", ""),
                    "错误信息": ""
                })

        df = pd.DataFrame(csv_data)
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')

        print(f"结果已保存至：{json_path} 和 {csv_path}")


# PDF文本提取器（保持不变）
class PDFTextExtractor:
    """PDF文本提取器"""

    @staticmethod
    def extract_text_from_pdf(pdf_path):
        """从PDF文件提取文本内容"""
        try:
            with open(pdf_path, 'rb') as file:
                reader = pdfplumber.open(file)
                text = ""
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                return text
        except Exception as e:
            print(f"提取PDF文本失败 {pdf_path}: {e}")
            return ""

    @staticmethod
    def clean_text(text):
        """清理文本，移除多余空格和换行"""
        text = re.sub(r'\n+', '\n', text)
        text = re.sub(r' +', ' ', text)
        return text.strip()


def load_pdfs_from_folder(folder_path):
    """从文件夹加载所有PDF文件并提取文本"""
    pdf_extractor = PDFTextExtractor()
    texts = []
    filenames = []

    pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

    if not pdf_files:
        print(f"在文件夹 {folder_path} 中未找到PDF文件")
        return [], []

    def natural_sort_key(filename):
        numbers = re.findall(r'\d+', filename)
        if numbers:
            return int(numbers[0])
        return filename

    pdf_files.sort(key=natural_sort_key)

    print(f"找到 {len(pdf_files)} 个PDF文件，开始提取文本...")

    for pdf_file in tqdm(pdf_files, desc="提取PDF文本"):
        text = pdf_extractor.extract_text_from_pdf(os.path.join(folder_path, pdf_file))
        if text.strip():
            texts.append(text)
            filenames.append(pdf_file)
        else:
            print(f"警告: {pdf_file} 提取的文本为空")

    return texts, filenames