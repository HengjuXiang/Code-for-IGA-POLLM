# manual_main.py - 三种提示词策略对比实验（支持多模型）
import os
import time
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import json
import random
import argparse
import requests
from LLM import CorrosionExtractor, load_pdfs_from_folder, PDFTextExtractor
from Standard import GOLD_STANDARDS, PDF_FOLDER, GENE_DEFINITIONS

# 设置matplotlib全局字体为Arial
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10

# 支持的模型列表 - 修正为正确的模型名称
SUPPORTED_MODELS = ["deepseek-chat", "gpt-4", "gpt-4o", "claude-3-sonnet", "qwen-plus"]

# 人工选择的提示词组件
MANUAL_PROMPT_COMPONENTS = {
    "role_context": " As a professional analyst in corrosion science, systematically analyze experimental data from literature. Your task is to accurately extract core parameters of corrosion inhibitor research, ensuring information completeness and accuracy.",
    "material_extraction": " Systematically identify corrosion inhibitor materials used in the text, including plant extracts, chemical compounds, composite materials, and all types of inhibitor names.",
    "corrosion_object_extraction": " Extract corrosion object names. Format: 'object name', e.g., 'carbon steel', 'stainless steel', 'copper', 'aluminum'.",
    "corrosion_solution_extraction": " Extract corrosion medium type and concentration. Format: 'concentration medium', e.g., '0.5M H₂SO₄', '1 M HCl', '3.5% NaCl'.",
    "performance_extraction": " Systematically record complete performance data of corrosion inhibitors. Include: inhibition efficiency values, corresponding corrosion inhibitor concentrations, and test corrosion media used.",
    "numerical_emphasis": "Identify experimental methods used to evaluate corrosion inhibition performance in the text. Include corrosion rate measurement methods, surface analysis techniques, electrochemical test methods, etc.",
    "temperature": 0.1
}

# GA优化后的提示词组件
GA_OPTIMIZED_PROMPT_COMPONENTS = {
    "role_context": "You are a corrosion literature extraction tool. Strictly extract information in specified format: inhibitor name, concentration, corrosion solution, performance, test methods.  Only output JSON format results",
    "material_extraction": "Corrosion inhibitor name is the core element for material identification. Extract clearly mentioned inhibitor substance names from the text",
    "corrosion_object_extraction": "Extract corrosion object names. Format: 'object name', e.g., 'carbon steel', 'stainless steel', 'copper', 'aluminum'",
    "corrosion_solution_extraction": "Corrosion solution core information contains two elements: 1) medium type (HCl/H₂SO₄/NaCl, etc.) 2) medium concentration (0.5M/1M/3.5%, etc.). Extract and combine these two elements",
    "performance_extraction": " Extract complete corrosion inhibition performance description. Pay attention to the complete association between inhibition efficiency, corrosion inhibitor, and corrosion medium.",
    "numerical_emphasis": " Extract test method names. Format: 'method1, method2, method3', e.g., 'weight loss, EIS, polarization'. Separate with commas, list only method names",
    "temperature": 0.1
}


def generate_random_prompt():
    """随机生成提示词组件"""
    random_prompt = {}
    for gene_name, alleles in GENE_DEFINITIONS.items():
        if gene_name == "temperature":
            random_prompt[gene_name] = random.choice([0.1, 0.2])
        else:
            random_prompt[gene_name] = random.choice(alleles)
    return random_prompt


def format_time(seconds):
    """格式化时间显示"""
    if seconds < 60:
        return f"{seconds:.2f}秒"
    elif seconds < 3600:
        minutes = seconds // 60
        seconds %= 60
        return f"{int(minutes)}分{seconds:.2f}秒"
    else:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds %= 60
        return f"{int(hours)}小时{int(minutes)}分{seconds:.2f}秒"


