from skills import *
# The skill have been modularized for ease of reading. Each skill returns the result from a corresponding skills module in the skills package.
# Probably not best practice but this allowed for easy reading of what does what instead of having long hard to read files.


class AvaSkills():
    def __init__(self, city_id):
        # Get intial data necessary for some requests and keeping it in memory rather than repeating API calls. In future version a database will
        # be integrated to cache a lot of requests data so certain features continue to work offline from a cached version.

        self._zomato_city_id = restaurant.get_city_id()
        self._zomato_cuisines = restaurant.get_categories(
            self._zomato_city_id, "cuisines")
        self._zomato_establishments = restaurant.get_categories(
            self._zomato_city_id, "establishments")

    def get_datetime(self, result):
        # Returns either the current date or time according to user request.
        return clock.get_datetime(result)

    def get_dictionary(self, result):
        # Returns the definition of the word in user command.
        return dictionary.get_dictionary(result)

    def run_program(self, result):
        # Will open the program specified if found.
        return programs.run_program(result)

    def get_restaurant(self, result):
        # Returns a random restaurant exceeding minimum star quality from settings.
        return restaurant.get_restaurant(result, self._zomato_city_id, self._zomato_cuisines, self._zomato_establishments)

    def get_status(self, result):
        # Returns a random response from a list of responses to "How are you?" or similar questions.
        return salutations.get_status()

    def get_temperature(self, result):
        # Makes use of the get_weather with an extra paramenter source to return just the temperature.
        return self.get_weather(result=result, source="temperature")

    def get_thesaurus(self, result):
        # Returns either the antonym or synonym of a word provided by the user.
        return dictionary.get_thesaurus(result)

    def unit_conversion(self, result):
        # Returns the result of converting a unit to another unit. i.e ounces to pounds.
        return exchange.unit_conversion(result)

    def get_weather(self, result, source="weather"):
        # Returns the weather condition at the specified time or day.
        return weather.get_weather(result=result, source=source)
