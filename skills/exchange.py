from pint import UnitRegistry
from pint import DimensionalityError, UndefinedUnitError


def unit_conversion(result):
    data = _get_entities(result)
    response = {
        "tts": "",
        "file": "",
        "save": True,
    }
    if data:
        units = UnitRegistry()
        units.default_format = '.2f'
        base = data["base"]
        conversion = data["conversion"]
        try:
            amount = data["amount"] * units(input_string=base)
        except UndefinedUnitError as e:
            response["tts"] = "The base unit does not appear to be in the unit registry."
            response["file"] = "base_unit_undefined.mp3"
        else:
            try:
                result = amount.to(conversion)
            except DimensionalityError as e:
                response["tts"] = f"I can't conver the base unit to the conversion unit."
                response["file"] = "conversion_dimensionality.mp3"
            except UndefinedUnitError as e:
                response["tts"] = "The conversion unit does not appear to be in the unit registry."
                response["file"] = "conversion_unit_undefined.mp3"
            else:
                response["tts"] = f"{amount} is {result}"
                response["save"] = False
        return response
    response["tts"] = "I wasn't able to convert those units."
    response["file"] = "conversion_failure.mp3"
    return response


def _get_entities(result):
    data = {
        "amount": 1.0
    }
    if result['entities']:
        for entity in result['entities']:
            if entity["entity"] == "amount":
                data["amount"] = float(entity["value"])

            if entity["entity"] == "base":
                data["base"] = entity["value"].lower()

            if entity["entity"] == "conversion":
                data["conversion"] = entity["value"].lower()
    return data
