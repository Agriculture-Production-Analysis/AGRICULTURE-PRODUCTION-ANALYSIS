
# ==========================================
# AGRICULTURE PRODUCTION ANALYSIS
# EXPLORATORY DATA ANALYSIS (EDA)
# ACADEMIC YEAR 2026
# ==========================================

import pandas as pd
import numpy as np
from pathlib import Path

# ==========================================
# STEP 1: PROJECT PATHS
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_FOLDER = PROJECT_ROOT / "Dataset"

# ==========================================
# STEP 2: LOAD CLEANED DATASET
# ==========================================

input_file = DATASET_FOLDER / "clean_dataset.csv"

df = pd.read_csv(input_file)

print("DATASET LOADED SUCCESSFULLY")

# ==========================================
# STEP 3: DATASET OVERVIEW
# ==========================================

print("\nDATASET SHAPE")
print(df.shape)

print("\nSTATISTICAL SUMMARY")
print(df.describe())

# ==========================================
# STEP 4: AVAILABLE CATEGORIES
# ==========================================

print("\nAVAILABLE CROPS")
print(df["Crop"].unique())

print("\nAVAILABLE STATES")
print(df["State"].unique())

print("\nAVAILABLE SEASONS")
print(df["Season"].unique())

# ==========================================
# STEP 5: PRODUCTION ANALYSIS
# ==========================================

# 1. TOTAL PRODUCTION BY CROP

print("\nTOTAL PRODUCTION BY CROP")

crop_production = df.groupby("Crop")[
    "Production_Tonnes"
].sum().sort_values(ascending=False)

print(crop_production)

# 2. TOTAL PRODUCTION BY STATE

print("\nTOTAL PRODUCTION BY STATE")

state_production = df.groupby("State")[
    "Production_Tonnes"
].sum().sort_values(ascending=False)

print(state_production)

# 3. TOTAL PRODUCTION BY YEAR

print("\nTOTAL PRODUCTION BY YEAR")

year_production = df.groupby("Year")[
    "Production_Tonnes"
].sum().sort_index()

print(year_production)

# 4. AVERAGE YIELD BY SEASON

print("\nAVERAGE YIELD BY SEASON")

season_yield = df.groupby("Season")[
    "Yield_Tonnes_per_Hectare"
].mean().sort_values(ascending=False)

print(season_yield)

# ==========================================
# STEP 6: KEY FINDINGS
# ==========================================

print("\nHIGHEST PRODUCING CROP")
print(crop_production.idxmax())

print("\nHIGHEST PRODUCING STATE")
print(state_production.idxmax())

print("\nYEAR WITH HIGHEST PRODUCTION")
print(year_production.idxmax())

# ==========================================
# STEP 7: SAVE ANALYSIS RESULTS
# ==========================================

crop_production.to_csv(
    DATASET_FOLDER / "crop_production.csv"
)

state_production.to_csv(
    DATASET_FOLDER / "state_production.csv"
)

year_production.to_csv(
    DATASET_FOLDER / "year_production.csv"
)

season_yield.to_csv(
    DATASET_FOLDER / "season_yield.csv"
)

print("\nANALYSIS RESULTS SAVED SUCCESSFULLY!")

print("\nOUTPUT LOCATION:")
print(DATASET_FOLDER)

print("\nDATA ANALYSIS COMPLETED SUCCESSFULLY!")