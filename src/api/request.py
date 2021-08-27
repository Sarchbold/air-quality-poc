"""
Send the request to the external API and return results
"""

import requests

def getSupportedStates(country):
    req = (
        "http://api.airvisual.com/v2/states?country="
        + country
        + "&key=14098954-5274-4969-b70a-c68fc6d522ca"
    )
    response = requests.get(req)
    print(response.text)
    print(req)


def getCountryData(city, state, country):
    req = (
        "http://api.airvisual.com/v2/city?city="
        + city
        + "&state="
        + state
        + "&country="
        + country
        + "&key=14098954-5274-4969-b70a-c68fc6d522ca"
    )
    response = requests.get(req)
    print(response.text)
    print(req)
