"""
AI-Powered Event Consumer

Consumes system events from Kafka and provides intelligent analysis.

Flow:
1. Connect to Kafka topic 'system-events'
2. Read events as they arrive
3. (Future) Send to AI for analysis
4. (Future) Handle errors with retry/DLQ pattern
"""

from kafka import KafkaConsumer
import json
import time
from datetime import datetime


class EventConsumer:
    def __init__(self, bootstrap_servers=['localhost:9092']):
        self.topic = 'system-events'
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',  # Start from beginning if no offset
            enable_auto_commit=True,       # Auto-commit offsets
            group_id='ai-consumer-group',  # Consumer group name
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        
    def format_event(self, event):
        """Format event for display"""
        timestamp = datetime.fromtimestamp(event['timestamp'] / 1000)
        
        return f"""
{'='*60}
📅 Timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}
🔧 Service: {event['service_name']}
📍 Environment: {event['environment']}
⚠️  Event Type: {event['event_type']}
🚨 Severity: {event['severity']}
📝 Details: {event['details']}
{'='*60}
"""
    
    def run(self):
        """Start consuming events"""
        print(f"🚀 Starting consumer...")
        print(f"📖 Listening to topic: {self.topic}")
        print(f"👥 Consumer group: ai-consumer-group")
        print(f"⏳ Waiting for events...\n")
        
        try:
            for message in self.consumer:
                event = message.value
                
                # Display the event
                print(self.format_event(event))
                
                # TODO: Send to AI for analysis
                # TODO: Handle errors
                
        except KeyboardInterrupt:
            print("\n\n🛑 Shutting down consumer...")
        finally:
            self.consumer.close()
            print("✅ Consumer closed cleanly")


if __name__ == "__main__":
    consumer = EventConsumer()
    consumer.run()
