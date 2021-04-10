from ast import Param
from urllib import response
import requests


def guess_gender(user_name):
    query = {'name':user_name}
    response = requests.get('https://api.genderize.io/', params=query)
    return response.json()['gender']

def guess_age(user_name):
    query = {'name':user_name}
    response = requests.get('https://api.agify.io/', params=query)
    return response.json()['age']
# guess_gender('Andy')