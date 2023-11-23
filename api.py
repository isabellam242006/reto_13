import json
import requests

url_1 = 'https://catfact.ninja/fact'

response_1 = requests.get(url_1)
cats = response_1.json()
print(cats)
print(list(cats.items()))

url_2 = 'https://www.boredapi.com/api/activity'
response_2 = requests.get(url_2)
bored = response_2.json()
print(bored)
print(list(bored.items()))

url_3 = 'https://api.genderize.io/?name=luc'
response_3 = requests.get(url_3)
genderize = response_3.json()
print(genderize)
print(list(genderize.items()))