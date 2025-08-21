"""Test area for functionality"""

from src.requester_api.requester.request import Request

response = Request("USA")
print(response.getsupportedstates())


# d = json.loads(response)
# df = pd.json_normalize(d["data"])
# print(df)
# getCountryData('Boston', 'MA', 'USA')
