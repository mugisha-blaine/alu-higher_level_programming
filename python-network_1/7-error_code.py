#!/usr/bin/python3
"""
Python Script that takes in a URL, sends a request to the URL
n displays the body of the response"""
import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(argv[1])
    status = response.status_code
    print(response.text) if status < 400 else print(
        "Error code: {}".format(response.status_code))
