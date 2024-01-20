# utils.py

import requests


def get_access_token():
    url = "https://mls-router1.p.rapidapi.com/cognito-oauth2/token"

    payload = {
        "client_id": "118po0r6i1o1ccsu6ee4cl132u",
        "grant_type": "client_credentials",
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "x-rapidapi-key": "52d03659f5mshde22d1aee3d427cp1154eajsn60129072a38e",
        "x-rapidapi-host": "mls-router1.p.rapidapi.com",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.json().get("access_token")

def fetch_property_data(access_token):
    url = "https://mls-router1.p.rapidapi.com/reso/odata/Property"
    querystring = {"orderby": "ModificationTimestamp desc", "top": "5"}

    headers = {
        "Authorization": access_token,
        "x-api-key": "a50YsdAcOQ6xyDqVYTzEB57jBqKVYV01MyTD4at6",
        "X-RapidAPI-Key": "52d03659f5mshde22d1aee3d427cp1154eajsn60129072a38e",
        "X-RapidAPI-Host": "mls-router1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

# Get access token
access_token = get_access_token()

# Fetch property data using the access token
if access_token:
    property_data = fetch_property_data(access_token)
    print(property_data)
else:
    print("Failed to get access token")


# def fetch_realty_data(*args, **kwargs):
#     url = "https://realty-in-ca1.p.rapidapi.com/properties/v2/list-for-sale"
    
#     querystring = {
#         "ReferenceNumber": kwargs.get("reference_number"),
#         "CultureId": kwargs.get("culture_id"),
#     }


#     for key, value in kwargs.items():
#         if key in ["min_list_price", "max_list_price", "bedrooms", "bathrooms"]:
#             querystring[key.capitalize()] = value

#     headers = {
#         "X-RapidAPI-Key": "52d03659f5mshde22d1aee3d427cp1154eajsn60129072a38e",
#         "X-RapidAPI-Host": "realty-in-ca1.p.rapidapi.com",
#     }

#     response = requests.get(url, headers=headers, params=querystring)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None

# def fetch_new_listings():
#     url = "https://realty-in-ca1.p.rapidapi.com/properties/v2/list-for-sale"

#     querystring = {"Page": "1", "PageSize": "10", "CultureId": "1"}

#     headers = {
#         "X-RapidAPI-Key": "52d03659f5mshde22d1aee3d427cp1154eajsn60129072a38e",
#         "X-RapidAPI-Host": "realty-in-ca1.p.rapidapi.com",
#     }

#     response = requests.get(url, headers=headers, params=querystring)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None