
# ==========================================
# AGRICULTURE PRODUCTION ANALYSIS
# DATA VISUALIZATION
# ACADEMIC YEAR 2026
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================
# STEP 1: PROJECT PATHS
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_FOLDER = PROJECT_ROOT / "Dataset"

GRAPHS_FOLDER = PROJECT_ROOT / "Graphs"

# Create Graphs folder automatically
GRAPHS_FOLDER.mkdir(exist_ok=True)

# ==========================================
# STEP 2: LOAD CLEANED DATASET
# ==========================================

df = pd.read_csv(
    DATASET_FOLDER / "clean_dataset.csv"
)

print("DATASET LOADED SUCCESSFULLY")
print("DATASET SHAPE:", df.shape)

# ==========================================
# 1. PRODUCTION BY CROP
# ==========================================

crop_production = df.groupby("Crop")[
    "Production_Tonnes"
].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))

crop_production.plot(kind="bar", color="steelblue")

plt.title("Agricultural Production by Crop")
plt.xlabel("Crop Name")
plt.ylabel("Total Production (Tonnes)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    GRAPHS_FOLDER / "production_by_crop.png",
    dpi=300
)

plt.show()

# ==========================================
# 2. PRODUCTION BY STATE
# ==========================================

state_production = df.groupby("State")[
    "Production_Tonnes"
].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))

state_production.plot(kind="bar", color="green")

plt.title("Agricultural Production by State")
plt.xlabel("State")
plt.ylabel("Total Production (Tonnes)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    GRAPHS_FOLDER / "production_by_state.png",
    dpi=300
)

plt.show()

# ==========================================
# 3. YEAR-WISE PRODUCTION
# ==========================================

year_production = df.groupby("Year")[
    "Production_Tonnes"
].sum().sort_index()

plt.figure(figsize=(10, 6))

year_production.plot(
    kind="line",
    marker="o",
    color="darkorange"
)

plt.title("Agricultural Production Trend by Year")
plt.xlabel("Year")
plt.ylabel("Total Production (Tonnes)")
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    GRAPHS_FOLDER / "production_by_year.png",
    dpi=300
)

plt.show()

# ==========================================
# 4. AVERAGE YIELD BY SEASON
# ==========================================

season_yield = df.groupby("Season")[
    "Yield_Tonnes_per_Hectare"
].mean().sort_values(ascending=False)

plt.figure(figsize=(8, 5))

season_yield.plot(kind="bar", color="orange")

plt.title("Average Agricultural Yield by Season")
plt.xlabel("Season")
plt.ylabel("Average Yield (Tonnes per Hectare)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    GRAPHS_FOLDER / "average_yield_by_season.png",
    dpi=300
)

plt.show()

print("\nAVERAGE YIELD BY SEASON")
print(season_yield)

# ==========================================
# 5. AVERAGE YIELD BY IRRIGATION METHOD
# ==========================================

irrigation_yield = df.groupby("Irrigation_Method")[
    "Yield_Tonnes_per_Hectare"
].mean().sort_values(ascending=False)

plt.figure(figsize=(9, 5))

irrigation_yield.plot(kind="bar", color="teal")

plt.title("Average Crop Yield by Irrigation Method")
plt.xlabel("Irrigation Method")
plt.ylabel("Average Yield (Tonnes per Hectare)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    GRAPHS_FOLDER / "yield_by_irrigation.png",
    dpi=300
)

plt.show()

print("\nAVERAGE YIELD BY IRRIGATION METHOD")
print(irrigation_yield)

# ==========================================
# 6. RAINFALL VS CROP YIELD
# ==========================================

plt.figure(figsize=(9, 6))

plt.scatter(
    df["Rainfall_mm"],
    df["Yield_Tonnes_per_Hectare"],
    alpha=0.6,
    color="royalblue"
)

