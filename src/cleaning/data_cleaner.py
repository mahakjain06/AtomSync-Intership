
import pandas as pd
from pathlib import Path

# Locate project directory
project_root = Path(__file__).resolve().parents[2]

# Read original sensor data
input_file = project_root / "data" / "sensor_readings.csv"
df = pd.read_csv(input_file)

print("AtmoSync - Data Cleaning")
print("------------------------")

# Original record count
print("Original records:", len(df))

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values
df = df.dropna(subset=[
    "shipment_id",
    "timestamp",
    "temperature_c",
    "humidity_percent",
    "vibration_g"
])

# Convert sensor columns to numeric
sensor_columns = [
    "temperature_c",
    "humidity_percent",
    "vibration_g"
]

for column in sensor_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Remove rows with invalid sensor values
df = df.dropna(subset=sensor_columns)

# Keep readings within our simulation ranges
df = df[
    df["temperature_c"].between(2, 15) &
    df["humidity_percent"].between(50, 95) &
    df["vibration_g"].between(0, 3)
]

# Save cleaned dataset
output_file = project_root / "data" / "cleaned_sensor_readings.csv"
df.to_csv(output_file, index=False)

print("Cleaned records:", len(df))
print("Removed records:", "Original - Cleaned =", "completed")
print("Cleaned dataset saved at:", output_file)
print("\nData cleaning completed!")
