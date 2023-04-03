#!/usr/bin/python3
"""
Python script that takes GitHub credentials
and uses the GitHub API to display the user id
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    reponse = requests.get(url, auth=auth.HTTPBasicAuth(user, password))
    print(reponse.json().get('id'))
