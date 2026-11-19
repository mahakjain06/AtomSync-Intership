
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]

input_file = project_root / "data" / "cleaned_sensor_readings.csv"
df = pd.read_csv(input_file)

df["timestamp"] = pd.to_datetime(df["timestamp"])

charts = [
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
