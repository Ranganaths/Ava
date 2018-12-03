from skills import *
# The skill have been modularized for ease of reading. Each skill returns the result from a corresponding skills module in the skills package.


class AvaSkills():
    def get_weather(self, result, source="weather"):
        # Returns the results of the weather module in the skills package.
        return weather.get_weather(result=result, source=source)

    def get_temperature(self, result):
        # get_temperature is an extention of the get_weather action. Rather than create a new similar function
        # we can can call get_weather with an extra parameter that will allow get_weather to return the appropriate
        # values based on who the original caller was.
        return self.get_weather(result=result, source="temperature")

    def get_restaurant(self, result):
        return restaurant.get_restaurant(result)

    def get_time(self, result):
        return clock.get_time(result)
