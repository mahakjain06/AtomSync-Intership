# Kafka Streaming Layer

Responsible for streaming container IoT telemetry and delivering it
to Snowflake.

## Flow
Python simulator (producer) -> Kafka topic -> Python consumer -> Snowflake

## Topic
- Name: iot.container.telemetry
- Partitions: 6
- Key: container_id (keeps each container's events ordered)

## Message format (JSON)
| Field | Type | Description |
|---|---|---|
| event_id | string | Unique ID, used later to remove duplicates |
| container_id | string | e.g. CNT-007 |
| commodity | string | e.g. avocado |
| event_ts | string (ISO 8601) | Time of the reading |
| temperature_c | float | Internal temperature |
| humidity_pct | float | Internal humidity |
| vibration_g | float | Vibration level |
| lat, lon | float | Container location |

## Run locally
docker compose up -d
bash scripts/create_topic.sh