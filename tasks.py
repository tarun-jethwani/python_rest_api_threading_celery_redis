from celery_config import app
from perform_job import read_n_write_data_to_db


@app.task
def send_task_in_rb_queue(data_vol):
    print("Task Recieved from Flask Rest Api")
    result = read_n_write_data_to_db(data_vol)
    return result
