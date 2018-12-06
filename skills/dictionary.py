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
        if category in "antonyms" or category in "opposites":
            antonym = _antonyms(lookup)
            if antonym:
                response["tts"] = f"{category} of {lookup} is {random.choice(antonym)}"
                return response
        elif(category in "synonyms"):
            synonym = _antonyms(lookup)
            if synonym:
                response["tts"] = f"{category} of {lookup} is {random.choice(synonym)}"
                return response
    response["tts"] = "I'm sorry but I was unable to look that up."
    response["file"] = "lookup_not_found.mp3"
    response["save"] = True
    return response


def _definition(word):
    return wn.synsets(word)[0].definition()


def _synonyms(word):
    return [lem for synset in wn.synsets(word) for lem in synset.lemma_names() if lem != word]


def _antonyms(word):
    return tuple(set(antonym.name() for synset in wn.synsets(word) for lem in synset.lemmas() for antonym in lem.antonyms()))
