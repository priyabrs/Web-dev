import requests

API_URL= 'https://api.npoint.io/718cdc0e6ee5a60c71d7'

def get_data_dict(api_url):
    response = requests.get(api_url)
    return response.json()


API_DATA = get_data_dict(API_URL)
# print(API_DATA)