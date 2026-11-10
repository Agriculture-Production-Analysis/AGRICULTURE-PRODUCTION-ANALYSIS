"""
Create charts from the cleaned agriculture crop analytics dataset.
Run: python Data_visualisation.py
Charts are saved in the charts folder.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

FILE = "clean_dataset.csv"
OUT_DIR = "charts"

def create_visualisations(file_name=FILE):
    """Generate crop, state, season and disease-risk charts."""
    data = pd.read_csv(file_name)
    os.makedirs(OUT_DIR, exist_ok=True)

    charts = [
        ("Average_Yield_by_Crop.png",
         data.groupby("Crop")["Yield_Tons"].mean().sort_values(ascending=False),
         "Average Yield by Crop", "Crop", "Average Yield (Tons)", "bar"),
        ("Total_Profit_by_State.png",
         data.groupby("State")["Profit_INR"].sum().sort_values(ascending=False).head(10),
         "Top 10 States by Total Profit", "State", "Total Profit (INR)", "bar"),
        ("Production_by_Season.png",
         data.groupby("Season")["Yield_Tons"].sum(),
         "Total Production by Season", "Season", "Yield (Tons)", "bar"),
        ("Disease_Risk_Distribution.png",
         data["Disease_Risk"].value_counts(),
         "Disease Risk Distribution", "Disease Risk", "Number of Records", "pie"),
    ]

    for filename, series, title, xlabel, ylabel, chart_type in charts:
        plt.figure(figsize=(10, 6))
        if chart_type == "pie":
            plt.pie(series.values, labels=series.index, autopct="%1.1f%%", startangle=90)
        else:
            series.plot(kind="bar")
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.xticks(rotation=35, ha="right")
        plt.title(title)
        plt.tight_layout()
        plt.savefig(os.path.join(OUT_DIR, filename), dpi=150)
        plt.close()
        print("Saved:", os.path.join(OUT_DIR, filename))

if __name__ == "__main__":
    create_visualisations()
