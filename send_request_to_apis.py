import requests

url = "http://127.0.0.1:5000/get_data_size/"

# max_size = 60
# min_size = 10
list_of_data_volumes = [1, 2, 3, 4, 5, 6]


def request_job(api_url, vol):
    response = requests.get(api_url + str(vol))
    return response


def send_bulk_request(data_volumes, api_url):
    responses = []
    for vol in data_volumes:
        current_response = request_job(api_url, vol)
        print(str(current_response) + str(vol))
        responses.append(current_response)
    return responses


if __name__ == "__main__":
    responses = send_bulk_request(list_of_data_volumes, url)
    print(responses)