def run_extraction_experiment(extractor, texts, gold_standards, prompt_components, strategy_name, filenames):
    """运行单个提取实验"""
    print(f"\n=== 开始 {strategy_name} 提示词实验 ===")
    print(f"提示词策略: {strategy_name}")
    print(f"使用模型: {extractor.model_name}")

    extraction_results = []
    metrics_data = []
    total_f1 = 0.0
    total_precision = 0.0
    total_recall = 0.0
    valid_count = 0

    for i, text in enumerate(texts):
        print(f"处理文献 {i + 1}/{len(texts)}: {filenames[i]}")

        # 添加详细的调试信息
        print(f"  文本长度: {len(text)} 字符")
        print(f"  提示词组件: {list(prompt_components.keys())}")

        result = extractor.extract_with_prompt(text, prompt_components)
        result["filename"] = filenames[i]
        result["gold_standard"] = gold_standards[i]
        extraction_results.append(result)

        # 计算指标
        if "error" not in result:
            precision, recall, f1_score = extractor.calculate_f1_score(result, gold_standards[i])
            total_f1 += f1_score
            total_precision += precision
            total_recall += recall
            valid_count += 1

            metrics_data.append({
                "filename": result['filename'],
                "strategy": strategy_name,
                "model": extractor.model_name,
                "f1_score": f1_score,
                "precision": precision,
                "recall": recall,
                "extracted_inhibitor": result.get('Name of corrosion inhibitor', ''),
                "extracted_object": result.get('Corrosion Object Extraction', ''),
                "extracted_environment": result.get('experimental environment', ''),
                "extracted_performance": result.get('corrosion inhibition', ''),
                "extracted_method": result.get('test method', '')
            })

            print(f"  ✅ 提取成功 - F1: {f1_score:.4f}")
        else:
            print(f"  ❌ 提取失败: {result['error']}")
            metrics_data.append({
                "filename": result['filename'],
                "strategy": strategy_name,
                "model": extractor.model_name,
                "f1_score": 0.0,
                "precision": 0.0,
                "recall": 0.0,
                "error": result['error']
            })

        # 添加延迟避免API限制
        if i < len(texts) - 1:
            print(f"  等待 3 秒...")
            time.sleep(3)

    # 计算平均指标
    if valid_count > 0:
        avg_f1 = total_f1 / valid_count
        avg_precision = total_precision / valid_count
        avg_recall = total_recall / valid_count
    else:
        avg_f1 = avg_precision = avg_recall = 0.0

    print(f"{strategy_name} 实验结果:")
    print(f"  成功处理文献数量: {valid_count}/{len(extraction_results)}")
    print(f"  平均F1分数: {avg_f1:.4f}")
    print(f"  平均精确率: {avg_precision:.4f}")
    print(f"  平均召回率: {avg_recall:.4f}")

    return {
        "strategy_name": strategy_name,
        "model_name": extractor.model_name,
        "extraction_results": extraction_results,
        "metrics_data": metrics_data,
        "avg_f1": avg_f1,
        "avg_precision": avg_precision,
        "avg_recall": avg_recall,
        "valid_count": valid_count,
        "total_count": len(extraction_results)
    }


