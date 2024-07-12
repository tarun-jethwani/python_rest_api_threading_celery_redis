from flask import Flask, request
from tasks import send_task_in_rb_queue

app = Flask(__name__)


def validate_api_param(param):
    pass


@app.route("/get_data_size/<int:param>/")
def get_data_volume(param):
    if request.method == "GET":
        result = send_task_in_rb_queue.delay(param)
        print(result)
        return "OK, job params received", 200

    else:
        return "Bad Request", 400


if __name__ == '__main__':
    app.run(debug=True)