plt.title("Relationship Between Rainfall and Crop Yield")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Crop Yield (Tonnes per Hectare)")
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    GRAPHS_FOLDER / "rainfall_vs_yield.png",
    dpi=300
)

plt.show()

correlation = df["Rainfall_mm"].corr(
    df["Yield_Tonnes_per_Hectare"]
)

print("\nRAINFALL VS CROP YIELD CORRELATION")
print(correlation)

# ==========================================
# 7. FERTILIZER USAGE VS CROP YIELD
# ==========================================

plt.figure(figsize=(9, 6))

plt.scatter(
    df["Fertilizer_kg_per_hectare"],
    df["Yield_Tonnes_per_Hectare"],
    alpha=0.6,
    color="purple"
)

plt.title("Fertilizer Usage vs Crop Yield")
plt.xlabel("Fertilizer (kg per hectare)")
plt.ylabel("Crop Yield (Tonnes per Hectare)")
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    GRAPHS_FOLDER / "fertilizer_vs_yield.png",
    dpi=300
)

plt.show()

correlation = df["Fertilizer_kg_per_hectare"].corr(
    df["Yield_Tonnes_per_Hectare"]
)

print("\nFERTILIZER VS CROP YIELD CORRELATION")
print(correlation)

# ==========================================
# 8. AVERAGE YIELD BY SOIL TYPE
# ==========================================

soil_yield = df.groupby("Soil_Type")[
    "Yield_Tonnes_per_Hectare"
].mean().sort_values(ascending=False)

plt.figure(figsize=(9, 6))

soil_yield.plot(kind="bar", color="brown")

plt.title("Average Crop Yield by Soil Type")
plt.xlabel("Soil Type")
plt.ylabel("Average Yield (Tonnes per Hectare)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    GRAPHS_FOLDER / "yield_by_soil_type.png",
    dpi=300
)

plt.show()

print("\nAVERAGE YIELD BY SOIL TYPE")
print(soil_yield)

# ==========================================
# 9. CULTIVATED AREA VS PRODUCTION
# ==========================================

plt.figure(figsize=(9, 6))

plt.scatter(
    df["Area_Hectares"],
    df["Production_Tonnes"],
    alpha=0.6,
    color="darkgreen"
)

plt.title("Cultivated Area vs Agricultural Production")
plt.xlabel("Cultivated Area (Hectares)")
plt.ylabel("Production (Tonnes)")
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    GRAPHS_FOLDER / "area_vs_production.png",
    dpi=300
)

plt.show()

correlation = df["Area_Hectares"].corr(
    df["Production_Tonnes"]
)

print("\nAREA VS PRODUCTION CORRELATION")
print(correlation)

# ==========================================
# 10. CORRELATION HEATMAP
# ==========================================

numeric_df = df.select_dtypes(
    include=np.number
).drop(
    columns=["Record_ID"],
    errors="ignore"
)

correlation_matrix = numeric_df.corr()

plt.figure(figsize=(12, 8))

plt.imshow(
    correlation_matrix,
    cmap="RdYlBu_r",
    interpolation="nearest",
    vmin=-1,
    vmax=1
)

plt.colorbar(
    label="Correlation Coefficient"
)

plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

for i in range(len(correlation_matrix.columns)):
    for j in range(len(correlation_matrix.columns)):
        plt.text(
            j,
            i,
            f"{correlation_matrix.iloc[i, j]:.2f}",
            ha="center",
            va="center",
            color="black",
            fontsize=9
        )

plt.title("Correlation Heatmap of Agricultural Factors")
plt.tight_layout()

plt.savefig(
    GRAPHS_FOLDER / "heatmap_correlation.png",
    dpi=300
)

plt.show()

print("\nCORRELATION HEATMAP CREATED SUCCESSFULLY!")

# ==========================================
# COMPLETION
# ==========================================

print("\nALL 10 VISUALIZATIONS COMPLETED!")
print("GRAPHS SAVED IN:", GRAPHS_FOLDER)