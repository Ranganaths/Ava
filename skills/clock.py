import datetime


def get_datetime(result):
    response = {
        "tts": "",
        "file": "",
        "save": False
    }
    if result['entities']:
        for entity in result['entities']:
            if entity["entity"] == "tempus":
                if entity["value"] == "time":
                    response["tts"] = f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}"
                    return response
                elif entity["value"] == "date":
                    response["tts"] = f"The current date is {datetime.datetime.now().strftime('%A %B %d')}"
                    return response
    response["tts"] = "I can't seem to find my calendar or watch."
