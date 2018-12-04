import ava_api_keys as keys
import ava_settings as settings
from pyjarowinkler import distance as jarowinkler
import os


def run_program(result):
    program_path = ""
    found = False
    response = {
        "tts": "",
        "file": "",
        "save": False,
    }
    if result['entities']:
        for entity in result['entities']:
            if entity["entity"] == "program":
                for subdir, dirs, files in os.walk(settings.PROGRAMS_DIR1):
                    for file in files:
                        if(entity["value"] in file and jarowinkler.get_jaro_distance(entity["value"], file, winkler=True) > 0.8):
                            program_path = subdir + "/" + file
                            found = True
                            break
                    if(found):
                        break

                if not program_path:
                    for subdir, dirs, files in os.walk(settings.PROGRAMS_DIR2):
                        for file in files:
                            if(entity["value"] in file and jarowinkler.get_jaro_distance(entity["value"], file, winkler=True) > 0.8):
                                program_path = subdir + "/" + file
                                found = True
                                break
                        if(found):
                            break
    if not program_path:
        response["tts"] = "I was unable to find the program you wanted. It may not be in the start programs directory."
        response["file"] = "program_not_found.mp3"
        response["save"] = True
        return response

    response["tts"] = "Ok"
    response["file"] = "ok.mp3"
    response["save"] = True
    print(f"Opening path {program_path}")
    os.startfile(program_path)

    return response
