# utils.py

import requests

def fetch_realty_data(*args, **kwargs):
    url = "https://realty-in-ca1.p.rapidapi.com/properties/v2/list-for-sale"
    
    querystring = {
        "ReferenceNumber": kwargs.get("reference_number"),
        "CultureId": kwargs.get("culture_id"),
    }


    for key, value in kwargs.items():
        if key in ["min_list_price", "max_list_price", "bedrooms", "bathrooms"]:
            querystring[key.capitalize()] = value

    headers = {
        "X-RapidAPI-Key": "52d03659f5mshde22d1aee3d427cp1154eajsn60129072a38e",
        "X-RapidAPI-Host": "realty-in-ca1.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def fetch_new_listings():
    url = "https://realty-in-ca1.p.rapidapi.com/properties/v2/list-for-sale"

    querystring = {"Page": "1", "PageSize": "10", "CultureId": "1"}

    headers = {
        "X-RapidAPI-Key": "52d03659f5mshde22d1aee3d427cp1154eajsn60129072a38e",
        "X-RapidAPI-Host": "realty-in-ca1.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        return None