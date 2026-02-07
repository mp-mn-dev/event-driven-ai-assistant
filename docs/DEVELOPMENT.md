# Development Guide

Building this project commit-by-commit.

---

## Prerequisites

- Docker running (`docker-compose ps` should work)
- Python virtual environment activated (`source venv/bin/activate`)

---

## Commit 1: Create Basic Kafka Producer and Consumer ✅

**What it does:** Reads events from Kafka and displays them (no AI yet)

### Run It

**Terminal 1 - Start Consumer:**
```bash
python3 consumer/ai_consumer.py
```
Consumer waits for events.

**Terminal 2 - Generate Events:**
```bash
python3 producer/event_producer.py
```

**Verify:** Events appear in Terminal 1 with formatted output.

**Stop:** `Ctrl+C` in Terminal 1

---

## Commit 2: OpenAI Integration (Next)

**What it does:** Adds AI analysis to each event

*(Coming soon...)*

---

## Commit 3: Error Handling - Simple (Planned)

**What it does:** Logs errors when AI fails

---

## Commit 4: Error Handling - DLQ (Planned)

**What it does:** Failed events → dead letter queue

---

## Commit 5: Error Handling - Full Retry Pattern (Planned)

**What it does:** Retry topic + exponential backoff

---

## Commit 6: Polish (Planned)

**What it does:** Tests, docs, cleanup

---

## Troubleshooting

**Consumer shows "Waiting..." but no events?**
- Check: `docker-compose ps` (all 3 containers "Up"?)
- Wait 30 seconds after `docker-compose up -d`
- Try: `docker-compose restart`

**Want to reset and start fresh?**
```bash
docker-compose down -v  # Deletes all messages
docker-compose up -d
sleep 30
```

---

## Useful Commands

**View messages in Kafka directly:**
```bash
docker exec -it event-driven-ai-assistant-kafka-1 \
  kafka-console-consumer --bootstrap-server localhost:9092 \
  --topic system-events --from-beginning
```

**Check consumer group offset:**
```bash
docker exec -it event-driven-ai-assistant-kafka-1 \
  kafka-consumer-groups --bootstrap-server localhost:9092 \
  --describe --group ai-consumer-group
```

---

## Resources

- [Kafka Python Docs](https://kafka-python.readthedocs.io/)
- [OpenAI API Docs](https://platform.openai.com/docs)
