
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

OUTPUT = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "shipment_data.csv"
)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

routes = [
    ("Tirupati", "Chennai"),
    ("Chennai", "Bangalore"),
    ("Bangalore", "Hyderabad"),
    ("Hyderabad", "Tirupati"),
    ("Tirupati", "Bangalore")
]

products = ["Electronics", "Food", "Textiles", "Medicines"]

with OUTPUT.open("w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "shipment_id",
        "origin",
        "destination",
        "product",
        "shipment_date",
        "distance_km",
        "base_cost",
        "temperature_sensitivity",
        "humidity_sensitivity"
    ])

    start_date = datetime.now() - timedelta(days=30)

    for i in range(1, 501):
        origin, destination = random.choice(routes)

        shipment_date = start_date + timedelta(
            days=random.randint(0, 30)
        )

        writer.writerow([
            f"SHIP_{i:04d}",
            origin,
            destination,
            random.choice(products),
            shipment_date.strftime("%Y-%m-%d"),
            random.randint(50, 700),
            round(random.uniform(1000, 15000), 2),
            random.choice(["Low", "Medium", "High"]),
            random.choice(["Low", "Medium", "High"])
        ])

print("Shipment data generated successfully!")
print(f"Output file: {OUTPUT}")
