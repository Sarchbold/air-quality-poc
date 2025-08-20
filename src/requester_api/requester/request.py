"""
Send the request to the external API and return results
"""

from urllib.request import urlopen


class Request:
    def __init__(self, country):
        self.country = country

    def getsupportedstates(self):
        req = (
            "http://api.airvisual.com/v2/states?country=" + self.country + "&key=<key>"
        )
        response = urlopen(req)
        json_data = response.read().decode("utf-8", "replace")
        return json_data

    # def getcountrydata(city, state, country):
    #     req = (
    #             "http://api.airvisual.com/v2/city?city="
    #             + city
    #             + "&state="
    #             + state
    #             + "&country="
    #             + country
    #             + "&key=<key>"
    #     )
    #     response = urlopen(req)
    #     json_data = response.read().decode("utf-8", "replace")
    #     return json_data
