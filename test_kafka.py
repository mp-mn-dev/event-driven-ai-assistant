from kafka import KafkaProducer, KafkaConsumer
import json
import time

print("Testing Kafka connection...")

# Test producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send test message
test_msg = {"test": "hello kafka", "timestamp": int(time.time())}
producer.send('test-topic', test_msg)
producer.flush()
print(f"✅ Sent: {test_msg}")

# Test consumer
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    consumer_timeout_ms=5000
)

print("Waiting for message...")
for message in consumer:
    print(f"✅ Received: {message.value}")
    break

print("\n🎉 Kafka is working!")