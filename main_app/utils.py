# utils.py

import requests

def fetch_realty_data(reference_number, culture_id):
    url = "https://realty-in-ca1.p.rapidapi.com/properties/list-by-mls"

    querystring = {
        "ReferenceNumber": reference_number,
        "CultureId": culture_id,
    }

    headers = {
        "X-RapidAPI-Key": "52d03659f5mshde22d1aee3d427cp1154eajsn60129072a38e",
        "X-RapidAPI-Host": "realty-in-ca1.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        return None
