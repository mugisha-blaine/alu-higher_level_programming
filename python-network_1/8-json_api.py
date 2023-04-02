#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
with the letter as a parameter
"""
import requests
from sys import argv

if __name__ == '__main__':
    q = argv[1] if len(argv) == 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': q})
    try:
        respo_dict = response.json()
        id, name = respo_dict.get('id'), respo_dict.get('name')
        if len(respo_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(respo_dict.get('id')\
            , respo_dict.get('name')))
    except:
        print("Not a valid JSON")
