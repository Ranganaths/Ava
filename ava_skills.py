from skills import *
# The skill have been modularized for ease of reading. Each skill returns the result from a corresponding skills module in the skills package.


class AvaSkills():
    def __init__(self, city_id):
        # Get intial data necessary for some requests and keeping it in memory rather than repeating API calls.

        self._zomato_city_id = restaurant.get_city_id()
        self._zomato_cuisines = restaurant.get_categories(
            self._zomato_city_id, "cuisines")
        self._zomato_establishments = restaurant.get_categories(
            self._zomato_city_id, "establishments")

    def get_datetime(self, result):
        return clock.get_datetime(result)

    def get_dictionary(self, result):
        return dictionary.get_dictionary(result)

    def run_program(self, result):
        return programs.run_program(result)

    def get_restaurant(self, result):
        return restaurant.get_restaurant(result, self._zomato_city_id, self._zomato_cuisines, self._zomato_establishments)

    def get_status(self, result):
        return salutations.get_status()

    def get_temperature(self, result):
        # get_temperature is an extention of the get_weather action. Rather than create a new similar function
        # we can can call get_weather with an extra parameter that will allow get_weather to return the appropriate
        # values based on who the original caller was.
        return self.get_weather(result=result, source="temperature")

    def get_thesaurus(self, result):
        return dictionary.get_thesaurus(result)

    def get_weather(self, result, source="weather"):
        # Returns the results of the weather module in the skills package.
        return weather.get_weather(result=result, source=source)
