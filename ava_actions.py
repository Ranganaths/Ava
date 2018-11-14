import ava_api_keys as keys
import ava_settings as settings
import requests
import dateparser
import datetime
import re


class AvaActions():
    def get_weather(self, result):
        weather = ""
        date = datetime.datetime.now()
        location = settings.HOME_ZIPCODE
        endpoint = "weather"
        method = "zip"
        response = {
            "tts": "",
            "file": ""
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
                if(endpoint == "forecast"):
                    for item in data["list"]:
                        parsed = dateparser.parse(
                            item["dt_txt"], settings={'TIMEZONE': 'UTC', 'TO_TIMEZONE': 'PST'})
                        if(parsed < date):
                            continue
                        else:
                            description = item["weather"][0]["description"]
                            temp = round(item["main"]["temp"])
                            response["tts"] = f"{description} with temperature around {temp}"
                            response["file"] = description.replace(
                                " ", "_") + f"_{temp}.mp3"
                            return response
                else:
                    description = data["weather"][0]["description"]
                    temp = round(data["main"]["temp"])
                    response["tts"] = f"{description} with temperature around {temp}"
                    response["file"] = description.replace(
                        " ", "_") + f"_{temp}.mp3"
                    return response