def plot_comparison_results(all_experiment_results, save_path=None):
    """绘制三种策略的对比结果"""

    # 将策略名称映射为英文
    strategy_name_mapping = {
        "人工选择": "Professional expertise",
        "随机生成": "Random Generation",
        "GA优化": "GA Optimized"
    }

    # 使用英文策略名称
    strategies = [strategy_name_mapping.get(result["strategy_name"], result["strategy_name"])
                  for result in all_experiment_results]

    avg_f1_scores = [result["avg_f1"] for result in all_experiment_results]
    avg_precisions = [result["avg_precision"] for result in all_experiment_results]
    avg_recalls = [result["avg_recall"] for result in all_experiment_results]

    # 创建对比图
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # 柱状图对比
    x = range(len(strategies))
    width = 0.25

    bars1 = ax1.bar([i - width for i in x], avg_f1_scores, width, label='F1 score', color='lightblue', alpha=0.7)
    bars2 = ax1.bar(x, avg_precisions, width, label='Precision', color='lightgreen', alpha=0.7)
    bars3 = ax1.bar([i + width for i in x], avg_recalls, width, label='Recall', color='lightcoral', alpha=0.7)

    ax1.set_xlabel('Source of prompts', fontsize=12, fontname='Arial', fontweight='bold')
    ax1.set_ylabel('Score', fontsize=12, fontname='Arial', fontweight='bold')
    ax1.set_title(
        f'Comparison of the Performance of Three Types of Prompt Words\nModel: {all_experiment_results[0]["model_name"] if all_experiment_results else "Unknown"}',
        fontsize=14, fontweight='bold', fontname='Arial')
    ax1.set_xticks(x)
    ax1.set_xticklabels(strategies, fontname='Arial', fontweight='bold')
    ax1.set_ylim(0, 1.1)
    ax1.legend(loc='upper left', prop={'family': 'Arial'})
    ax1.grid(True, alpha=0.3)

    # 设置y轴刻度标签字体为Arial + 加粗
    for label in ax1.get_yticklabels():
        label.set_fontname('Arial')
        label.set_weight('bold')

    # 添加数值标签
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width() / 2., height + 0.01,
                     f'{height:.3f}', ha='center', va='bottom', fontsize=9, fontname='Arial')

    # 雷达图对比
    ax2 = fig.add_subplot(2, 1, 2, polar=True)

    categories = ['F1 score', 'Precision', 'Recall']
    N = len(categories)

    angles = [n / float(N) * 2 * 3.14159 for n in range(N)]
    angles += angles[:1]

    colors = ['lightblue', 'lightgreen', 'lightcoral']
    for i, result in enumerate(all_experiment_results):
        values = [result["avg_f1"], result["avg_precision"], result["avg_recall"]]
        values += values[:1]
        label = strategy_name_mapping.get(result["strategy_name"], result["strategy_name"])
        ax2.plot(angles, values, 'o-', linewidth=2, label=label, color=colors[i])
        ax2.fill(angles, values, alpha=0.1, color=colors[i])

    ax2.set_xticks(angles[:-1])
    ax2.set_xticklabels(categories, fontname='Arial', fontweight='bold')
    ax2.set_ylim(0, 1.0)
    ax2.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    for label in ax2.get_yticklabels():
        label.set_fontname('Arial')
        label.set_weight('bold')
    ax2.grid(True)
    ax2.legend(loc='upper left', bbox_to_anchor=(-0.835, 1.0), prop={'family': 'Arial'})
    ax2.set_title('Performance Indicator Radar Chart Comparison', fontsize=14, fontweight='bold', fontname='Arial',
                  y=1.02)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"策略对比图已保存至: {save_path}")

    plt.show()


def save_comparison_results(all_experiment_results, output_dir="comparison_results"):
    """保存对比实验结果"""
    import os
    model_name = all_experiment_results[0]["model_name"] if all_experiment_results else "unknown_model"
    output_dir = os.path.join(output_dir, model_name)
    os.makedirs(output_dir, exist_ok=True)

    # 保存每个策略的详细结果
    for experiment in all_experiment_results:
        strategy_name = experiment["strategy_name"]
        strategy_dir = os.path.join(output_dir, strategy_name)
        os.makedirs(strategy_dir, exist_ok=True)

        # 保存提取结果
        results_path = os.path.join(strategy_dir, f"{strategy_name}_extraction_results.json")
        with open(results_path, 'w', encoding='utf-8') as f:
            json.dump(experiment["extraction_results"], f, ensure_ascii=False, indent=2)

        # 保存详细指标
        metrics_path = os.path.join(strategy_dir, f"{strategy_name}_metrics.csv")
        metrics_df = pd.DataFrame(experiment["metrics_data"])
        metrics_df.to_csv(metrics_path, index=False, encoding='utf-8-sig')

        # 保存提示词配置
        if strategy_name == "人工选择":
            prompt_components = MANUAL_PROMPT_COMPONENTS
        elif strategy_name == "GA优化":
            prompt_components = GA_OPTIMIZED_PROMPT_COMPONENTS
        else:
            prompt_components = experiment.get("prompt_components", {})

        prompt_path = os.path.join(strategy_dir, f"{strategy_name}_prompt_config.json")
        with open(prompt_path, 'w', encoding='utf-8') as f:
            json.dump(prompt_components, f, ensure_ascii=False, indent=2)

    # 保存总体对比结果
    comparison_summary = []
    for experiment in all_experiment_results:
        comparison_summary.append({
            "strategy": experiment["strategy_name"],
            "model": experiment["model_name"],
            "avg_f1_score": experiment["avg_f1"],
            "avg_precision": experiment["avg_precision"],
            "avg_recall": experiment["avg_recall"],
            "successful_extractions": experiment["valid_count"],
            "total_extractions": experiment["total_count"],
            "success_rate": experiment["valid_count"] / experiment["total_count"] if experiment[
                                                                                         "total_count"] > 0 else 0
        })

    summary_path = os.path.join(output_dir, "comparison_summary.csv")
    summary_df = pd.DataFrame(comparison_summary)
    summary_df.to_csv(summary_path, index=False, encoding='utf-8-sig')

    # 保存实验总结
    experiment_summary = {
        "experiment_type": "三种提示词策略对比",
        "model_used": model_name,
        "total_papers": all_experiment_results[0]["total_count"] if all_experiment_results else 0,
        "strategies_tested": [exp["strategy_name"] for exp in all_experiment_results],
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "results_summary": comparison_summary
    }

    summary_json_path = os.path.join(output_dir, "experiment_summary.json")
    with open(summary_json_path, 'w', encoding='utf-8') as f:
        json.dump(experiment_summary, f, ensure_ascii=False, indent=2)

    print(f"\n所有实验结果已保存至: {output_dir}")
    return output_dir


