from celery_config import app


@app.task
def send_task_in_queue(data_vol):
    print("Task Recieved from Flask Rest Api")
    return data_vol
