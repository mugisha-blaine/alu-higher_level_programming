#!/usr/bin/python3
"""script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""


import sys
import requests
username = sys.argv[1]
password = sys.argv[2]
url = 'https://api.github.com/user'
headers = {'Authorization': 'Basic ' + (username + ':' + password).encode('base64').rstrip()}
reponse = requests.get(url, headers)
user_id = reponse.json()['id']
print(user_id)
