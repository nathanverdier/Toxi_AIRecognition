import requests
import os
import base64

from getToken import getToken

token_getter = getToken()
token = token_getter.get_token()

url = "https://codefirst.iut.uca.fr/containers/ToxiTeam-toxi-api/v1/person"

headers = {
    "Authorization": "Bearer " + token,
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    for item in data:
        if 'image' in item and 'name' in item:
            img_data = base64.b64decode(item['image'])
            image_path = f'codeIA/Images/{item["name"]}.jpg'
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            with open(image_path, 'wb') as f:
                f.write(img_data)
else:
    print(f"Request failed with status code {response.status_code}")