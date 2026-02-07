# Event-Driven AI Assistant

Real-time event processing with Kafka and AI-powered analysis.

## 🏗️ Architecture
```
Producer → Kafka → Consumer → OpenAI → Insights
```

1. **Producer** generates system events
2. **Kafka** queues events in real-time
3. **Consumer** reads events and sends to OpenAI
4. **OpenAI** provides intelligent analysis

## 📁 Project Structure
```
event-driven-ai-assistant/
├── producer/
│   └── event_producer.py    # Generates system events
├── consumer/
│   └── ai_consumer.py        # Consumes & analyzes with AI
├── schemas/
│   └── system_event.avsc     # Avro event schema
├── docs/
│   └── ARCHITECTURE.md       # Detailed architecture docs
└── docker-compose.yml        # Kafka cluster setup
```

## 🚀 Quick Start

**1. Start Kafka:**
```bash
docker-compose up -d
```

**2. Run Producer (generates events):**
```bash
python producer/event_producer.py
```

**3. Run Consumer (analyzes with AI):**
```bash
python consumer/ai_consumer.py
```

## 💡 What This Demonstrates

- Event-driven architecture with Kafka
- Real-time stream processing
- LLM integration for intelligent analysis
- Production-ready patterns (producer/consumer)

## 📖 Detailed Documentation

See [ARCHITECTURE.md](docs/ARCHITECTURE.md) for complete system design.