import time
from concurrent.futures import ThreadPoolExecutor, as_completed
# from celery import Celery
from celery import current_app
from perform_job import read_n_write_data_to_db
import pika
import json


# app = Celery('tasks', broker='pyamqp://guest@localhost//')


# def fetch_and_process_tasks():
#     with ThreadPoolExecutor(max_workers=4) as executor:
#         while True:
#             results = app.AsyncResult()
#             futures = [executor.submit(read_n_write_data_to_db, result) for result in results]
#             for future in as_completed(futures):
#                 try:
#                     future.result()
#                 except Exception as e:
#                     print(f"Task failed: {e}")
#             time.sleep(1)




def fetch_task():
    # Connect to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declare the queue; it should match Celery's default queue name
    queue_name = 'tasks'
    channel.queue_declare(queue=queue_name, durable=True)

    # Fetch task from the RabbitMQ queue
    method_frame, header_frame, body = channel.basic_get(queue=queue_name)

    if method_frame:
        # Acknowledge the message to remove it from the queue
        channel.basic_ack(method_frame.delivery_tag)

        # Decode the task message
        task_data = json.loads(body)
        print("Fetched task:", task_data)
        connection.close()
        return task_data
    else:
        print("No tasks in the queue")
        connection.close()
        return None



def worker(task):
    result = task()
    read_n_write_data_to_db(result)
    print(f'Processed task with result: {result}')


def fetch_and_process_tasks():
    with ThreadPoolExecutor(max_workers=4) as executor:
        while True:
            task = fetch_task()
            if task:
                executor.submit(worker, task)


if __name__ == "__main__":
    fetch_and_process_tasks()
