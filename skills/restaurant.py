import requests
import ava_api_keys as keys
import ava_settings as settings
import random


def get_restaurant(result, city_id, cuisines, establishments):
    cuisine_id = ""
    establishment_id = ""
    response = {
        "tts": "",
        "file": "",
        "save": False,
    }
    # Get the corresponding ID that matches our entity value for cuisine
    if(result['entities']):
        for entity in result['entities']:
            if entity["entity"] == "cuisine":
                for cuisine in cuisines:
                    if cuisine["cuisine"]["cuisine_name"] == entity["value"]:
                        cuisine_id = cuisine["cuisine"]["cuisine_id"]
                        break
                if not cuisine_id:
                    for establishment in establishments:
                        if establishment["establishment"]["name"] == entity["value"]:
                            establishment_id = establishment["establishment"]["id"]
    # If no ID was found to match then the entity didn't exist and a random selection can be made.
    if not cuisine_id and not establishment_id and not next((item for item in result["entities"] if item["entity"] == "cuisine"), True):
        response["tts"] = "I was not able to extract the cuisine from your command."
        response["file"] = "cuisine_entity_failure.mp3"
        response["save"] = True
        return response

    elif not cuisine_id and not establishment_id:
        cuisine_id = random.choice(cuisines)["cuisine"]["cuisine_id"]

    # Formulate the headers and paramaters needed to create a request to the Zomato API and then retrieve the data. If request fails the corresponding exception is used for a response.

    headers = {
        'Accept': 'application/json',
        'user-key': keys.ZOMATO_KEY,
    }

    params = (
        ('entity_id', city_id),
        ('entity_type', 'city'),
        ('cuisines', cuisine_id),
        ('establishment_type', establishment_id),
        ('sort', 'rating'),
        ('order', 'desc')
    )

    try:
        r = requests.get(
            'https://developers.zomato.com/api/v2.1/search', headers=headers, params=params)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("HTTP_ERROR: ", errh)
        response["tts"] = "Apologies, it seems a bad request was made to the Zomato API."
        response["file"] = "bad_zomato_request.mp3"
        response["save"] = True
        return response
    except requests.exceptions.ConnectionError as errc:
        print("CONNECTION_ERROR: ", errc)
        response["tts"] = "There appears to be a network error. I was unable to connect to the Zomato API."
        response["file"] = "bad_zomato_connection.mp3"
        response["save"] = True
        return response
    except requests.exceptions.Timeout as errt:
        print("TIMEOUT_ERROR: ", errt)
        response["tts"] = "I was unable to to get the answer for you. The request to the Zomato API timed out."
        response["file"] = "zomato_timeout.mp3"
        response["save"] = True
        return response
    except requests.exceptions.RequestException as err:
        print("UNKOWN_ERROR", err)
        response["tts"] = "I'm sorry but I was unable to get the weather for you. An unkown error occured. "
        response["file"] = "bad_zomato_request.mp3"
        response["save"] = True
        return response
    else:
        try:
            restaurants = r.json()["restaurants"]
        except Exception as e:
            print("Error in getting json from Zomato api response...")
        else:
            # Parse the the returned JSON data which is very nested hence a lot of key value notation. Create a new list that match criteria of locality and or minimum rating.
            pick = None
            locations = []
            if(result['entities']):
                for entity in result['entities']:
                    if entity == "location":
                        for restaurant in restaurants:
                            locality = restaurant["restaurant"]["location"]["locality_verbose"].split(
                                ",")
                            rating = float(
                                restaurant["restaurant"]["user_rating"]["aggregate_rating"])
                            if entity["value"] in locality and rating >= settings.MINIMUM_RESTAURANT_RATING:
                                locations.append(restaurant)
                            elif(rating > settings.MINIMUM_RESTAURANT_RATING):
                                locations.append(restaurant)
            # An empty locations list indicates no matching entities therefor we can randomly select a location from the restaurants list.
            # In order to not creat an infinite loop when trying to match for >= than minimum rating we create a new list of just results >= than minimum rating.
            if locations:
                pick = random.choice(locations)
            else:
                restaurants = [item for item in restaurants if float(
                    item["restaurant"]["user_rating"]["aggregate_rating"]) >= settings.MINIMUM_RESTAURANT_RATING]
                pick = random.choice(restaurants)

            if not pick:
                response["tts"] = "I'm sorry, but none of the results matched your criteria."
                return response

            options = [f"How about {pick['restaurant']['name']} in {pick['restaurant']['location']['locality']}",
                       f"I found a {pick['restaurant']['user_rating']['aggregate_rating']} rating restaurant named {pick['restaurant']['name']}. It's located in {pick['restaurant']['location']['locality']} ",
                       f"{pick['restaurant']['name']} sounds like a real winner.",
                       f"Why not give {pick['restaurant']['name']} a go?",
                       f"{pick['restaurant']['name']} has {pick['restaurant']['user_rating']['aggregate_rating']} stars. Give it a try!"]

            response["tts"] = random.choice(options)
            return response
        response["tts"] = "I'm sorry, but none of the results matched your criteria."
        response["file"] = "restaurant_no_criteria_match.mp3"
        response["save"] = True
        return response


def get_city_id():
    headers = {
        'Accept': 'application/json',
        'user-key': keys.ZOMATO_KEY,
    }
    params = (
        ('q', settings.HOME_CITY),
    )
    response = requests.get(
        'https://developers.zomato.com/api/v2.1/cities', headers=headers, params=params)
    data = response.json()
    return data["location_suggestions"][0]["id"]


def get_categories(city_id, endpoint):
    headers = {
        'Accept': 'application/json',
        'user-key': keys.ZOMATO_KEY,
    }

    params = (
        ('city_id', city_id),
    )
    url = f'https://developers.zomato.com/api/v2.1/{endpoint}'
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    return data[endpoint]
