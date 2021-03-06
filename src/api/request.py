"""
Send the request to the external API and return results
"""
import pandas as pd
from urllib.request import urlopen
import json


def getsupportedstates(country):

    req = (
        "http://api.airvisual.com/v2/states?country="
        + country
        + "&key=<getkey>"
    )
    response = urlopen(req)
    json_data = response.read().decode("utf-8", "replace")
    return json_data


def getcountrydata(city, state, country):
    req = (
        "http://api.airvisual.com/v2/city?city="
        + city
        + "&state="
        + state
        + "&country="
        + country
        + "&key=<getkey>"
    )
    response = urlopen(req)
    json_data = response.read().decode("utf-8", "replace")
    return json_data
