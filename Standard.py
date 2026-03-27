# Standard.py - 黄金标准数据和配置

#黄金标准数据

GOLD_STANDARDS = [
    {   #1
        "Name of corrosion inhibitor": "Tikoua extract, Ficus extract, ZnO, CuO, Sodium lauryl sulfate (SLS)",
        "Corrosion Object Extraction": "carbon steel",
        "experimental environment": "0.5M H₂SO₄ media",
        "corrosion inhibition":"The inhibition efficiency reaches 53% at 1000 ppm plant extract concentration. By using 100 ppm ZnO Nanomaterial the inhibition efficiency reaches 87.43%",
        "test method": "Weight loss measurements, scanning electron microscope,atomic absorption spectroscopy"
    },
    {#2
        "Name of corrosion inhibitor": "Garcinia cambogia extract (GCE)",
        "Corrosion Object Extraction": "mild steel",
        "experimental environment": "1 M HCl, 0.5M H₂SO₄",
        "corrosion inhibition":"High inhibition efficiencies of 91.73 and 75.53% in 1 M HCl and 0.5 M H2SO₄",
        "test method": "Weight loss measurement，Electrochemical impedance spectroscopy (EIS)，Potentiodynamic polarisation (PDP)，Electrochemical noise measurements，Atomic force microscopy (AFM)，Quantum chemical calculations，FTIR spectroscopy"
    },
    {#3
        "Name of corrosion inhibitor": "triglycidyl-dibenzylidene-thiosemicarbazide (TGDBTSC)",
        "Corrosion Object Extraction": "mild steel",
        "experimental environment": "1 M HCl",
        "corrosion inhibition":"The maximum corrosion inhibition efficiency as determined by PDP was 93.2%, and 88.9% by EIS at a TGDBTSC concentration of 10-3M",
        "test method": "Potentiodynamic Polarization (PDP)、Electrochemical Impedance Spectroscopy (EIS)、Electrochemical Frequency Modulation (EFM)",
    },
    {#4
        "Name of corrosion inhibitor": "oak cupule (OC) biomass",
        "Corrosion Object Extraction": "mild steel",
        "experimental environment": "0.5 M HCl",
        "corrosion inhibition": "At 250 ppm, the inhibition efficiency reached 92.5 %",
        "test method": "electrochemical impedance spectroscopy, SEM, contact angle measurements, DFT, FTIR-ATR, mass spectrometry, UV-Vis spectroscopy"
    },
    {#5
        "Name of corrosion inhibitor": "carboxymethyl chitosan(CMCS)/L-lysine(Lys) composite",
        "Corrosion Object Extraction": "EH40 steel",
        "experimental environment": "seawater",
        "corrosion inhibition": "the ratio of CMCS to Lys is 3:2,the corrosion inhibition is 92.25 %",
        "test method": "Weight loss measurements, electrochemical tests and surface characterization"
    },
    {#6
        "Name of corrosion inhibitor": "synthesized NPSA and KI",
        "Corrosion Object Extraction": "Q235 steel",
        "experimental environment": "3.5 wt% NaCl",
        "corrosion inhibition": "in solution containing 0.8 mM NPSA and 5 mM KI,the inhibition efficiency for Q235 steel reached 83.3 %",
        "test method": "Electrochemical testing, Weight-loss experiment and X-ray photoelectron spectroscopy (XPS) testing"
    },
    {#7
        "Name of corrosion inhibitor": "thalidomide",
        "Corrosion Object Extraction": "mild steel",
        "experimental environment": "1 M HCl",
        "corrosion inhibition": "the  maximum inhibition efficiency of 98.71±0.02% at 1600 ppm",
        "test method": "gravimetric, electrochemical (PDP and EIS), surface characterization SEM–EDX, AFM, XPS, and quantum chemical (DFT)"
    },
    {#8
        "Name of corrosion inhibitor": "Black Cumin Cake Extract (BCCE)",
        "Corrosion Object Extraction": "Aluminum 5086",
        "experimental environment": " 1 M HCl",
        "corrosion inhibition": "the maximum inhibition efficiency is 99.57%",
        "test method": "weight loss (WL), Electrochemical Impedance Spectroscopy (EIS), and Potentiodynamic Polarization (PDP)"
    },
    {#9
        "Name of corrosion inhibitor": "Tinospora cordifolia fraction (TCF)",
        "Corrosion Object Extraction": "carbon steel",
        "experimental environment": "seawater medium",
        "corrosion inhibition": "90.89% (PDP) and 92.25% (EIS) with the addition of 150 mg.L−1 of TCF.",
        "test method":"electrochemical techniques and computational analyses"
    },
    {  # 10
        "Name of corrosion inhibitor": "Citrus limon peel essential oil (EO-A, EO-B, and EO-F)",
        "Corrosion Object Extraction": "mild steel",
        "experimental environment": "1 M HCL",
        "corrosion inhibition": "Inhibition efficiencies increased with increasing concentration, and reach a maximum of 81.45% (EO-A), 84.15% (EO-B), and 83.62% (EO-F), respectively. Different investigated inhibitors acted as mixed-type inhibitors by suppressing both anodic and cathodic reactions. ",
        "test method": "electrochemical impedance spectroscopy (EIS), potentiodynamic polarisation (PDP)"
    },
    {  # 11
        "Name of corrosion inhibitor": "1‑benzyloxynaphthalene",
        "Corrosion Object Extraction": "H13 steel",
        "experimental environment": "1 M HCl",
        "corrosion inhibition": "reaching a maximum of 91.40% at 2× 10–3 M. ",
        "test method": "Electrochemical Impedance Spectroscopy (EIS)"
    },
   {  # 12
       "Name of corrosion inhibitor": "benzylhydrazineyl imidazolone derivatives, ClPh-DDI and FPh-DDI",
       "Corrosion Object Extraction": "mild steel",
       "experimental environment": "1 M HCl",
       "corrosion inhibition": "inhibition efficiencies of 99.0 % and 99.2 % at 10− 4 M for ClPh-DDI and FPh-DDI",
       "test method": "electrochemical impedance spectroscopy and potentiodynamic polarization analyses"
   },
   {  # 13
       "Name of corrosion inhibitor": "alcohol/cobalt nanoparticle (Co-PVA) nanocomposite",
       "Corrosion Object Extraction": "soft-cast steel",
       "experimental environment": "1 M HCl",
       "corrosion inhibition": "maximum inhibition efficiency of 96.9 at 303 K",
       "test method": "weight loss measurements, electrochemical testing"
   },
   {  # 14
       "Name of corrosion inhibitor": "agro-waste cassava (Manihot esculenta) peels",
       "Corrosion Object Extraction": "AA6063",
       "experimental environment": "NaOH",
       "corrosion inhibition": "87.45% inhibition efficiency at 0.3 mL inhibitor dosage",
       "test method": "Electrochemical techniques, including potentiodynamic polarisation and open-circuit potential measurements"
   },
   {  # 15
       "Name of corrosion inhibitor": "olive leaf extract (OLE) and fig leaf extract (FLE)",
       "Corrosion Object Extraction": "copper",
       "experimental environment": "0.5 to 2 M HCL",
       "corrosion inhibition": "51% for FLE and 39% for OLE at 0.75 g/L in 1 M HCl,in 0.5 M HCl, FLE and OLE achieved maximum efficiencies of 69 % and 47 %,at 2 M HCl, the efficiencies dropped to 21% and 18% for FLE and OLE",
       "test method":"weight loss measurements,Surface analysis"
   },
    {  # 16
        "Name of corrosion inhibitor": "1,2,4-triazole (TAZ)",
        "Corrosion Object Extraction": "mild steel",
        "experimental environment": " 0.5 M H2SO4",
        "corrosion inhibition": "at high concentrations (300 mM), achieving maximum protection efficiency of 73% at 303 K.",
        "test method": "Weight Loss Method,Electrochemical Impedance Measurement,Surface Morphological Studies"
    },
   {  # 17
       "Name of corrosion inhibitor": "nano-SiO₂@3-mercaptopropyltrimethoxysilane (nano-SiO₂@MPTMS)",
       "Corrosion Object Extraction": "Q235 steel",
       "experimental environment": "3.5 wt% NaCl",
       "corrosion inhibition":"when 0.01 g of nano-SiO₂ was doped, with a corrosion inhibition efficiency of 99.90 %",
       "test method":"characterization methods and electrochemical tests"
   },
   {  # 18
       "Name of corrosion inhibitor": "Quaternium-15 (Q-15)",
       "Corrosion Object Extraction": "carbon steel",
       "experimental environment": "1 M HCL",
       "corrosion inhibition":"when 0.01 g of nano-SiO₂ was doped, with a corrosion inhibition efficiency of 99.90 %.",
       "test method":"electrochemical techniques,Surface characterization(force microscopy (AFM) and scanning electron microscopy (SEM))"
   },
   {  # 19
       "Name of corrosion inhibitor": "SCBS-I and SCBS-II",
       "Corrosion Object Extraction": "Q235 carbon steel",
       "experimental environment": "1 M HCL",
       "corrosion inhibition":" with a greater inhibition efficiency of 94.8 % at 250 mg/L",
       "test method":"Weight loss,Electrochemical measurements,Surface analysis"
   },
    {  # 20
        "Name of corrosion inhibitor": "coumarin–thiosemicarbazone (CT) hybrid",
        "Corrosion Object Extraction": "copper",
        "experimental environment": "hydrochloric acid(HCL)",
        "corrosion inhibition": "97.15 % under optimal conditions (40.10℃, 3.10 M HCl, 0.51 mM CT, 15.76 h immersion time)",
        "test method": "weight loss measurements,Electrochemical measurements,Surface analysis SEM and XPS"
    },
    {  # 21
        "Name of corrosion inhibitor": "Allium jesdianum extract (AEAJ)",
        "Corrosion Object Extraction": "mild steel",
        "experimental environment": "3.5 wt% NaCl",
        "corrosion inhibition": "inhibition performance of about 93.57 %",
        "test method": "electrochemical impedance spectroscopy (EIS), polarization measurements,surface characterization methods"
    },
    {  # 22
        "Name of corrosion inhibitor": "expired Butylphthalide (NBP) drugs",
        "Corrosion Object Extraction": "mild steel",
        "experimental environment": "acidic conditions(1 M hydrochloric acid)",
        "corrosion inhibition": "inhibition efficiency exceeding 94%",
        "test method": "weight loss method, electrochemical measurements, surface characterizations, and theoretical simulation calculations"
    },
    {  # 23
        "Name of corrosion inhibitor": "N-(1-dodecyl-1-H-1,2,3-triazol-4- ylmethyl)-N,N,N-triethylammonium bromide (C12TzTEA)",
        "Corrosion Object Extraction": "XC48 carbon steel",
        "experimental environment": "1M HCl",
        "corrosion inhibition": "with a maximum inhibition efficiency of 94.6% at 25℃",
        "test method": "weight loss measurements, potentiodynamic polarization (PDP), electrochemical impedance spectroscopy (EIS), scanning electron microscopy (SEM), energy dispersive X-ray spectroscopy (EDS), atomic force microscopy (AFM), density functional theory (DFT) and molecular dynamics (MD) simulations"
    },
    {  # 24
        "Name of corrosion inhibitor": "picolinoyl N4-phenylthiosemicarbazide (HL1 ), salicyloyl N4- phenylthiosemicarbazide (HL2), and anthraniloyl N4-phenylthiosemicarbazide (HL3)",
        "Corrosion Object Extraction": "zinc substratesl",
        "experimental environment": " 0.1 M NaCl",
        "corrosion inhibition": "HL1 significantly increased from 46.47% at 1.0 × 10–5 M to 97.22% at 1.0 × 10–3 M, while at the same concentration (1.0 × 10–3 M), HL3 provided the highest protection efficiency (98.59%), followed by HL2 (97.82%) and HL1",
        "test method": "polarization curves and electrochemical impedance spectroscopy (EIS)"
    },
    {  # 25
        "Name of corrosion inhibitor": "TRFE",
        "Corrosion Object Extraction": "carbon steel",
        "experimental environment": "1 M HCl",
        "corrosion inhibition": "TRFE achieved high inhibition efficiencies of 94.67 % at 298 K, 96.15 % at 308 K, and 95.63 % at 318 K, at a concentration of 400 mg L−1",
        "test method": "lectrochemical measurements, surface analysis, quantum chemical calculations, and molecular dynamics simulations"
    },
    {  # 26
        "Name of corrosion inhibitor": "dodecyl dimethyl betaine (BS-12)",
        "Corrosion Object Extraction": "cold rolled steel (CRS) ",
        "experimental environment": "1.0 M H3PO4",
        "corrosion inhibition": "corrosion inhibition efficiency of 90.3 % at a concentration of 100 mg L−1 at 50℃",
        "test method": "weight loss method,Electrochemical testing"
    },
    {  # 27
        "Name of corrosion inhibitor": "3-ethyl-2-styrylbenzo[d]thiazol-3-ium iodide ([ESBT]I)",
        "Corrosion Object Extraction": "mild steel",
        "experimental environment": "1M HCl",
        "corrosion inhibition":"Weight loss: 97.8% at 0.05 mM, 98.55% at 0.25 mM; Tafel: 94.4% at 0.05 mM, 97.5% at 0.25 mM; EIS: 94.64% at 0.05 mM, 96.07% at 0.25 mM; Stability: 80.31% after 720h immersion",
        "test method": "weight loss experiments, Tafel plots and electrochemical impedance spectroscopy (EIS)"
    },
    {  # 28
        "Name of corrosion inhibitor": "3-(5-methyl-3-oxo-2,3-dihydro-1H-pyrazol-4-yl)-3-phenylpropanoic acid (C4-PRZ-1)",
        "Corrosion Object Extraction": "mild steel(MS)",
        "experimental environment": "1 M HCl",
        "corrosion inhibition": "with a maximum efficiency of 85% observed at 5.0 mM",
        "test method": "weight loss experiments, Tafel plots and electrochemical impedance spectroscopy (EIS)"
    },
    {  # 29
        "Name of corrosion inhibitor": "green Cu nanocomplex (Cu2L2)",
        "Corrosion Object Extraction": "316 L stainless steel",
        "experimental environment": "1 M HCl,1 M HNO3",
        "corrosion inhibition": "with a maximum efficiency of 85.56% achieved at 600 ppm addition",
        "test method": "open-circuit potential (OCP), impedance spectroscopy (EIS), potentiodynamic polarization (PDP), and SEM/EDX methods"
    },
{  # 30
        "Name of corrosion inhibitor": "Okoubaka seed extract (OSE)",
        "Corrosion Object Extraction": "1 M HCl",
        "experimental environment": "1 M HCl+1 M HNO3",
        "corrosion inhibition": " at a concentration of 2.5 g/L, yielding a percentage inhibitory efficacy (IE%) above 90.0%",
        "test method": "weight loss, electrochemical impedance spectroscopy (EIS), and potentiodynamic polarization (PDP)"
    }
]

