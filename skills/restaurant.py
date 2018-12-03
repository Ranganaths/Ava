import requests


def get_restaurant(result):
    headers = {
        "Accept": "application/json",
        "user-key": keys.ZOMATO_KEY,
        "entity-id": "",
        "res_id": "",
    }
    category = ""

    url = f'https://developers.zomato.com/api/v2.1/{category}'

    r = requests.get(url=url, headers=headers)
