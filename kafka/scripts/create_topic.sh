#!/bin/bash
docker exec atmosync-kafka /opt/kafka/bin/kafka-topics.sh \
  --create \
  --topic iot.container.telemetry \
  --bootstrap-server localhost:9092 \
  --partitions 6 \
  --replication-factor 1