# 基因定义
GENE_DEFINITIONS = {
    "role_context": [  # Role Definition
        # Direct extraction style - Tool role
        "You are a corrosion literature extraction tool. Strictly extract information in specified format: inhibitor name, concentration, corrosion solution, performance, test methods.",
        # Task description style - Expert role
        "As a professional analyst in corrosion science, systematically analyze experimental data from literature. Your task is to accurately extract core parameters of corrosion inhibitor research, ensuring information completeness and accuracy.",
        # Element combination style - Structured role
        "You are a structured information extraction expert. Decompose literature content into five core dimensions: material, concentration, solution, performance, method, and combine output according to standard template.",
        # Result-oriented style - Application role
        "Your goal is to build standardized data entries for corrosion research database. Extract complete experimental information from literature that can be directly used for data analysis and model building."
    ],

    "material_extraction": [  # Corrosion Inhibitor Name Extraction
        # Direct extraction style - Precise name extraction
        "Extract corrosion inhibitor names.e.g., 'green tea extract', 'imidazoline derivative'.",
        # Task description style - Systematic material identification
        "Systematically identify corrosion inhibitor materials used in the text, including plant extracts, chemical compounds, composite materials, and all types of inhibitor names.",
        # Element combination style - Name element decomposition
        "Identify and extract the key information: the specific names of corrosion inhibitor substances as explicitly mentioned in the text.",
        # Result-oriented style - Material identification oriented
        "To build a corrosion inhibitor material library, extract all corrosion inhibitor names."
    ],

    "corrosion_object_extraction": [  # Corrosion Object Extraction
        # Direct extraction style - Precise object extraction
        "Extract corrosion object names. Format: 'object name', e.g., 'carbon steel', 'stainless steel', 'copper', 'aluminum'.",
        # Task description style - Systematic object identification
        "Systematically identify the material objects protected by the corrosion inhibitor in the experiment like carbon steel, stainless steel, copper, aluminum, and their specific grades.",
        # Element combination style - Object element decomposition
        "Corrosion object identification consists of material type and specific grade. Extract both the base material and any specified grade information.",
        # Result-oriented style - Material protection oriented
        "To understand the application scope of corrosion inhibitors, extract all corrosion object names. These indicate which materials are being protected in the study."
    ],

    "corrosion_solution_extraction": [  # Corrosion Solution Extraction
        # Direct extraction style - Precise medium and concentration extraction
        "Extract corrosion medium type and concentration. Format: 'concentration medium', e.g., '0.5M H₂SO₄', '1 M HCl', '3.5% NaCl'.",
        # Task description style - Systematic medium and concentration extraction
        "Identify the medium type and its concentration used in corrosion experiments. Focus on chemical names of corrosion media and precise concentration values.",
        # Element combination style - Medium and concentration element decomposition
        "Corrosion solution core information contains two elements: 1) medium type (HCl/H₂SO₄/NaCl, etc.) 2) medium concentration (0.5M/1M/3.5%, etc.). Extract and combine these two elements.",
        # Result-oriented style - Solution formulation oriented
        "To determine the basic formulation of corrosion solution, extract medium type and concentration information. Include chemical names of basic corrosion media and corresponding concentrations."
    ],

    "performance_extraction": [  # Corrosion Inhibition Performance Extraction
        # Direct extraction style - Complete performance expression extraction
        "Extract complete corrosion inhibition performance description. Pay attention to the complete association between inhibition efficiency, corrosion inhibitor, and corrosion medium.",
        # Task description style - Systematic performance condition recording
        "Systematically record complete performance data of corrosion inhibitors. Include: inhibition efficiency values, corresponding corrosion inhibitor concentrations, and test corrosion media used.",
        # Element combination style - Performance condition element combination
        "Complete corrosion inhibition performance contains three core elements: 1) efficiency value (percentage) 2) corrosion inhibitor concentration 3) corrosion medium. Combine these elements to form complete performance condition description.",
        # Result-oriented style - Performance comparison analysis oriented
        "For horizontal comparison analysis of corrosion inhibitor performance, extract performance data containing complete experimental conditions. Require simultaneous inclusion of efficiency values, usage concentrations, and corrosion media."
    ],

    "numerical_emphasis": [  # Test Method Extraction
        # Direct extraction style - Precise method name listing
        "Extract test method names. Format: 'method1, method2, method3', e.g., 'weight loss, EIS, polarization'. Separate with commas, list only method names.",
        # Task description style - Systematic method system identification
        "Identify experimental methods used to evaluate corrosion inhibition performance in the text. Include corrosion rate measurement methods, surface analysis techniques, electrochemical test methods, etc.",
        # Element combination style - Method type combination
        "Test methods can be classified by measurement principle. Extract test method names used in the text.",
        # Result-oriented style - Method applicability oriented
        "To evaluate the applicability of test methods, extract all experimental methods used for corrosion inhibition performance evaluation."
    ],

    "temperature": [0.1, 0.1, 0.1, 0.1]  # Temperature parameters[1.0, 1.0, 1.0, 1.0]
}


