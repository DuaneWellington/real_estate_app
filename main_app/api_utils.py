# real_estate_django/main_app/api_utils.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

REALTYNA_CLIENT_ID = os.getenv("REALTYNA_CLIENT_ID")
REALTYNA_CLIENT_SECRET = os.getenv("REALTYNA_CLIENT_SECRET")
REALTYNA_GRANT_TYPE = os.getenv("REALTYNA_GRANT_TYPE")

def get_dynamic_authorization():
    # API endpoint for obtaining access token
    token_url = "https://mls-router1.p.rapidapi.com/cognito-oauth2/token"

    # Credentials provided by Realtyna
    client_id = os.getenv("REALTYNA_CLIENT_ID")
    client_secret = os.getenv("REALTYNA_CLIENT_SECRET")
    grant_type = os.getenv("REALTYNA_GRANT_TYPE")

    # Request body parameters
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": grant_type
    }

    try:
        # Send POST request to obtain access token
        response = requests.post(token_url, data=data)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes

        # Parse JSON response
        json_response = response.json()

        # Extract and return access token
        access_token = json_response.get("access_token")
        return access_token

    except requests.exceptions.RequestException as e:
        # Handle request exceptions (e.g., connection error, timeout)
        print(f"Error obtaining access token: {e}")
        return None

# Usage example
access_token = get_dynamic_authorization()
print(access_token)
