
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path


# Generate simulated sensor readings for a shipment
def generate_sensor_data(shipment_id, num_readings=10):

    readings = []

    start_time = datetime.now()

    for i in range(num_readings):

        temperature = round(np.random.uniform(2, 12), 2)
        humidity = round(np.random.uniform(60, 90), 2)
        vibration = round(np.random.uniform(0.1, 2.0), 2)

        timestamp = start_time + timedelta(minutes=i * 5)

        readings.append({
            "shipment_id": shipment_id,
            "timestamp": timestamp,
            "temperature_c": temperature,
            "humidity_percent": humidity,
            "vibration_g": vibration
        })

    return readings


# Generate data for two shipments
all_readings = []

all_readings.extend(
    generate_sensor_data("SHIP001", 10)
)

all_readings.extend(
    generate_sensor_data("SHIP002", 10)
)


# Convert data into a Pandas DataFrame
df = pd.DataFrame(all_readings)


# Save the dataset inside the data folder
project_root = Path(__file__).resolve().parents[2]
output_folder = project_root / "data"
output_folder.mkdir(exist_ok=True)

output_file = output_folder / "sensor_readings.csv"

df.to_csv(output_file, index=False)


print("AtmoSync Sensor Data Generated Successfully!")
print(df.head())

print(f"\nTotal readings: {len(df)}")
print(f"Dataset saved at: {output_file}")
