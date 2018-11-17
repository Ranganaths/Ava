<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/grab-the-nlu-training-dataset-and-starter-packs/903 -->

## intent:bye

- Bye
- Bye Ava
- Goodbye
- Goodbye Ava
- See you later
- Talk to you later
- See you later Ava
- Talk to you later Ava
- Goodbye friend
- bye for now
- catch you later
- gotta go
- See you
- goodnight
- have a nice day
- i'm off
- see you later alligator
- we'll speak soon
- later

## intent:gratitude

- Thanks
- Thank you
- Thank you so much
- Thanks Ava
- Thanks for that
- cheers
- cheers bro
- ok thanks!
- perfect thank you
- thanks a bunch for everything
- thanks for the help
- thanks a lot
- amazing, thanks
- cool, thanks
- cool thank you
- right on
- perfect, thanks
- perfect, thank you
- I appreciate it
- I'm grateful
- Greatly apprciated
- It's appreciated
- gratitude
- thanks very much

## intent:confirm

- yes
- correct
- that's right
- yes sure
- sure
- absolutely
- for sure
- yes yes yes
- definitely
- that's correct
- right
- correct

## intent:user_name

- My name is [Alice](name) <!--- Square brackets contain the value of entity while the text inside the parentheses is a a label of the entity -->
- I am [Josh](name)
- I'm [Lucy](name)
- People call me [Greg](name)
- It's [David](name)
- Usually people call me [Amy](name)
- My name is [John](name)
- You can call me [Sam](name)
- Please call me [Linda](name)
- Name name is [Tom](name)
- I am [Richard](name)
- I'm [Tracy](name)
- Call me [Sally](name)
- I am [Philipp](name)
- I am [Charlie](name)

## intent:get_restaurant

- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I'm hungry
- I am hungry
- i'm looking for a place in the [north](location) of town
- show me [chinese](cuisine) restaurants
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot
- search for restaurants
- anywhere in the [west](location)
- anywhere near [18328](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [29432](location)
- Is there good [bbq](cuisine) around [here](location)
- What's the closest [fast food](cuisine)
- What should eat
- any good food around here
- whats the best place to eat
- whats the best [thai](cuisine) food in [ballard](location)
- what restaurants are open [now](time)
- what [thai](cuisine) restaurants are open [right now](time)
- is there any good [indian](cuisine) around [here](location)

## intent:get_weather

- What's the weather like
- What's the [current](time) weather
- What is [today's](time) weather
- Will it be [sunny](weather) [today](time)
- Will it be [rainy](weather) [today](time)
- Will it be [cloudy](weather) [today](time)
- What is [tomorrow's](time) weather
- What is [friday's](time) weather
- Will it be [sunny](weather) [friday](time)
- Will it be [cloudy](weather) [monday](time)
- Will it be [rainy](weather) [tuesday](time)
- What's the weather going to be like [tomorrow](time)
- What's the weather going to be like [thursday](time)
- What's the weather in [San Francisco](location)
- Is it [raining](weather)
- Is it sunny in [Los Angeles](location)
- What will the weather be on [friday](time)
- What is [New York's](location) weather
- What's [Miami's](location) weather [sunday](time)
- What's the weather [tomorrow](time) in [San Francisco](location)
- What's the weather [tomorrow](time) in zipcode [98119](location)
- Is it cloudy in zipcode [94608](location)
- What's the weather like in areacode [94806](location)

## intent:get_temperature

- What's the [current](time) temperature
- What's the temperature [tonight](time)
- What is the temperature
- Do I need a jacket
- Is it cold outside
- Will it be cold [tonight](time)
- Will it be hot [tonight](time)
- What is [tomorrow's](time) temperature
- What is [friday's](time) temperature
- What is the temperature on [saturday](time)
- What is the temperature on [saturday](time) in [Houston](location)
- Is it warm outside
- How cold is it
- How warm is it
- What's the temperature in [Bellevue](location)
- How hot is [San Francisco](location)
- Whats the current temperature in [98109](location)

## intent:convert_unit

- How many [ounces](unit) in a [pound](unit)
- [Five](ammount) [cups](unit) is how many [liters](unit)

## intent:get_status

- How are you?
- How are you doing?
- How are you feeling?
- How's it going?
- What's up?
- You doing ok?
- You doing alright?

## intent:get_defenition

- Definition of the word [carrot](key)
- Define [trust](key)
- Define the word [sand](key)
- What's the meaning of the word [smart](key)
- What is the meaning of [machine](key)

## intent:get_music

- [play](action) music
- [play](action) [Despacito][title]
- [play](action) [Beyonce][artist]
- [play](action) [trust](title) by [brent faiyaz](artist)
- [play](action) playlist [slowing it down](playlist)
- [play](action) a [random](type) song
- lets [turn up](type)
- i need music
- i need [concentration](type) music
- we need [party](type) music
- put on some music
- put on some [jazz](type)
- [pause](action) the music
- [pause](action) music
- [next](action) song
- [play](action) [next](action) song
- [previous](action) song
- [play](action) [previous](action) song

## intent:finance_search

- what's the current price of [AAPL](ticker)
- how's [GE](ticker) performing
- how's the market doing?
- is [bitcoin](ticker) up or down?

## intent:get_time

- What time is it?
- Can you give me the time?
- Can you tell me the time?
- What is the time?
- What's the current time?
- what's the time?

<!-- ## intent:light_control
## get_antonyms
## get_synonym
## get_cryptocurrency
## set_timer
##
## intent:os_control

## intent:google_search

## intent:math_calculation
- What's two times two
- What is 2 times 2
- what is 12 time
## intent:get_event"

## intent:geo_location

## intent:get_recipes

## intent:movie_facts

## intent:movie_lookup

## intent:create_appointment

## intent:update_appointment

## intent:remove_appointment

## intent:get_free_times

## intent:get_appointments

## intent:get_news

## intent:manage_project
-->
