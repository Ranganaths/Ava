import ava_api_keys as keys
import ava_settings as settings
import requests
import dateparser
import datetime
import re


class AvaSkills():
    def get_weather(self, result, source="weather"):
        # Makes use of the Open Weather Map to retrieve weather data. The function has
        # default parameters that will get modified depending on the entities result received
        # from the calling entity processing function. A variable source is added to allow
        # get_temperature to use the same function as they are only differ on the return statement.
        # With the source variable set we know the calling function is get_temperature and can
        # conditionally change the return to just temperature data.

        weather = ""
        date = datetime.datetime.now()
        location = settings.HOME_ZIPCODE
        endpoint = "weather"
        method = "zip"
        response = {
            "tts": "",
            "file": "",
            "save": True,
        }
        if(result['entities']):
            for entity in result['entities']:
                if(entity['entity'] == "weather"):
                    weather = entity['value']
                if(entity['entity'] == "location"):
                    if(not re.search(r"\d{5}", entity['value'])):
                        method = "q"
                    location = entity['value'].replace(" ", "")
                if(entity['entity'] == "time"):
                    try:
                        date = dateparser.parse(entity['value'], settings={
                                                'PREFER_DATES_FROM': 'future'})
                        if(date.date() > datetime.datetime.now().date()):
                            endpoint = "forecast"
                    except Exception as e:
                        print("Error parsing date: ", e)
        url = f"https://api.openweathermap.org/data/2.5/{endpoint}?{method}={location},{settings.HOME_COUNTRY_CODE}&units=imperial&appid={keys.OWM_DEFAULT_KEY}"
        try:
            print(f"URL: {url}")
            r = requests.get(url, timeout=5)
            r.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print("HTTP_ERROR: ", errh)
            response["tts"] = "Apologies, it seems a bad request was made to the weather API."
            response["file"] = "bad_weatherapi_request.mp3"
            return response
        except requests.exceptions.ConnectionError as errc:
            print("CONNECTION_ERROR: ", errc)
            response["tts"] = "There appears to be a network error. I was unable to connect to the weather API."
            response["file"] = "bad_weatherapi_connection.mp3"
            return response
        except requests.exceptions.Timeout as errt:
            print("TIMEOUT_ERROR: ", errt)
            response["tts"] = "I was unable to to get the answer for you. The request to the weather API timed out."
            response["file"] = "weatherapi_timeout.mp3"
            return response
        except requests.exceptions.RequestException as err:
            print("UNKOWN_ERROR", err)
            response["tts"] = "I'm sorry but I was unable to get the weather for you. An unkown error occured. "
            response["file"] = "bad_weather_request.mp3"
            return response
        else:
            try:
                data = r.json()
            except Exception as e:
                print("Error in getting json from weather api response...")
            else:
                # Forecast endpoint vs Weather endpoint return differently structured data. Therefor we need to conditionally
                # set our return response based on which API endpoint was hit. The forecast endpoint requires looping through
                # a lit to get the appopriate weather forecast item that corresponds to the correct date reuqested by the user.

                if(endpoint == "forecast"):
                    for item in data["list"]:
                        parsed = dateparser.parse(
                            item["dt_txt"], settings={'TIMEZONE': 'UTC', 'TO_TIMEZONE': 'PST'})
                        if(parsed < date):
                            continue
                        else:
                            if(source == "temperature"):
                                temp = round(item["main"]["temp"])
                                response["tts"] = f"The forecasted temperature is {temp} degrees"
                                response["file"] = f"forecast_temperature_{temp}.mp3"
                                return response

                            description = item["weather"][0]["description"]
                            temp = round(item["main"]["temp"])
                            response["tts"] = f"Forecast: {description} with temperature around {temp} degrees"
                            response["file"] = "forecast_" + description.replace(
                                " ", "_") + f"_{temp}.mp3"
                            return response
                else:
                    if(source == "temperature"):
                        temp = round(data["main"]["temp"])
                        response["tts"] = f"The temperature is around {temp} degrees"
                        response["file"] = f"temperature_{temp}.mp3"
                        return response
                    description = data["weather"][0]["description"]
                    temp = round(data["main"]["temp"])
                    response["tts"] = f"Looks like {description} with temperature around {temp} degrees"
                    response["file"] = description.replace(
                        " ", "_") + f"_{temp}.mp3"
                    return response

    def get_temperature(self, result):
        # get_temperature is an extention of the get_weather action. Rather than create a new similar function
        # we can can call get_weather with an extra parameter that will allow get_weather to return the appropriate
        # values based on who the original caller was.
        return self.get_weather(result, "temperature")

    def get_restaurant(self, result):

        # Get_restaurants makes use of Zomato API for restaurant searching. Zomato API requires multiple requests to first
        # get the location id and then from the location id to get categorie id's and from there get the restaurant id's before
        # finally being able to get the restaurant details. That's a lot. A lot of the data for categories and city id can just be
        # stored. Additional restaurant data can then be used via requests. Get_restaurants will make use of TinyDB for a simple
        # document based database. The database will be used if its present or created if it hasn't been already. The initial requests
        # will use the settings location information to retrive and store the data related to the user city.

        headers = {
            "Accept": "application/json",
            "user-key": keys.ZOMATO_KEY,
            "entity-id": "",
            "res_id": "",
        }
        category = ""

        url = f'https://developers.zomato.com/api/v2.1/{category}'

        r = requests.get(url=url, headers=headers)

    def get_time(self, result):
        return {
            "tts": f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}",
            "file": "time.mp3",
            "save": False
        }
