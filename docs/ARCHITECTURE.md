# System Architecture

## Overview
Real-time event processing system using Kafka and AI for intelligent system monitoring.

## Components

### 1. Event Producer
- **Location:** `producer/event_producer.py`
- **Purpose:** Simulates system events (errors, warnings, deployments)
- **Output:** Publishes events to Kafka topic `system-events`

### 2. Kafka Cluster
- **Components:** Zookeeper, Kafka Broker, Schema Registry
- **Topic:** `system-events`
- **Purpose:** Message queue for event streaming

### 3. AI Consumer (Next to build)
- **Location:** `consumer/ai_consumer.py`
- **Purpose:** Consumes events and analyzes with OpenAI
- **Output:** Intelligent insights about system issues

## Data Flow
```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│   Producer  │────────>│    Kafka    │────────>│  Consumer   │────────>│  OpenAI API │
│             │  Events │   Topic     │  Events │             │ Prompt  │             │
│ Generates   │         │ (Queue)     │         │ Reads &     │         │ Returns     │
│ System      │         │             │         │ Sends to AI │         │ Analysis    │
│ Events      │         │             │         │             │         │             │
└─────────────┘         └─────────────┘         └─────────────┘         └─────────────┘
```

## Event Schema

See `schemas/system_event.avsc` for full Avro schema.

**Example Event:**
```json
{
  "event_id": "abc-123",
  "service_name": "payment-service",
  "event_type": "ERROR",
  "timestamp": 1707264000000,
  "environment": "PRODUCTION",
  "details": "API endpoint /users returned 500 error",
  "severity": "HIGH",
  "metadata": "{...}"
}
```

## AI Analysis Flow

1. Consumer receives event from Kafka
2. Formats event details into prompt
3. Sends to OpenAI API
4. Receives intelligent analysis:
   - Root cause possibilities
   - Recommended actions
   - Related concerns

## Local Development

**Start Kafka:**
```bash
docker-compose up -d
```

**Run Producer:**
```bash
python producer/event_producer.py
```

**Run Consumer:**
```bash
python consumer/ai_consumer.py
```

## Use Cases

- Real-time system monitoring
- Intelligent alert analysis
- Operational insights
- Automated incident triage