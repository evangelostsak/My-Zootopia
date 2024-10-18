import requests
import json


def fetch_data(animal):
    """Fetches animal info from the API"""

    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal)  # API url targeting animals  name
    api_key = 'yDM/hllrax2UOLR6bqaiFQ==UOGJ66wUKFT0FkNH'
    # get request
    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:  # if code green, proceed!
        data = response.json()  # getting the response in json
        if len(data) == 0:  # Missing animal error fix
            return None
        return data
    else:
        print("Error:", response.status_code, response.json())
        return None


def load_data_json(file_path):
    """Loader for static json file"""
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File named '{file_path}' was not found")
        return None