# GOLD_STANDARDS = [
#     {   #1
#         "Name of corrosion inhibitor": "PESA-grafted-PAM (PESAPAM)",
#         "Corrosion Object Extraction": "carbon steel",
#         "experimental environment": "1.0 M HC",
#         "corrosion inhibition":"inhibition efficiency (IE) reaching 90% at 500 mg·L−1 at 25 °C",
#         "test method": "Electrochemical, kinetics, and surface microscopic studies"
#     },
#     {#2
#         "Name of corrosion inhibitor": "Carbonic anhydrase (CA)",
#         "Corrosion Object Extraction": "Concrete",
#         "experimental environment": "5 wt % NaCl",
#         "corrosion inhibition":"reducing rebar corrosion depth to 109 μm�34% lower than the control",
#         "test method": "accelerated corrosion test, Faraday’s law analysis, thermogravimetric analysis (TGA), mercury intrusion porosimetry (MIP)"
#     },
#     {#3
#         "Name of corrosion inhibitor": "Dextran",
#         "Corrosion Object Extraction": "St37−2 steel",
#         "experimental environment": "15% H₂SO₄",
#         "corrosion inhibition":"Dextran with molecular weight of 100000−200000 g/mol (Dex 1) exhibited the highest inhibition efficiency of 51.38% at 25 °C",
#         "test method": "weight loss, electrochemical(EIS,EFM,PDP,LPR,SEM,EDAX,AFM,XPS)",
#     },
#     {#4
#         "Name of corrosion inhibitor": "ethanedihydrazide (EH)",
#         "Corrosion Object Extraction": "iron",
#         "experimental environment": "3.5% NaCl",
#         "corrosion inhibition": "The presence of 5 × 10−5 M EH was found to inhibit the corrosion of iron, and the eﬀect of inhibition profoundly increased with an increase in EH concentration up to 1 × 10−4 M and further to 5 × 10−4 M",
#         "test method": "EIS, CPP, SEM, EDX"
#     },
#     {#5
#         "Name of corrosion inhibitor": "Ketosulfone",
#         "Corrosion Object Extraction": "mild steel",
#         "experimental environment": "1 M HCl",
#         "corrosion inhibition": "Inhibition efficiency increases with an increase in concentration of Ketosulfone and with increase in temperature up to 313 K.",
#         "test method": "Weight Loss Measurements,Electrochemical Measurements,Quantum Chemical Studies,Adsorption Isotherm and Thermodynamic Pa-rameters,Scanning Electron Microscopic (SEM) Studies."
#     },
#     {#6
#         "Name of corrosion inhibitor": "carboxymethyl chitosan (CMCS) and sodium humate (SH)",
#         "Corrosion Object Extraction": "EH40 steel",
#         "experimental environment": "seawater",
#         "corrosion inhibition": "When the CMCS mass concentration reaches 100 mg/L and the SH mass concentration reaches 50 mg/L, the corrosion inhibition rate is 74.65%, the corrosion potential shifts by about 47.39 mV, the Rp value increases from 358.6 to 1102.4 Ω·cm2, and the Ydl value decreases from 177.31 Sn Ω−1cm−2 × 10−6 to 92.672 Sn Ω−1cm−2 × 10−6.",
#         "test method": "Corrosion Weight Loss Experiment,Electrochemical Experiment,XPS Analysis,SEM-EDS Analysis"
#     },
#     {#7
#         "Name of corrosion inhibitor": "Caesalpinia spinosa extract (Tara-SE, Tara-ME)",
#         "Corrosion Object Extraction": "mild steel",
#         "experimental environment": "0.1 M HNO3",
#         "corrosion inhibition": "Values of IE ranging from 90.73 to 97.38% for Tara-1000-SE and from 85.3 to 96.05% for Tara-1000-ME were obtained by WL, PP, and EIS experiments.",
#         "test method": "Values of IE ranging from 90.73 to 97.38% for Tara-1000-SE and from 85.3 to 96.05% for Tara-1000-ME were obtained by WL, PP, and EIS experiments"
#     },
#     {#8
#         "Name of corrosion inhibitor": "New Chalcone Oxime Functionalized Graphene Oxide",
#         "Corrosion Object Extraction": "carbon steel",
#         "experimental environment": " 1 M HCl",
#         "corrosion inhibition": "CO-GO has an outstanding corrosion inhibitor performance of up to 94%.",
#         "test method": "spectroscopy (FTIR), X-ray diffraction (XRD), thermal gravimetric analysis (TGA), and scanning electron microscopy (SEM)"
#     },
#     {#9
#         "Name of corrosion inhibitor": "pumpkin leaf extract",
#         "Corrosion Object Extraction": "copper",
#         "experimental environment": "0.5 M H2SO4",
#         "corrosion inhibition": "The corrosion inhibition efficiency of the PLE against copper reached 89.98% when the concentration of the PLE reached 800 mg/L. Furthermore, when the temperature and soaking time increased, the corrosion protection efficiency of 800 mg/L PLE on copper consistently remained above 85%.",
#         "test method":"Fourier infrared spectroscopy, electrochemical testing, XPS, AFM, and SEM"
#     },
#     {  # 10
#         "Name of corrosion inhibitor": "Cyproconazole (CPA)",
#         "Corrosion Object Extraction": "copper",
#         "experimental environment": "0.5 M H2SO4",
#         "corrosion inhibition": "the inhibition efficiency reaches 89.3%, 91.3%, 94.1%, and 85.6% at 288, 293, 298, and 303 K, respectively.",
#         "test method": "electrochemical impedance spectroscopy (EIS), potentiodynamic polarization, and scanning electron microscopy (SEM)"
#     },
#     {  # 11
#         "Name of corrosion inhibitor": "Biomass-Derived High-Yield Carbon Quantum Dots",
#         "Corrosion Object Extraction": "Q235 Carbon Steel",
#         "experimental environment": "1 M HCl",
#         "corrosion inhibition": "the corrosion inhibition efficiency reached 95.98% at 200 mg/L",
#         "test method": "weight loss, electrochemical test, surface analysis, and adsorption thermodynamic analyses"
#     },
#    {  # 12
#        "Name of corrosion inhibitor": "[BsMIM][HSO4], [BsMIM][BF4]",
#        "Corrosion Object Extraction": "304 Stainless Steel",
#        "experimental environment": "1.0 M sulfuric acid",
#        "corrosion inhibition": "inhibition efficiencies of 99.0 % and 99.2 % at 10− 4 M for ClPh-DDI and FPh-DDI",
#        "test method": "Electrochemical Tests,Surface Analysis,EIS Study"
#    },
#    {  # 13
#        "Name of corrosion inhibitor": "2-(8-heptadecenyl)-2-imidazoline-1-ethanamin (S-Imd)",
#        "Corrosion Object Extraction": "Carbon Steel Pipelines",
#        "experimental environment": "CO₂-saturated environment",
#        "corrosion inhibition": "the corrosion rate increased following the der of [BsMIM][BF4] < [BsMIM][HSO4] < 98% H2SO4",
#        "test method": "weight loss and electrochemical measurements, such as the electrochemical impedance spectrum (EIS), potentiodynamic polarization (PDP), and linear polarization resistance (LPR),"
#    },
#    {  # 14
#        "Name of corrosion inhibitor": "[C16DMIM]+[PF6]−",
#        "Corrosion Object Extraction": "carbon steel",
#        "experimental environment": "1 M HCl and 1 M H2SO4",
#        "corrosion inhibition": "the addition of 0.05 mmol/L [C16DMIM]+[PF6]− resulted in an inhibition efficiency of 98.28% and 80.10% in 1 M HCl and 1 MH2SO4 at 363 K",
#        "test method": "weight loss and electrochemical measurements"
#    },
#    {  # 15
#        "Name of corrosion inhibitor": "oarabinogalactan (AG)",
#        "Corrosion Object Extraction": "carbon steel",
#        "experimental environment": "1 M HCl",
#        "corrosion inhibition": "The inhibition efficiency is both concentration- and temperature-reliant and reaches as high as 96.3%",
#        "test method":"Gravimetric method, potentiodynamic polarization measurements, electrochemical impedance spectroscopy"
#    },
#     {  # 16
#         "Name of corrosion inhibitor": "Schinopsis lorentzii extract",
#         "Corrosion Object Extraction": "low carbon steel",
#         "experimental environment": "1 M HCl",
#         "corrosion inhibition": "Schinopsis lorentzii extract acted as slightly cathodic inhibitor and inhibition efficiencies increased with the increase of extract concentration",
#         "test method": "Tafel extrapolation, linear polarization, and electrochemical impedance spectroscopy (EIS)"
#     },
#    {  # 17
#        "Name of corrosion inhibitor": "copper-added water extracts from cigarette butts (CBWECI)",
#        "Corrosion Object Extraction": "N80 steel",
#        "experimental environment": "15% HCl",
#        "corrosion inhibition":"tthe inhibition efficiency ofwater extracts from cigarette butts in the presence ofCuCl is higher than in absence ofCuCl, and it can reach 95.3% when 9% water extracts with copper added is used",
#        "test method":"weight loss, electrochemical noise, polarization, impedance, and X-ray photoelectron spectroscopy"
#    },
#    {  # 18
#        "Name of corrosion inhibitor": "Purpald (4-amino-3-hydrazino-5-mercapto-1,2,4-triazole, AHMT)",
#        "Corrosion Object Extraction": "copper",
#        "experimental environment": "2 M HNO₃",
#        "corrosion inhibition":"inhibition efficiency attains 94.7% at 10−2 M",
#        "test method":"weight loss, ac impedance, and dc polarization techniques"
#    },
#    {  # 19
#        "Name of corrosion inhibitor": "sulfonated zinc phthalocyanine (Zn-Pc)",
#        "Corrosion Object Extraction": "copper",
#        "experimental environment": "3.5% NaCl",
#        "corrosion inhibition":" demonstrates an impressive 97% inhibition efficiency",
#        "test method":"electrochemically characterized,potentiodynamic polarization,X-ray analysis"
#    },
#     {  # 20
#         "Name of corrosion inhibitor": "L-cysteine-grafted graphene oxide (Cys-GO)",
#         "Corrosion Object Extraction": "Q235 steel",
#         "experimental environment": "1M HCl",
#         "corrosion inhibition": "The optimum concentration of Cys-GO was 15 mg L−1, and the according η value was up to 90%.",
#         "test method": "electrochemical methods,"
# },
#     {  # 21
#         "Name of corrosion inhibitor": "carbon quantum dots from acerola seeds",
#         "Corrosion Object Extraction": "mild steel",
#         "experimental environment": "1M HCl",
#         "corrosion inhibition": "achieving corrosion inhibition efficiencies of 87 % at 300 ppm after 2 h, and 94 % at 200 ppm after 24 h",
#         "test method": "transmission electron microscopy, dynamic light scattering, fluorimetry, Fourier transform infrared spectroscopy, UV–Vis, and X-ray photoelectron spectroscopy"
#     },
#     {  # 22
#         "Name of corrosion inhibitor": "Potency of ethanolic extracts of Lagenaria breviflora leaf",
#         "Corrosion Object Extraction": "mild steel",
#         "experimental environment": "0.5M HCl",
#         "corrosion inhibition": "This resulted in a protection efficiency of 87.0% in the presence of LELB inhibitor by the electrochemical method",
#         "test method": "Phytochemical analysis, FTIR, thermodynamic, Kinetic, weight loss, and electrochemical studies"
#     },
#     {  # 23
#         "Name of corrosion inhibitor": "sodium lauryl diphenyl ether disulfonate (SLDED) and Na₂B₄O₇",
#         "Corrosion Object Extraction": "AZ91D magnesium alloy",
#         "experimental environment": "3.5 wt% NaCl",
#         "corrosion inhibition": "When the concentrations of both SLDED and Na₂B₄O₇ were 5 g/L, the corrosion inhibition efficiency reached 87.50 %",
#         "test method": "electrochemical experiments, surface characterization techniques, and theoretical calculations"
#     },
#     {  # 24
#         "Name of corrosion inhibitor": "Baccaurea ramiflora leaf extract",
#         "Corrosion Object Extraction": "carbon steel",
#         "experimental environment": "1 N HCl",
#         "corrosion inhibition": "achieving a maximum inhibition effectiveness of 96.40%",
#         "test method": "Potentiodynamic polarization and Electrochemical Impedance Spectroscopy (EIS)"
#     },
#     {  # 25
#         "Name of corrosion inhibitor": "Rosa Damascena extract (RDE)",
#         "Corrosion Object Extraction": "carbon steel",
#         "experimental environment": "hydrochloric acid environments",
#         "corrosion inhibition": "Potentiodynamic polarization experiments showed an inhibition efficiency of 94.8%",
#         "test method": "potentiodynamic polarization, electrochemical impedance spectroscopy (EIS), scanning electron microscopy (SEM), and quantum chemical calculations"
#     },
#     {  # 26
#         "Name of corrosion inhibitor": "tetraglycidyldiphenylcarbazide (TGDPC)",
#         "Corrosion Object Extraction": "mild steel",
#         "experimental environment": "1M HCl",
#         "corrosion inhibition": "The highest protection efficiency was 95.5% as measured by potentiodynamic polarization (PDP) and 92.27% by electrochemical impedance spectroscopy (EIS) at a concentration of 10−3 M",
#         "test method": "electrochemical, surface, and computational analyses"
#     },
#     {  # 27
#         "Name of corrosion inhibitor": "N/S(CDs)",
#         "Corrosion Object Extraction": "AZ31 Mg alloy",
#         "experimental environment": "3.5 wt% NaCl",
#         "corrosion inhibition":"with the highest performance observed at 200 mg/L N/S(CDs), where the inhibition rate reached approximately 81%",
#         "test method": "TEM, FTIR, UV–Vis,Electrochemical tests"
#     },
#     {  # 28
#         "Name of corrosion inhibitor": "1-hydroxybenzotriazole (BTAOH)",
#         "Corrosion Object Extraction": "copper",
#         "experimental environment": "acidic copper ion solution",
#         "corrosion inhibition": "the corrosion inhibitor significantly reduced the corrosion rate of the etching solution. When the BTAOH concentration reached 0.004 mol  L−1, the inhibition efficiency increased to 24.60%",
#         "test method": "scanning electron microscopy (SEM), atomic force microscopy (AFM), electron backscatter diffraction (EBSD), focused ion beam (FIB), and energy-dispersive spectroscopy (EDS),Potentiodynamic polarization and electrochemical impedance spectroscopy (EIS)"
#     },
#     {  # 29
#         "Name of corrosion inhibitor": "Vanillin",
#         "Corrosion Object Extraction": "aluminum",
#         "experimental environment": "0.5 M H2SO4",
#         "corrosion inhibition": "PDP curves showed that at 25 °C, the Icorr reached 82% efficiency at 2 mM. At elevated temperatures of 40 and 60 °C, efficiencies of 77% and 75% were reached at 4 mM and 10 mM, respectively",
#         "test method": "SEM analysis,electrochemical characterization,weight loss analyses,EDS analyses"
#     },
# {  # 30
#         "Name of corrosion inhibitor": "OCMP-4, OCMP-3, NCMP-4, NCMP-3",
#         "Corrosion Object Extraction": "N80 carbon steel",
#         "experimental environment": "15% HCl",
#         "corrosion inhibition": "Electrochemical impedance spectroscopy revealed strong adsorption of NCMP-3 on the steel surface, achieving over 90% inhibition efficiency",
#         "test method": "Surface analysis, computational methods, weight loss measurements, and electrochemical techniques"
#     }
# ]


