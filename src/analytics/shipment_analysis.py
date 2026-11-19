
import pandas as pd
from pathlib import Path

# Locate project directory
project_root = Path(__file__).resolve().parents[2]

# Load cleaned sensor data
input_file = project_root / "data" / "cleaned_sensor_readings.csv"
df = pd.read_csv(input_file)

print("AtmoSync - Shipment Analytics")
print("-----------------------------")

# Convert timestamp into datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Calculate shipment-level statistics
summary = df.groupby("shipment_id").agg(
    total_readings=("shipment_id", "count"),
    avg_temperature=("temperature_c", "mean"),
    max_temperature=("temperature_c", "max"),
    min_temperature=("temperature_c", "min"),
    avg_humidity=("humidity_percent", "mean"),
    max_humidity=("humidity_percent", "max"),
    avg_vibration=("vibration_g", "mean"),
    max_vibration=("vibration_g", "max")
).reset_index()

# Round decimal values
numeric_columns = summary.select_dtypes(
    include="number"
).columns

summary[numeric_columns] = summary[numeric_columns].round(2)

# Save shipment summary
output_file = project_root / "data" / "shipment_summary.csv"
summary.to_csv(output_file, index=False)

print(summary)
print("\nShipment analytics completed!")
print("Summary saved at:", output_file)
