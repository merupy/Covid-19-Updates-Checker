import requests
import json

def covid_nepal():
    url = 'https://api.covid19api.com/country/nepal'
    r = requests.get(url)
    con_json = r.json()
    a = con_json[-1]
    for x,y in a.items():
        print (str(x) + ' : ' +str(y))

def covid_international():
    url = 'https://api.covid19api.com/summary'
    r = requests.get(url)
    con_json = json.loads(r.text)
    a = con_json['Global']
    for x,y in a.items():
        print (str(x) + ' : ' +str(y))

