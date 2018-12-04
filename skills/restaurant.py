import requests
import ava_api_keys as keys
import ava_settings as settings
import random

def get_restaurant(result,city_id,cuisines,establishments):
    cuisine_id = ""
    establishment_id = ""
    
    if(result['entities']):
        for entity in result['entities']:
            if entity == "cuisine":
                for cuisine in cuisines:
                    if cuisine["cuisine"]["cuisine_name"] == entity["value"]:
                        cuisine_id = cuisine["cuisine"]["cuisine_id"]
                        break
                if not cuisine_id:
                    for establishment in establishments:
                        if establishment["establishment"]["name"] == entity["value"]:
                            establishment_id = establishment["establishment"]["id"]

    if not cuisine_id or not establishment_id:
        cuisine_id = random.choice(cuisines)["cuisine"]["cuisine_id"]


    headers = {
    'Accept': 'application/json',
    'user-key': keys.ZOMATO_KEY,
    }

    params = (
        ('entity_id', city_id),
        ('entity_type', 'city'),
        ('cuisines', cuisine_id),
        ('establishment_type', establishment_id)
    )

    r = requests.get('https://developers.zomato.com/api/v2.1/search', headers=headers, params=params)
    restaurants = r.json()["restaurants"]
    
    pick = None
    locations = []
    if(result['entities']):
        for entity in result['entities']:
            if entity == "location":
                for restaurant in restaurants:
                    locality = restaurant["restaurant"]["location"]["locality_verbose"].split(",")
                    rating = restaurant["restaurant"]["user_rating"]["aggregate_rating"]
                    if entity["value"] in locality and rating > 3.0:
                        locations.append(restaurant)
                    elif(rating > 3.0):
                        locations.append(restaurant)
    
    if not locations:
        pick = random.choice(locations)
    else:
        pick = random.choice(restaurants)
        while pick["restaurant"]["user_rating"]["aggregate_rating"] < 3.0 :
            pick = random.choice(restaurants)
            
    options = [f"How about {pick['restaurant']['name']}? It's located in {pick['restaurant']['location']['locality']}",f"I found a {pick['restaurant']['user_rating']['aggregate_rating']}"]
    
    response = {
        "tts": random.choice(options),
        "file": "",
        "save": False,
    }
    return response

def get_city_id():
    headers = {
    'Accept': 'application/json',
    'user-key': keys.ZOMATO_KEY,
    }
    params = (
        ('q', settings.HOME_CITY),
        )
    response = requests.get('https://developers.zomato.com/api/v2.1/cities', headers=headers, params=params)
    data = response.json()
    return data["location_suggestions"][0]["id"]

def get_categories(city_id,endpoint):
    headers = {
    'Accept': 'application/json',
    'user-key': keys.ZOMATO_KEY,
    }

    params = (
        ('city_id',city_id),
    )
    url = f'https://developers.zomato.com/api/v2.1/{endpoint}'
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    return data[endpoint]