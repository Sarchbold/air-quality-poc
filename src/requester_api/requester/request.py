"""
Send the request to the external API and return results
"""
import pandas as pd
from urllib.request import urlopen
import json


class Requester:
    def __init__(self, country):
        self.country = country

    def getsupportedstates(self):
        req = (
                "http://api.airvisual.com/v2/states?country="
                + self.country
                + "&key=<getkey>"
        )
        response = urlopen(req)
        json_data = response.read().decode("utf-8", "replace")
        return json_data
