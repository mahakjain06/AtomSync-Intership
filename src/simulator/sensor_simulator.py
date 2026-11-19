
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path


def generate_sensor_data(shipment_id, num_readings=20):

    readings = []

    start_time = datetime.now()

    # Initial sensor conditions
    temperature = np.random.uniform(4, 8)
    humidity = np.random.uniform(65, 80)

    for i in range(num_readings):

        # Temperature changes gradually
        temperature += np.random.uniform(-0.3, 0.5)

        # Humidity fluctuates slightly
        humidity += np.random.uniform(-2, 2)

        # Simulate normal vibration with occasional spikes
        vibration = np.random.uniform(0.1, 0.8)

        if np.random.random() < 0.15:
            vibration = np.random.uniform(1.0, 2.5)

        # Keep readings within simulation boundaries
        temperature = np.clip(temperature, 2, 15)
        humidity = np.clip(humidity, 50, 95)

        timestamp = start_time + timedelta(minutes=i * 5)

        readings.append({
            "shipment_id": shipment_id,
            "timestamp": timestamp,
            "temperature_c": round(temperature, 2),
            "humidity_percent": round(humidity, 2),
            "vibration_g": round(vibration, 2)
        })

    return readings


# Generate data for two shipments
all_readings = []

all_readings.extend(generate_sensor_data("SHIP001", 20))
all_readings.extend(generate_sensor_data("SHIP002", 20))


# Convert to DataFrame
df = pd.DataFrame(all_readings)

# Save CSV
project_root = Path(__file__).resolve().parents[2]
output_folder = project_root / "data"
output_folder.mkdir(exist_ok=True)

output_file = output_folder / "sensor_readings.csv"

df.to_csv(output_file, index=False)

print("AtmoSync Improved Sensor Simulation Completed!")
print(df.head(10))

print("\nTotal readings:", len(df))
print("Average temperature:", round(df["temperature_c"].mean(), 2))
print("Average humidity:", round(df["humidity_percent"].mean(), 2))
print("Dataset saved at:", output_file)
