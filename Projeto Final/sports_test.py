import requests
import json

uri = 'https://api.football-data.org/v4/matches'
headers = { 'X-Auth-Token': '8d6f101a236f4c6a8579c90caaabc378' }

response = requests.get(uri, headers=headers)
match = response.json()['matches'][0]
