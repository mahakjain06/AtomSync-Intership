
import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]

input_file = project_root / "data" / "shipment_summary.csv"
df = pd.read_csv(input_file)

print("AtmoSync - Shipment Risk Indicator Analysis")
print("-------------------------------------------")

# Illustrative demo thresholds, not validated spoilage limits
def classify_risk(row):
    if (
        row["max_temperature"] > 10
        or row["max_vibration"] > 1.5
        or row["max_humidity"] > 90
    ):
        return "High"

    elif (
        row["avg_temperature"] > 8
        or row["avg_vibration"] > 0.8
    ):
        return "Medium"

    return "Low"


df["risk_level"] = df.apply(classify_risk, axis=1)

output_file = project_root / "data" / "shipment_risk_report.csv"
df.to_csv(output_file, index=False)

print(df[["shipment_id", "risk_level"]])

print("\nRisk analysis completed!")
print("Report saved at:", output_file)
