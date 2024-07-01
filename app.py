from flask import Flask, request
from perform_job import read_n_write_data_to_db

app = Flask(__name__)


def validate_api_param(param):
    pass


@app.route("/get_data_size/<int:param>/")
def get_data_volume(param):
    messages = []
    if request.method == "GET":
        messages.append(read_n_write_data_to_db(param))
        print(messages)
        return "OK, job params received", 200

    else:
        return "Bad Request", 400


if __name__ == '__main__':
    app.run(debug=True)
