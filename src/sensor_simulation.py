
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

OUTPUT = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "sensor_data.csv"
)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

locations = ["Tirupati", "Chennai", "Bangalore", "Hyderabad"]

with OUTPUT.open("w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "timestamp",
        "sensor_id",
        "location",
        "temperature_c",
        "humidity_percent",
        "wind_speed_kmh",
        "rainfall_mm"
    ])

    start_time = datetime.now() - timedelta(days=7)

    for i in range(500):
        timestamp = start_time + timedelta(minutes=20 * i)

        writer.writerow([
            timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            f"SENSOR_{random.randint(1, 10):03d}",
            random.choice(locations),
            round(random.uniform(20, 42), 2),
            round(random.uniform(30, 95), 2),
            round(random.uniform(0, 35), 2),
            round(random.uniform(0, 15), 2)
        ])

print("Sensor data generated successfully!")
print(f"Output file: {OUTPUT}")
