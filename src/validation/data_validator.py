import pandas as pd
from pathlib import Path

# Project folder location
project_root = Path(__file__).resolve().parents[2]

# Read sensor data
input_file = project_root / "data" / "sensor_readings.csv"
df = pd.read_csv(input_file)

print("AtmoSync - Sensor Data Validation")
print("----------------------------------")

# 1. Check required columns
required_columns = [
    "shipment_id",
    "timestamp",
    "temperature_c",
    "humidity_percent",
    "vibration_g"
]

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    print("Missing columns:", missing_columns)
else:
    print("All required columns are available.")

# 2. Check missing values
print("\nMissing values:")
print(df[required_columns].isnull().sum())

# 3. Check duplicate records
duplicates = df.duplicated().sum()
print("\nDuplicate records:", duplicates)

# 4. Check invalid sensor readings
invalid_temperature = (
    (df["temperature_c"] < 2) |
    (df["temperature_c"] > 15)
).sum()

invalid_humidity = (
    (df["humidity_percent"] < 50) |
    (df["humidity_percent"] > 95)
).sum()

invalid_vibration = (
    (df["vibration_g"] < 0) |
    (df["vibration_g"] > 3)
).sum()

print("\nInvalid readings:")
print("Temperature:", invalid_temperature)
print("Humidity:", invalid_humidity)
print("Vibration:", invalid_vibration)

print("\nTotal records:", len(df))
print("Validation completed!")