def print_detailed_comparison(all_experiment_results):
    """打印详细的对比分析"""
    model_name = all_experiment_results[0]["model_name"] if all_experiment_results else "Unknown"

    print("\n" + "=" * 80)
    print(f"三种提示词策略详细对比分析 - 模型: {model_name}")
    print("=" * 80)

    # 找出最佳策略
    best_f1_strategy = max(all_experiment_results, key=lambda x: x["avg_f1"])
    best_precision_strategy = max(all_experiment_results, key=lambda x: x["avg_precision"])
    best_recall_strategy = max(all_experiment_results, key=lambda x: x["avg_recall"])

    print(f"\n📊 性能排名:")
    print(f"  F1分数最高: {best_f1_strategy['strategy_name']} ({best_f1_strategy['avg_f1']:.4f})")
    print(f"  精确率最高: {best_precision_strategy['strategy_name']} ({best_precision_strategy['avg_precision']:.4f})")
    print(f"  召回率最高: {best_recall_strategy['strategy_name']} ({best_recall_strategy['avg_recall']:.4f})")

    print(f"\n📈 详细指标对比:")
    for experiment in all_experiment_results:
        print(f"\n  {experiment['strategy_name']}:")
        print(f"    F1分数: {experiment['avg_f1']:.4f}")
        print(f"    精确率: {experiment['avg_precision']:.4f}")
        print(f"    召回率: {experiment['avg_recall']:.4f}")
        print(
            f"    成功率: {experiment['valid_count']}/{experiment['total_count']} ({experiment['valid_count'] / experiment['total_count'] * 100:.1f}%)")

    # 计算相对提升
    manual_result = next((exp for exp in all_experiment_results if exp["strategy_name"] == "人工选择"), None)
    if manual_result:
        print(f"\n🚀 相对于人工选择的提升:")
        for experiment in all_experiment_results:
            if experiment["strategy_name"] != "人工选择":
                f1_improvement = experiment["avg_f1"] - manual_result["avg_f1"]
                precision_improvement = experiment["avg_precision"] - manual_result["avg_precision"]
                recall_improvement = experiment["avg_recall"] - manual_result["avg_recall"]

                print(f"\n  {experiment['strategy_name']}:")
                print(f"    F1分数提升: {f1_improvement:+.4f} ({f1_improvement / manual_result['avg_f1'] * 100:+.1f}%)")
                print(
                    f"    精确率提升: {precision_improvement:+.4f} ({precision_improvement / manual_result['avg_precision'] * 100:+.1f}%)")
                print(
                    f"    召回率提升: {recall_improvement:+.4f} ({recall_improvement / manual_result['avg_recall'] * 100:+.1f}%)")


