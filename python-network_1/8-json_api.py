#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
with the letter as a parameter"""
import requests
from sys import argv

if __name__ == '__main__':
    q = argv[1] if len(argv) == 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': q})
    try:
        res_dict = response.json()
        id, name = res_dict.get('id'), res_dict.get('name')
        if len(res_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(res_dict.get('id'), res_dict.get('name')))
    except:
        print("Not a valid JSON")
