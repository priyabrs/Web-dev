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

def blog():
    response = requests.get('https://api.npoint.io/5cb4231037a3aebb3a2c')
    return response.json()
# guess_gender('Andy')
# blog()