from flask import Flask, request
from perform_job import read_n_write_data_to_db
from threading import Thread
import threading

app = Flask(__name__)


def validate_api_param(param):
    pass


Job_Thread_Counter = []


@app.route("/get_data_size/<int:param>/")
def get_data_volume(param):
    global Job_Thread_Counter
    if request.method == "GET":
        curr_thread = Thread(target=read_n_write_data_to_db, args=(param,))
        Job_Thread_Counter.append(curr_thread)
        print(threading.enumerate())
        curr_thread.start()
        curr_thread.join()
        return "OK, job params received", 200

    else:
        return "Bad Request", 400


if __name__ == '__main__':
    app.run(debug=True)
