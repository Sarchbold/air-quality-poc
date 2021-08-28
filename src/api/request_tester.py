""" Test area for functionality """

from request import *
import json

response = getsupportedstates("USA", "raw")
print(response)

response = getsupportedstates("USA", "json")
print(response)

# d = json.loads(response)
# df = pd.json_normalize(d["data"])
# print(df)
# getCountryData('Boston', 'MA', 'USA')
