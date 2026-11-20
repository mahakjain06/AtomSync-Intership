
import json
import time
from pathlib import Path

import pandas as pd
from kafka import KafkaProducer

# Find project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CSV_FILE = PROJECT_ROOT / "data" / "sensor_readings.csv"

# Connect to Kafka broker
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)

# Read sensor data
df = pd.read_csv(CSV_FILE)

print(f"Sending {len(df)} sensor readings to Kafka...")

# Send readings
for _, row in df.iterrows():
    sensor_data = row.to_dict()

    producer.send(
        "atmosync-sensor-data",
        value=sensor_data
    )

    print("Sent:", sensor_data)
    time.sleep(1)

producer.flush()
producer.close()

print("All sensor readings sent successfully!")
