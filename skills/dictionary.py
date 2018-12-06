from nltk.corpus import wordnet as wn
import random

def get_dictionary(result):
    response = {
        "tts": "",
        "file": "",
        "save": False,
    }
    if result['entities']:
        for entity in result['entities']:
            if entity["entity"] == "key":
                definition = _definition(entity["value"])
                response["tts"] = f"{entity['value']}: {definition}"
                return response
    response["tts"] = "I'm sorry but I was unable to look that up."
    response["file"] = "lookup_not_found.mp3"
    response["save"] = True
    return response


def get_thesaurus(result):
    response = {
        "tts": "",
        "file": "",
        "save": False,
    }
    lookup = ""
    category = ""

    if result['entities']:
        for entity in result['entities']:
            if entity["entity"] == "key":
                lookup = entity["value"]
            if entity["entity"] == "type":
                category = entity["value"]
    
    if lookup and category:
        if category == "antonym" or category == "opposite":
            antonym = _antonyms(lookup)
            response["tts"] = f"An {category} of {lookup} is {random.choice(antonym)}"
            return response
        response["tts"] = "I'm sorry but I was unable to get that definition."
    response["tts"] = "I'm sorry but I was unable to look that up."
    response["file"] = "lookup_not_found.mp3"
    response["save"] = True
    return response



def _definition(word):
    return wn.synsets(word)[0].definition()


def _synonyms(word):
    return [lem for synset in wn.synsets(word) for lem in synset.lemma_names() if lem != word]


def _antonyms(word):
    antonyms = [antonym.name() for synset in wn.synsets(word) for lem in synset.lemmas() for antonym in lem.antonyms()]
    return set(antonyms)
