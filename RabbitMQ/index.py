import pika
import threading

def publish_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='test_queue')

    for i in range(10000000):
        channel.basic_publish(exchange='', routing_key='test_queue', body=f'Hello World! User {i}')
    connection.close()
    print(" [x] Tüm mesajlar gönderildi.")

def consume_worker(thread_id):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='test_queue')

    def callback(ch, method, properties, body):
        print(f" [x] Thread {thread_id} received {body}")

    channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)
    print(f" [*] Thread {thread_id} mesajları dinlemeye başladı.")
    channel.start_consuming()

def start_consumers(num_threads):
    max_threads = 4
    if num_threads > max_threads:
        num_threads = max_threads

    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=consume_worker, args=(i+1,))
        t.start()
        threads.append(t)

    # Tüketiciler sürekli çalıştığı için join yapmıyoruz

if __name__ == "__main__":
    # Publish işlemini thread olarak başlat
    producer_thread = threading.Thread(target=publish_messages)
    producer_thread.start()

    # Aynı anda tüketicileri başlat
    start_consumers(4)

    # Publish thread'in bitmesini bekle (isteğe bağlı)
    producer_thread.join()