# #MDPI20
# GOLD_STANDARDS = [
#     {   #1
#         "Name of corrosion inhibitor": "collagen–BMIM·Br composite",
#         "Corrosion Object Extraction": "mild steel",
#         "experimental environment": "1.5 M HCl",
#         "corrosion inhibition":"Gravimetric analysis demonstrated exceptional inhibition efficiency (>95%) across a temperature range of 30–60 °C",
#         "test method": "FTIR and XRD analyses,Density Functional Theory (DFT),Weight Loss Analysis"
#     },
#     {#2
#         "Name of corrosion inhibitor": "locust bean gum",
#         "Corrosion Object Extraction": "N80 carbon steel",
#         "experimental environment": "CO2-saturated 2 wt.% KCl solution",
#         "corrosion inhibition":"reaching maximum inhibition efficiency of 84.11% at 25 ◦C and 55.81% at 80 ℃",
#         "test method": "weight loss, electrochemical measurements,Potentiodynamic tests,Potentiodynamic tests"
#     },
#     {#3
#         "Name of corrosion inhibitor": "Allium sativum extract",
#         "Corrosion Object Extraction": "copper matrix composites",
#         "experimental environment": "3.5 wt.% NaCl",
#         "corrosion inhibition":"the maximal inhibitor concentration of 92% was reached at 5 mL",
#         "test method": "electrochemical techniques, including OCPT, Tafel polarization, EIS, LSV, and chronocoulometry",
#     },
#     {#4
#         "Name of corrosion inhibitor": "thiocolchicoside (TCC)",
#         "Corrosion Object Extraction": "Ti6Al4V alloy",
#         "experimental environment": "saline solution (SS)",
#         "corrosion inhibition": "the inhibitory efficacy improved with higher TCC concentrations (achieving 92.40% at 200 mg/L of TCC) and diminished with an increase in solution temperature",
#         "test method": "potentiodynamic polarization curves (PPCs), open-circuit potential (OCP), and electrochemical impedance spectroscopy (EIS) methodologies, supplemented by scanning electron microscopy (SEM), energy-dispersive X-ray (EDS) analysis, atomic force microscopy (AFM), and contact angle (CA) measurements"
#     },
#     {#5
#         "Name of corrosion inhibitor": "CATA",
#         "Corrosion Object Extraction": "mild steel",
#         "experimental environment": "2M HCl, 100°C",
#         "corrosion inhibition": "Under the most aggressive experimental conditions (2 M HCl, 100 ◦C), the addition of 10 mM CATA achieved an inhibition efficiency of 99.6%, with a corrosion rate of 3.3 g m−2 h−1",
#         "test method": "Vacuum Extraction Method,Cyclic Bending Tests,Voltammetry,Electrochemical Impedance Spectroscopy (EIS),Electrochemical Impedance Spectroscopy (EIS),AFM Method,XPS Method,Mass Spectrometry,Molecular Dynamics Simulations"
#     },
#     {#6
#         "Name of corrosion inhibitor": "ZnO nanoparticles",
#         "Corrosion Object Extraction": "iron",
#         "experimental environment": "seawater with sulphate-reducing bacteria (SRB)",
#         "corrosion inhibition": "the corrosion rate increased by 21.3% in the presence of SRB compared to the control, whereas the ZnO-added electrode showed a 21.7% reduction in corrosion rate relative to the control.",
#         "test method": "cyclic voltammetry (CV), scanning electron microscopy (SEM), energy-dispersive X-ray spectroscopy (EDX), mass loss, and pH measurements"
#     },
#     {#7
#         "Name of corrosion inhibitor": "[2-(thiophen-2-yl)-1-(thiophen-2-ylmethyl)-1H-benzo[d]imidazole] and its Zn and Cu complexes",
#         "Corrosion Object Extraction": "mild steel",
#         "experimental environment": "1.0 M HCl",
#         "corrosion inhibition": "a significant decrease in corrosion current density and increased polarization resistance, with the Zn complex achieving the highest inhibition efficiency (93.8%)",
#         "test method": "EIS, PDP, LPR, CASP,SEM and EDS"
#     },
#     {#8
#         "Name of corrosion inhibitor": "xanthan gum",
#         "Corrosion Object Extraction": "N80 carbon steel",
#         "experimental environment": "saline CO2-saturated solution",
#         "corrosion inhibition": "inhibition efficiencies of 70.10% at 30 ◦C and 61.41% at 90 ◦C using 1.0 g L−1 of XG, after 24 h",
#         "test method": "weight loss and conducting electrochemical assessments"
#     },
#     {#9
#         "Name of corrosion inhibitor": "Artemisia annua L. extract",
#         "Corrosion Object Extraction": "304 stainless steel",
#         "experimental environment": "simulated seawater (ASWB), biotic medium with Pseudomonas aeruginosa",
#         "corrosion inhibition": "A. annua extract demonstrated a 74.4 ± 4.4% reduction in MIC-induced corrosion of 304 SS in marine conditions",
#         "test method":"electrochemical, surface, and spectroscopic techniques"
#     },
#     {  # 10
#         "Name of corrosion inhibitor": "Benzotriazole (BTA), 8-hydroxyquinoline (8HQ)",
#         "Corrosion Object Extraction": "mild steel",
#         "experimental environment": "simulated marine environment",
#         "corrosion inhibition": "with a 50% improvement in corrosion resistance of steel exposed within the scratch",
#         "test method": "electrochemical impedance spectroscopy (EIS),scanning electron microscopy (SEM),Energy dispersive X-Ray spectrometer (EDS)"
#     },
#     {  # 11
#         "Name of corrosion inhibitor": "tea tree essential oil, expired Sinecod",
#         "Corrosion Object Extraction": "carbon steel",
#         "experimental environment": "5M HCl",
#         "corrosion inhibition": "The optimum concentration proved to be 4% for both substances, with inhibition efficiencies up to 90% in the case of tea tree essential oil and up to 60% in the case of expired Sinecod",
#         "test method": "weight loss method, potentiodynamic polarization, electrochemical impedance spectroscopy"
#     },
#    {  # 12
#        "Name of corrosion inhibitor": "SiO2 superhydrophobic coating",
#        "Corrosion Object Extraction": "Al7075",
#        "experimental environment": "NaCl and H2SO4 at 3.5 wt.%",
#        "corrosion inhibition": "the coating presented an efficiency of 81% when exposed to NaCl",
#        "test method": "cyclic potentiodynamic polarization (CPP),electrochemical impedance spectroscopy (EIS),"
#    },
#    {  # 13
#        "Name of corrosion inhibitor": "Caffeic acid (CA)",
#        "Corrosion Object Extraction": "Zn",
#        "experimental environment": "0.1M NaCl",
#        "corrosion inhibition": "The highest inhibition efficiency was achieved for CA coating obtained from ethanol solution of CA (10 mM), and its value was almost 95%",
#        "test method": "electrochemical methods,SEM-EDS,XRD,TOF-SIMS,PDP,EIS"
#    },
#    {  # 14
#        "Name of corrosion inhibitor": "biosurfactant produced by Pseudomonas cepacia CCT 6659",
#        "Corrosion Object Extraction": "carbon steel",
#        "experimental environment": "seawater",
#        "corrosion inhibition": "The biosurfactant formulated in a 1:5 (v/v) ratio reduced the mass loss of test specimens (119.72±2.64 g/m²) by no less than 57.3% compared to the control (280.28±4.58 g/m²). Under dynamic conditions, the 1:2 (v/v) formulation showed greater protection, being able to reduce specimen corrosion (578.87±7.01 g/m²) by 69.6% compared to the control (1901.41±13.53 g/m²).",
#        "test method": "weight loss, SEM/EDS",
#    },
#    {  # 15
#        "Name of corrosion inhibitor": "KEDG peptide (H-Lys-Glu-Asp-Gly-OH)",
#        "Corrosion Object Extraction": "copper",
#        "experimental environment": "sodium chloride solution",
#        "corrosion inhibition": "achieved an inhibition efficiency of around 86% calculated from electrochemical measurements",
#        "test method":"electrochemical measurements,SEM/EDS analysis"
#    },
#     {  # 16
#         "Name of corrosion inhibitor": "Phalaris canariensis extract",
#         "Corrosion Object Extraction": "brass",
#         "experimental environment": "CO2-saturated 3.5% NaCl solution",
#         "corrosion inhibition": "reaching its maximum value of 99% with an inhibitor concentration of 100 ppm, decreasing the corrosion current density by more than two orders of magnitude",
#         "test method": "potentiodynamic polarization curves and electrochemical impedance spectroscopy tests"
#     },
#    {  # 17
#        "Name of corrosion inhibitor": "Benzoxazole-2-thione",
#        "Corrosion Object Extraction": "C38 steel",
#        "experimental environment": "1 M HCl",
#        "corrosion inhibition":"The results indicate that the benzoxazole-2-thione significantly reduces the corrosion rate, achieving a maximum inhibition efficiency of 95.25% at a concentration of 10−4 M",
#        "test method":"Tafel polarization and electrochemical impedance spectroscopy"
#    },
#    {  # 18
#        "Name of corrosion inhibitor": "4-Nitrobenzaldehyde (BA2)",
#        "Corrosion Object Extraction": "mild steel",
#        "experimental environment": "1M HCl",
#        "corrosion inhibition":"Benzaldehyde derivative (BA-2) showed a maximum inhibition efficiency of 93.3% at 500 ppm",
#        "test method":"PDP,EIS,FTIR,DFT,UV-Vis "
#    },
#    {  # 19
#        "Name of corrosion inhibitor": "TETA",
#        "Corrosion Object Extraction": "AZ31 magnesium alloy",
#        "experimental environment": "simulated seawater",
#        "corrosion inhibition":"at the optimal concentration (47 mM), after 24 h of immersion, the maximum |Z|0.01 Hz reached 7.56 × 105 Ω·cm2—three orders of magnitude higher than pure Li–Al LDH coated AZ31 (2.55 × 102 Ω·cm2).",
#        "test method":"Electrochemical tests, SEM, FT-IR, XPS, and 3D depth-of-field microscopy"
#    },
#     {  # 20
#         "Name of corrosion inhibitor": "6-diallylamino-1,3,5-triazine-2,4-dithiol monosodium (DAN), 6-dibutylamino-1,3,5-triazine-2,4-dithiol monosodium (DBN)",
#         "Corrosion Object Extraction": "aluminum alloy (AA5052)",
#         "experimental environment": "1 M HCl",
#         "corrosion inhibition": "The inhibition efficiency of both DAN and DBN improved with increases in inhibitor concentration but decreased with increases in temperature.",
#         "test method": "weight loss methods, electrochemical measurements, and scanning electron microscopy (SEM) techniques"
# }
# ]


