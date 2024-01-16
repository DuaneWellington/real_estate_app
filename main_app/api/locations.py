import requests

base_url = "https://realty-in-ca1.p.rapidapi.com/"
endpoint = "locations/v2/auto-complete"

params = {
    "query": {"Query":"Quebec","CultureId":"1","IncludeLocations":"true"},
    "api_key": "52d03659f5mshde22d1aee3d427cp1154eajsn60129072a38e",
}

response = requests.get(base_url + endpoint, params=params)
data = response.json()