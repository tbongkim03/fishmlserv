import requests

def get(l, w, url='http://localhost:8765/fish'):
    headers = {
        'accept': 'application/json',
    }
    params = {
        'length': l,
        'weight': w,
    }

    response = requests.get('http://localhost:8765/fish', params=params, headers=headers)
    j = response.json()
    result = j.get("prediction")

    return result
