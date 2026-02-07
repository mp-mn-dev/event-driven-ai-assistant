"""
Event Producer - Part 1 of the Pipeline

Flow:
1. This script generates fake system events (errors, warnings, etc.)
2. Sends those events to the Kafka topic 'system-events'
3. Consumer (ai_consumer.py) will read these events
4. Consumer sends to OpenAI for intelligent analysis

Real-world use: In production, actual microservices would publish events
to Kafka instead of this simulator.
"""

from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime
import uuid


class SystemEventProducer:
    def __init__(self, bootstrap_servers=['localhost:9092']):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.topic = 'system-events'

    def generate_event(self):
        """Generate a realistic system event"""
        event_types = [
            ("ERROR", "API endpoint /users returned 500 error - database connection timeout"),
            ("WARNING", "Memory usage at 85% on service-auth pod-3"),
            ("DEPLOYMENT", "New version v2.1.0 deployed to production"),
            ("SCALE_EVENT", "Auto-scaled payment-service from 3 to 8 replicas due to high load"),
            ("PERFORMANCE_DEGRADATION", "API response time increased from 120ms to 450ms"),
            ("SECURITY_ALERT", "Multiple failed login attempts detected from IP 192.168.1.100")
        ]

        services = ["api-gateway", "auth-service", "payment-service", "user-service", "notification-service"]
        environments = ["PRODUCTION", "STAGING", "DEVELOPMENT"]
        severities = {
            "ERROR": ["MEDIUM", "HIGH", "CRITICAL"],
            "WARNING": ["LOW", "MEDIUM"],
            "DEPLOYMENT": ["LOW", "MEDIUM"],
            "SCALE_EVENT": ["LOW", "MEDIUM", "HIGH"],
            "PERFORMANCE_DEGRADATION": ["MEDIUM", "HIGH"],
            "SECURITY_ALERT": ["HIGH", "CRITICAL"]
        }

        event_type, details = random.choice(event_types)
        service = random.choice(services)
        environment = random.choice(environments)
        severity = random.choice(severities[event_type])

        event = {
            "event_id": str(uuid.uuid4()),
            "service_name": service,
            "event_type": event_type,
            "timestamp": int(time.time() * 1000),  # milliseconds
            "environment": environment,
            "details": details,
            "severity": severity,
            "metadata": json.dumps({
                "region": "us-east-1",
                "cluster": "prod-cluster-01",
                "version": f"v{random.randint(1, 3)}.{random.randint(0, 5)}.{random.randint(0, 10)}"
            })
        }

        return event

    def send_event(self, event):
        """Send event to Kafka"""
        future = self.producer.send(self.topic, event)
        self.producer.flush()
        return future

    def run(self, num_events=10, interval=2):
        """Generate and send multiple events"""
        print(f"🚀 Starting event producer - generating {num_events} events...")
        print(f"📤 Publishing to topic: {self.topic}\n")

        for i in range(num_events):
            event = self.generate_event()
            self.send_event(event)

            print(f"[{i + 1}/{num_events}] 📨 Sent {event['event_type']} event")
            print(f"  Service: {event['service_name']}")
            print(f"  Severity: {event['severity']}")
            print(f"  Details: {event['details'][:60]}...")
            print()

            time.sleep(interval)

        print("✅ All events sent!")


if __name__ == "__main__":
    producer = SystemEventProducer()
    producer.run(num_events=5, interval=3)