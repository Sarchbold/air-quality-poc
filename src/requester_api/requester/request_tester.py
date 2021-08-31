""" Test area for functionality """

from request import Request
import json

response = Request("USA")
print(response.getsupportedstates())


# d = json.loads(response)
# df = pd.json_normalize(d["data"])
# print(df)
# getCountryData('Boston', 'MA', 'USA')