def test_model_connection(model_name):
    """测试模型连接性"""
    try:
        extractor = CorrosionExtractor(model_name=model_name)
        print(f"✅ {model_name} 模型连接测试成功")
        return True
    except Exception as e:
        print(f"❌ {model_name} 模型连接测试失败: {e}")
        return False


def main():
    """主函数 - 三种提示词策略对比实验"""
    parser = argparse.ArgumentParser(description='腐蚀文献提取实验')
    parser.add_argument('--model', type=str, default='deepseek-chat',  # 默认使用 GPT-4
                        choices=SUPPORTED_MODELS,
                        help=f'选择使用的模型，支持: {", ".join(SUPPORTED_MODELS)}')
    parser.add_argument('--papers', type=int, default=30,  # 默认10篇，避免时间过长
                        help='处理的文献数量（默认: 10）')
    parser.add_argument('--test-only', action='store_true',
                        help='仅测试模型连接性，不运行完整实验')

    args = parser.parse_args()

    start_time = time.time()

    # 创建输出目录
    OUTPUT_DIR = "comparison_results"
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    try:
        print(f"🚀 开始三种提示词策略对比实验")
        print(f"📊 使用模型: {args.model}")

        # 测试模型连接性
        if not test_model_connection(args.model):
            print(f"❌ 模型 {args.model} 连接失败，请检查配置")
            return

        print(f"初始化腐蚀文献提取器，使用模型: {args.model}")
        extractor = CorrosionExtractor(model_name=args.model)
        print("✅ 腐蚀文献提取器初始化成功！")

        if not os.path.exists(PDF_FOLDER):
            print(f"错误: 文件夹 '{PDF_FOLDER}' 不存在")
            return

        print(f"从文件夹 '{PDF_FOLDER}' 加载PDF文献...")
        texts, filenames = load_pdfs_from_folder(PDF_FOLDER)

        if not texts:
            print("没有找到可处理的PDF文献")
            return

        print(f"✅ 成功提取 {len(texts)} 篇文献的文本内容")

        # 使用指定数量的文献进行实验
        test_count = min(args.papers, len(texts))
        test_texts = texts[:test_count]
        test_gold_standards = GOLD_STANDARDS[:test_count]
        test_filenames = filenames[:test_count]

        print(f"使用前 {test_count} 篇文献进行实验")

        # 如果只是测试连接性，就退出
        if args.test_only:
            print("✅ 模型连接测试完成")
            return

        # 定义三种实验策略
        experiment_strategies = [
            {
                "name": "人工选择",
                "components": MANUAL_PROMPT_COMPONENTS
            },
            {
                "name": "随机生成",
                "components": generate_random_prompt()
            },
            {
                "name": "GA优化",
                "components": GA_OPTIMIZED_PROMPT_COMPONENTS
            }
        ]

        # 运行所有三种策略的实验
        all_experiment_results = []

        for strategy in experiment_strategies:
            experiment_result = run_extraction_experiment(
                extractor, test_texts, test_gold_standards,
                strategy["components"], strategy["name"], test_filenames
            )
            experiment_result["prompt_components"] = strategy["components"]
            all_experiment_results.append(experiment_result)

        # 绘制对比结果
        comparison_plot_path = os.path.join(OUTPUT_DIR, f"{args.model}_strategy_comparison.png")
        plot_comparison_results(all_experiment_results, comparison_plot_path)

        # 保存所有结果
        save_comparison_results(all_experiment_results, OUTPUT_DIR)

        # 打印详细对比分析
        print_detailed_comparison(all_experiment_results)

        print(f"\n🎉 三种提示词策略对比实验完成！")
        print(f"📊 使用模型: {args.model}")
        print(f"📄 处理文献: {test_count} 篇")

    except Exception as e:
        print(f"程序执行出错: {e}")
        import traceback
        traceback.print_exc()

    finally:
        end_time = time.time()
        total_time = end_time - start_time
        print(f"\n总运行时间: {format_time(total_time)}")


if __name__ == "__main__":
    main()