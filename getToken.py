import requests
import json

class getToken:
    def __init__(self):
        self.url = "https://dev-3ja73wpfp1j6uzed.us.auth0.com/oauth/token"

        self.payload = {
            "client_id": "eAf8z4vS3B47LGatTn34q38IRdJrNNvc",
            "client_secret": "n_oChtKZlpXG60n-N1V4LwXkaFYbvRGoWT-4Lsk8nwPo3aXIEONevoHUa8uMEN4g",
            "audience": "https://toxiapi/",
            "grant_type": "client_credentials"
        }

        self.headers = {
            'content-type': "application/json"
        }

    def get_token(self):
        response = requests.post(self.url, data=json.dumps(self.payload), headers=self.headers)

        if response.status_code == 200:
            return response.json()['access_token']
        else:
            print(f"Request failed with status code {response.status_code}")
            return None