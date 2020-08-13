# Please complete the TODO items in this code
import asyncio 
from confluent_kafka import Consumer
from confluent_kafka.admin import AdminClient, NewTopic

BROKER_URL = 'PLAINTEXT://localhost:9092'

async def produce_consume(topic_name):
    """Consumes data from the Kafka Topic"""
    c = Consumer({"bootstrap.servers": BROKER_URL, "group.id": "0"})
    c.subscribe([topic_name])
    
    while True:
        message = c.poll(1.0)
        if not message:
            print("no message received by consumer")
        elif message.error():
            print(f"error from consumer {message.error()}")
        else:
            print(f"consumed message {message.key()}: {message.value()}")
        await asyncio.sleep(0.1)
    
def main():
    try:
        asyncio.run(produce_consume("sfcs.summary"))
    except KeyboardInterrupt as e:
        print("shutting down")

if __name__ == '__main__':
    main()