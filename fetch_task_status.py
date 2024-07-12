from celery import result
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

app.conf.update(
    result_backend='rpc://',
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    worker_concurrency=2,
    timezone='UTC',
    enable_utc=True,
)

TASK_LIST = ['a4a9e896-db53-4b18-a633-ae03248991fe',
             '56863d46-1844-4f26-b1a0-d3e2038ba5c3',
             '80fd3110-0a7c-4020-b819-87a43b1e3d9f',
             'a8dd8df3-bf4f-4259-ab13-15a48a9aff22',
             '27b9f1cd-69de-4999-be39-05bc06a423b5',
             '8ff0013e-95e4-464b-a393-6258fd151258'
             ]

for task_id in TASK_LIST:
    res = result.AsyncResult(id=task_id, app=app)
    print(res.status)