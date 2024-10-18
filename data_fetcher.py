import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')


def fetch_data(animal):
    """Fetches animal info from the API"""

    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal)  # API url targeting animals  name

    # get request
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

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