# #wiley
# GOLD_STANDARDS = [
#     {   #1
#         "Name of corrosion inhibitor": "fatty amidine",
#         "Corrosion Object Extraction": "copper",
#         "experimental environment": "3.0 wt.% NaCl",
#         "corrosion inhibition":"the optimum inhibition efficiency of96% was achieved using only 0.2mM stearamidine",
#         "test method": "electrochemical (potentiodynamic polarization) and morphological (scanning electron microscopy) measurements"
#     },
#     {#2
#         "Name of corrosion inhibitor": "alkaloid",
#         "Corrosion Object Extraction": "N-80, S13Cr",
#         "experimental environment": "HCl solutions ranging from 15-28 wt.% at temperatures between 25-121°C for 6 h",
#         "corrosion inhibition":"The concentration of alkaloid used was at 2 wt.% for most tests and was shown to be effective even at concentrations as low as 0.2 wt.%",
#         "test method": "weight loss method"
#     },
#     {#3
#         "Name of corrosion inhibitor": "sodium humate (SH)",
#         "Corrosion Object Extraction": "EH40 steel",
#         "experimental environment": "natural seawater",
#         "corrosion inhibition":"the optimum concentration is 2 g/L, at this concentration, the inhibition rate can reach 93.6%",
#         "test method": "scanning electron microscope (SEM), atomic force microscope (AFM), contact angle and X-ray photoelectron spectroscopy (XPS)",
#     },
#     {#4
#         "Name of corrosion inhibitor": "CS-PEG",
#         "Corrosion Object Extraction": "mild steel",
#         "experimental environment": "1M HCl",
#         "corrosion inhibition": "The maximum corrosion inhibition efficiency of 93.9% was obtained at a concentration of 200 mg/L",
#         "test method": "weight loss method, electrochemical measurements, surface morphology (AFM) and quantum chemical investigation."
#     },
#     {#5
#         "Name of corrosion inhibitor": "novel quaternary ammonium Gemini surfactant synthesized from chloroacetyl chloride, 1,3-propanediamine, and dodecyldimethyl tertiary amine",
#         "Corrosion Object Extraction": "2024 Al-Cu-Mg alloy",
#         "experimental environment": "1M HCl",
#         "corrosion inhibition": "When the concentration is 1.0 × 10−3 mol L−1, the average corrosion IE reaches a maximum of 87.9%",
#         "test method": "the weight-loss method, electrochemical measurements"
#     },
#     {#6
#         "Name of corrosion inhibitor": "2‐hydroxyethylammonium oleate (2HEAOl)",
#         "Corrosion Object Extraction": "aluminum",
#         "experimental environment": "neutral 0.5 mol/L NaCl",
#         "corrosion inhibition": "the concentration of 5×10−4 mol/L was a suitable concentration to promote corrosion inhibition until 72 h at the high chloride concentration studied，",
#         "test method": "electrochemical characterization, OCP and potentiodynamic polarization measurement,EIS"
#     },
#     {#7
#         "Name of corrosion inhibitor": "zinc aminophosphonate coordination complex (ZnATMP)",
#         "Corrosion Object Extraction": "carbon steel (0.2% C)",
#         "experimental environment": "aqueous medium saturated with oxygen (mg/l: NaCl 914, MgSO4 250, Na2SO4 1924, NaHCO3 361, CaCl2 237), natural aeration, 75°C",
#         "corrosion inhibition": "the corrosion rate decreases from 0.162 to 0.011 mm/year in the presence of the inhibitor, which corresponds to γ = 14.7",
#         "test method": "X-ray photoelectron spectroscopy,"
#     },
#     {#8
#         "Name of corrosion inhibitor": "polyaniline",
#         "Corrosion Object Extraction": "iron",
#         "experimental environment": "0.5M H2SO4",
#         "corrosion inhibition": "the maximum efficiency of 84% has been observed at a concentration of 100 ppm",
#         "test method": "potentiodynamic polarization, linear polarization, electrochemical impedance spectroscopyFTIR studies"
#     },
#     {#9
#         "Name of corrosion inhibitor": "Waterborne Methylamine Adduct",
#         "Corrosion Object Extraction": "carbon steel",
#         "experimental environment": "3% NaCl solution",
#         "corrosion inhibition": "0.5 g of the methylamine adduct per 100 g paint was the optimum concentration which provided the most protective corrosion inhibitio",
#         "test method":"electrochemical, surface, spectroscopic techniques"
#     },
#     {  # 10
#         "Name of corrosion inhibitor": "bis-piperidiniummethyl-urea (BPMU)",
#         "Corrosion Object Extraction": "mild steel",
#         "experimental environment": "simulated atmospheric corrosion water containing Cl⁻ 0.1 kg/m³, HCO₃⁻ 0.1 kg/m³, SO₄²⁻ 0.1 kg/m³",
#         "corrosion inhibition": "BPMU has good protection effect for steel. It suppressed the anodic reaction of the steel electrode in a manner of promoted passivation.",
#         "test method": "Electrochemical measurements,Electrochemical impedance spectro-scopy,Fourier transform infrared (FT-IR) spectroscopy"
#     },
#     {  # 11
#         "Name of corrosion inhibitor": "1-Hexadecylbenzimidazole (HDBI)",
#         "Corrosion Object Extraction": "low carbon steel (LCS)",
#         "experimental environment": "15% HCl",
#         "corrosion inhibition": "with 50 mg/L concentration achieving a 97% corrosion inhibition efficiency in 15% HCl solution at 25°C",
#         "test method": "electrochemical techniques, weight loss measurements"
#     },
#    {  # 12
#        "Name of corrosion inhibitor": "2X-XFJ",
#        "Corrosion Object Extraction": "2024 aluminum alloy",
#        "experimental environment": "20-wt.% HCl solution at 363 K",
#        "corrosion inhibition": "the corrosion inhibition rates calculated by weight loss method, electrochemical impedance method, and potentiodynamic polarization method were 84.5%, 91.5%, and 91.9%, respectively.",
#        "test method": "weight loss method, electrochemical method,XPS and molecular dynamics"
#    },
#    {  # 13
#        "Name of corrosion inhibitor": "N-methyl-2-hydroxyethylammonium oleate ([m-2HEA][Ol])",
#        "Corrosion Object Extraction": "mild steel",
#        "experimental environment": "0.1-mol/L hydrochloric acid",
#        "corrosion inhibition": "[m-2HEA][Ol] can reach up to 94–97% of inhibition efficiency",
#        "test method": "Electrochemical and weight loss measurements, surface contact angle determination, scanning electron microscopy, and Raman spectroscopy"
#    },
#    {  # 14
#        "Name of corrosion inhibitor": "Emblica officinalis (Indian gooseberry) leaves extract",
#        "Corrosion Object Extraction": "mild steel",
#        "experimental environment": "1N HCl",
#        "corrosion inhibition": "Emblica officinalis leaves to be a good corrosion inhibitor of a mixed type and having efficiency of 87.9% at 2% v/v inhibitor concentration",
#        "test method": "weight loss, potentiodynamic polarization and impedance studies"
#    },
#    {  # 15
#        "Name of corrosion inhibitor": "Equisetum arvense extract",
#        "Corrosion Object Extraction": "A36 steel",
#        "experimental environment": "0.5M sulfuric acid",
#        "corrosion inhibition": "a decrease of about two orders of magnitude in the corrosion rate, an increase in polarization resistance and a greater efficiency of inhibition by increasing the concentration of extract",
#        "test method":"determination of the polarization curves, linear polarization resistance (LPR), electrochemical impedance spectroscopy (EIS),scanning electronic microscopy (SEM)"
#    },
#     {  # 16
#         "Name of corrosion inhibitor": "ceria nanoparticles",
#         "Corrosion Object Extraction": "steel",
#         "experimental environment": "saturated Ca(OH)₂ + 0.5M CaCl₂",
#         "corrosion inhibition": "ceria nanoparticles act as an anodic inhibitor and provide maximum inhibition efficiency (80%) at a concentration of 800 ppm",
#         "test method": "electrochemical and various characterization techniques"
#     },
#    {  # 17
#        "Name of corrosion inhibitor": "S, N co-doped carbon dots (CD1), N doped carbon dots (CD2)",
#        "Corrosion Object Extraction": "mild steel",
#        "experimental environment": "15% HCl solution",
#        "corrosion inhibition":"Inhibition efficiency of 96.40 and 90.00%, respectively, at 100 ppm concentration and 303 K temperature",
#        "test method":"Fourier Transform Infrared Spectroscopy (FTIR), Transmission electron microscopy (TEM) and Raman spectroscopy analysis"
#    },
#    {  # 18
#       "Name of corrosion inhibitor": "pomegranate peels crude extract (PPE)",
#       "Corrosion Object Extraction": "mild steel",
#       "experimental environment": "1M HCl",
#       "corrosion inhibition": "the inhibition properties of PPE on steel is significant (η> 95%) in a very corrosive electrolyte, 1M HC",
#       "test method": "stationary and dynamic electrochemical techniques,surface analysis"
#    },
#    {  # 19
#        "Name of corrosion inhibitor": "lignin–(2,3‐epoxypropyl)trimethyl ammonium chloride (EPTAC)",
#        "Corrosion Object Extraction": "carbon steel",
#        "experimental environment": "1mol/L hydrochloric acid",
#        "corrosion inhibition":"inhibition efficiency of 97.80% at 100 mg/L concentration.",
#        "test method":"electrochemical meth-ods, adsorption thermodynamics analysis, and molecular dynamic simulation "
#    },
#     {  # 20
#         "Name of corrosion inhibitor": "sebacic acid",
#         "Corrosion Object Extraction": "hot dip galvanized (HDG) steel",
#         "experimental environment": "0.1 M NaCl",
#         "corrosion inhibition": "an intermediate value of about 5·10−4 M seems to provide HDG substrate with improved corrosion protection",
#         "test method": "electrochemical test,scanning electron microscopy (SEM),Fourier transform infrared (FT‐IR) analysis"
# }
# ]



