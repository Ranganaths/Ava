import datetime


def get_time(result):
    return {
        "tts": f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}",
        "file": "time.mp3",
        "save": False
    }
