
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]

input_file = project_root / "data" / "cleaned_sensor_readings.csv"
df = pd.read_csv(input_file)

df["timestamp"] = pd.to_datetime(df["timestamp"])

charts = [
    ("temperature_c", "Shipment Temperature Monitoring",
     "Temperature (°C)", "temperature_chart.png"),

    ("humidity_percent", "Shipment Humidity Monitoring",
     "Humidity (%)", "humidity_chart.png"),

    ("vibration_g", "Shipment Vibration Monitoring",
     "Vibration (g)", "vibration_chart.png")
]
for column, title, ylabel, filename in charts:
    plt.figure(figsize=(10, 5))

    for shipment_id, group in df.groupby("shipment_id"):
        plt.plot(
            group["timestamp"],
            group[column],
            marker="o",
            label=shipment_id
        )

    plt.title(title)
    plt.xlabel("Timestamp")
    plt.ylabel(ylabel)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    output_file = project_root / "data" / filename
    plt.savefig(output_file)
    plt.close()

    print("Chart saved:", output_file)

print("\nAll visualizations completed!")

# Shipment Risk Distribution Chart

risk_file = project_root / "data" / "shipment_risk_report.csv"
risk_df = pd.read_csv(risk_file)

risk_counts = (
    risk_df["risk_level"]
    .value_counts()
    .reindex(["High", "Medium", "Low"], fill_value=0)
)

plt.figure(figsize=(8, 5))

plt.bar(
    risk_counts.index,
    risk_counts.values
)

plt.title("Shipment Risk Distribution")
plt.xlabel("Risk Level")
plt.ylabel("Number of Shipments")

plt.tight_layout()

output_file = project_root / "data" / "risk_distribution_chart.png"
plt.savefig(output_file)
plt.close()

print("Risk distribution chart saved:", output_file)