# 基因定义
GENE_DEFINITIONS = {
    "role_context": [  # Role Definition
        # Direct extraction style - Tool role
        "You are a corrosion literature extraction tool. Strictly extract information in specified format: inhibitor name, concentration, corrosion solution, performance, test methods.",
        # Task description style - Expert role
        "As a professional analyst in corrosion science, systematically analyze experimental data from literature. Your task is to accurately extract core parameters of corrosion inhibitor research, ensuring information completeness and accuracy.",
        # Element combination style - Structured role
        "You are a structured information extraction expert. Decompose literature content into five core dimensions: material, concentration, solution, performance, method, and combine output according to standard template.",
        # Result-oriented style - Application role
        "Your goal is to build standardized data entries for corrosion research database. Extract complete experimental information from literature that can be directly used for data analysis and model building."
    ],

    "material_extraction": [  # Corrosion Inhibitor Name Extraction
        # Direct extraction style - Precise name extraction
        "Extract corrosion inhibitor names.e.g., 'green tea extract', 'imidazoline derivative'.",
        # Task description style - Systematic material identification
        "Systematically identify corrosion inhibitor materials used in the text, including plant extracts, chemical compounds, composite materials, and all types of inhibitor names.",
        # Element combination style - Name element decomposition
        "Identify and extract the key information: the specific names of corrosion inhibitor substances as explicitly mentioned in the text.",
        # Result-oriented style - Material identification oriented
        "To build a corrosion inhibitor material library, extract all corrosion inhibitor names."
    ],

    "corrosion_object_extraction": [  # Corrosion Object Extraction
        # Direct extraction style - Precise object extraction
        "Extract corrosion object names. Format: 'object name', e.g., 'carbon steel', 'stainless steel', 'copper', 'aluminum'.",
        # Task description style - Systematic object identification
        "Systematically identify the material objects protected by the corrosion inhibitor in the experiment like carbon steel, stainless steel, copper, aluminum, and their specific grades.",
        # Element combination style - Object element decomposition
        "Corrosion object identification consists of material type and specific grade. Extract both the base material and any specified grade information.",
        # Result-oriented style - Material protection oriented
        "To understand the application scope of corrosion inhibitors, extract all corrosion object names. These indicate which materials are being protected in the study."
    ],

    "corrosion_solution_extraction": [  # Corrosion Solution Extraction
        # Direct extraction style - Precise medium and concentration extraction
        "Extract corrosion medium type and concentration. Format: 'concentration medium', e.g., '0.5M H₂SO₄', '1 M HCl', '3.5% NaCl'.",
        # Task description style - Systematic medium and concentration extraction
        "Identify the medium type and its concentration used in corrosion experiments. Focus on chemical names of corrosion media and precise concentration values.",
        # Element combination style - Medium and concentration element decomposition
        "Corrosion solution core information contains two elements: 1) medium type (HCl/H₂SO₄/NaCl, etc.) 2) medium concentration (0.5M/1M/3.5%, etc.). Extract and combine these two elements.",
        # Result-oriented style - Solution formulation oriented
        "To determine the basic formulation of corrosion solution, extract medium type and concentration information. Include chemical names of basic corrosion media and corresponding concentrations."
    ],

    "performance_extraction": [  # Corrosion Inhibition Performance Extraction
        # Direct extraction style - Complete performance expression extraction
        "Extract complete corrosion inhibition performance description. Pay attention to the complete association between inhibition efficiency, corrosion inhibitor, and corrosion medium.",
        # Task description style - Systematic performance condition recording
        "Systematically record complete performance data of corrosion inhibitors. Include: inhibition efficiency values, corresponding corrosion inhibitor concentrations, and test corrosion media used.",
        # Element combination style - Performance condition element combination
        "Complete corrosion inhibition performance contains three core elements: 1) efficiency value (percentage) 2) corrosion inhibitor concentration 3) corrosion medium. Combine these elements to form complete performance condition description.",
        # Result-oriented style - Performance comparison analysis oriented
        "For horizontal comparison analysis of corrosion inhibitor performance, extract performance data containing complete experimental conditions. Require simultaneous inclusion of efficiency values, usage concentrations, and corrosion media."
    ],

    "numerical_emphasis": [  # Test Method Extraction
        # Direct extraction style - Precise method name listing
        "Extract test method names. Format: 'method1, method2, method3', e.g., 'weight loss, EIS, polarization'. Separate with commas, list only method names.",
        # Task description style - Systematic method system identification
        "Identify experimental methods used to evaluate corrosion inhibition performance in the text. Include corrosion rate measurement methods, surface analysis techniques, electrochemical test methods, etc.",
        # Element combination style - Method type combination
        "Test methods can be classified by measurement principle. Extract test method names used in the text.",
        # Result-oriented style - Method applicability oriented
        "To evaluate the applicability of test methods, extract all experimental methods used for corrosion inhibition performance evaluation."
    ],

    "temperature": [0.1, 0.1, 0.1, 0.1]  # Temperature parameters[1.0, 1.0, 1.0, 1.0]
}

# 其他配置
PDF_FOLDER = "corrosion_papers"
OUTPUT_DIR = "corrosion_literature_results"

# 在 Standard.py 文件末尾添加

# 提示词风格定义
PROMPT_STYLES = {
    0: "Direct extraction style",
    1: "Task description style",
    2: "Element combination style",
    3: "Result-oriented style"
}

# 风格颜色定义（用于绘图）- 使用更浅的颜色
STYLE_COLORS = {
    "Direct extraction style": "#FFB6C1",  # 浅粉色
    "Task description style": "#98FB98",   # 浅绿色
    "Element combination style": "#87CEFA", # 浅蓝色
    "Result-oriented style": "#FFFACD"     # 浅黄色
}