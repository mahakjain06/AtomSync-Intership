
import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "atmosync-sensor-data",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="atmosync-test-consumer",
    value_deserializer=lambda data: json.loads(data.decode("utf-8")),
    consumer_timeout_ms=10000
)

print("Receiving AtmoSync sensor readings from Kafka...\n")

count = 0

for message in consumer:
    print("Received:", message.value)
    count += 1

consumer.close()

print(f"\nTotal sensor readings received: {count}")
