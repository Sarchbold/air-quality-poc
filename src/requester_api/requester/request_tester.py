""" Test area for functionality """

from request import Requester
import json

response = Requester("USA")
print(response.getsupportedstates())


# d = json.loads(response)
# df = pd.json_normalize(d["data"])
# print(df)
# getCountryData('Boston', 'MA', 'USA')
