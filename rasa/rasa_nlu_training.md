<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/grab-the-nlu-training-dataset-and-starter-packs/903 -->

## intent:get_restaurant

- Any good food around here
- I am hungry
- I am hungry, what do you recommend?
- I am hungry, what should I eat?
- I am looking a restaurant in [98119](location)?
- I am looking a restaurant in [98103](location)?
- I am looking a restaurant in [98109](location)?
- I am looking a restaurant in [98122](location)?
- I am looking for [asian fusion](cuisine) food?
- I am looking for [American](cuisine) food)?
- I am looking for [Thai](cuisine) food?
- I am looking for [BBQ](cuisine) food?
- I am looking for an [Indian](cuisine) spot?
- I am looking for an [Chinese](cuisine) spot?
- I am looking for an [Burger](cuisine) spot?
- I am looking for an [Pizza](cuisine) spot?
- I am searching for a dinner spot?
- I could really go for some [Asian](cuisine) food.
- I could really go for some [Burgers](cuisine).
- I could really go for some [Caribbean](cuisine) food.
- I could really go for some [Cuban](cuisine) food.
- I could really go for some [Italian](cuisine) food.
- I want to grab lunch?
- I'd like some [Chinese](cuisine) food?
- I'd like some [Cantonese](cuisine) food?
- I'd like some [Dim Sum](cuisine) food?
- I'd like some [Ethiopian](cuisine) food?
- I'm hungry?
- I'm looking for a place to eat?
- I'm starving?
- I'm starving what should i eat?
- Is there any good [indian](cuisine) around [here](location)?
- Is there any good [chinese](cuisine) around [here](location)?
- Is there good [bbq](cuisine) around [here](location)?
- Is there good [pizza](cuisine) around [here](location)?
- Is there good [Vietnamese](cuisine) around [here](location)?
- Search for Restaurants?
- Show me [Chinese](cuisine) restaurants?
- Show me a [Mexican](cuisine) place in the [centre](location)?
- What [thai](cuisine) restaurants are open [right now](time)?
- What restaurants are open [now](time)?
- What should I eat?
- What's the [closest](location) [fast food](cuisine)?
- Whats the best [thai](cuisine) food in [ballard](location)?
- Whats the best place to eat?
- Where should we eat?

## intent:get_weather

- Is it [raining](weather)?
- Is it [snowing](weather)?
- Is it [sunny](weather)?
- Is it [cloudy](weather) in zipcode [94608](location)
- Is it [clear](weather) in zipcode [98105](location)
- Is it [cloudy](weather) in zipcode [97899](location)
- Is it sunny in [Los Angeles](location)?
- Is it raining in [San Diego](location)?
- Is it cloudy in [Kansas](location)?
- What is [New York's](location) weather
- What is [friday's](time) weather
- What is [today's](time) weather
- What is [tomorrow's](time) weather
- What will the weather be on [friday](time)
- What's [Miami's](location) weather [sunday](time)
- What's the [current](time) weather
- What's the weather [tomorrow](time) in [San Francisco](location)
- What's the weather [today](time) in zipcode [98119](location)
- What's the weather [tomorrow](time) in zipcode [946112](location)
- What's the weather going to be like [thursday](time)
- What's the weather going to be like [tomorrow](time)
- What's the weather in [San Francisco](location)
- What's the weather like?
- What's the weather like in areacode [94806](location)?
- What's the weather like in areacode [98107](location)?
- What's the weather like in areacode [98115](location)?
- What's the weather like in areacode [97217](location)?
- Will it be [cloudy](weather) [monday](time)
- Will it be [cloudy](weather) [today](time)
- Will it be [rainy](weather) [today](time)
- Will it be [rainy](weather) [tuesday](time)
- Will it be [sunny](weather) [friday](time)
- Will it be [sunny](weather) [today](time)

## intent:get_temperature

- Do I need a jacket?
- How cold is it?
- How hot is [San Francisco](location)?
- How hot is [Seattle](location)?
- How hot is [Tacoma](location)?
- How hot is [Atlanta](location)?
- How warm is it?
- Is it cold outside?
- Is it warm outside?
- What is [friday's](time) temperature?
- What is [monday's](time) temperature?
- What is [tuesday's](time) temperature?
- What is [sunday's](time) temperature?
- What is the temperature?
- What is the temperature on [saturday](time)?
- What is the temperature on [saturday](time) in [Houston](location)?
- What is the temperature on [sunday](time) in [Dallas](location)?
- What is the temperature on [thursday](time) in [Miami](location)?
- What's the [current](time) temperature?
- What's the temperature [tonight](time)?
- What's the temperature in [Bellevue](location)?
- What's the temperature in [Berkeley](location)?
- What's the temperature in [Austin](location)?
- Whats the current temperature in [98109](location)?
- Whats the current temperature in [98199](location)?
- Whats the current temperature in [94608](location)?
- Will it be cold [tonight](time)?
- Will it be hot [tonight](time)?

## intent:get_status

- How are you doing?
- How are you feeling?
- How are you?
- How's it going?
- What's up?
- You doing alright?
- You doing ok?

## intent:get_music

- [Play](action) music
- [Play](action) Spotify
- [Play](action) [Despacito][title]
- [Play](action) [Lovely][title]
- [Play](action) [Get You][title]
- [Play](action) [We Find Love][title]
- [Play](action) [Freudian][title]
- [Play](action) [Beyonce][artist]
- [Play](action) [Daniel Caesar][artist]
- [Play](action) [Frank Ocean][artist]
- [Play](action) [Khalid][artist]
- [Play](action) [John Legend][artist]
- [Play](action) [Trust](title) by [Brent Faiyaz](artist)
- [Play](action) [Oui](title) by [Jeremih](artist)
- [Play](action) [Dreamz](title) by [J. Cole](artist)
- [Play](action) [Sure Thing](title) by [Miguel](artist)
- [Play](action) [Humble](title) by [Kendrick Lamar](artist)
- [Play](action) playlist [Slowing it Down](playlist)
- [Play](action) playlist [For Bae](playlist)
- [Play](action) playlist [Oldies](playlist)
- [Play](action) playlist [Sobriety](playlist)
- [Play](action) a [random](type) song
- [Play](action) a [rap](type) song
- [Play](action) a [pop](type) song
- [Play](action) a [country](type) song
- Lets [turn up](type)
- I need music
- I need [concentration](type) music
- We need [party](type) music
- Put on some music
- Put on some [jazz](type)
- [Pause](action) the music
- [Pause](action) music
- [Next](action) song
- [Play](action) [next](action) song
- [Previous](action) song
- [Play](action) [previous](action) song

## intent:get_datetime

- Can you give me the [date](tempus)?
- Can you give me the [time](tempus)?
- Can you tell me the [date](tempus)?
- Can you tell me the [time](tempus)?
- What [date](tempus) is it?
- What [time](tempus) is it?
- What is the [date](tempus)?
- What is the [time](tempus)?
- What's the current [date](tempus)?
- What's the current [time](tempus)?
- what's the [date](tempus)?
- what's the [time](tempus)?

## intent:run_program

- Can you launch [Access](program)?
- Can you launch [Excel](program)?
- Can you launch [Google Chrome](program)?
- Can you launch [Skype for Business](program)?
- Can you open [Outlook](program)?
- Can you open [Windows Media Player](program)?
- Can you open [Jupyter Notebook](program)?
- Can you open [Anaconda Navigator](program)?
- Launch [Audacity](program)?
- Launch [onedrive](program)?
- Launch [Side Sync](program)?
- Launch [SideSync](program)?
- Launch [Chrome](program)?
- Launch program [Github Desktop](program)?
- Open [Adobe Illustrator](program)?
- Open [Firefox](program)?
- Open [PowerPoint](program)?
- Open [Publisher](program)?
- Open [Publisher](program)?
- Open [VLC media player](program)?
- Open [Visual Studio Code](program)?
- Open [settings](program)?
- Open [Spotify](program)?
- Run [Audacity](program)?
- Run [BlueStacks](program)?
- Run [Google Chrome](program)?
- Run [Netbeans IDE](program)?
- Run [OneNote](program)?
- Run [Word](program)?
- Will you open [Visual Studio Code](program)?
- Will you open [CCleaner](program)?
- Will you open [Node.js](program)?
- Will you run [OneNote 2016](program)?
- Will you run [Task Manager](program)?
- Will you run [Slack](program)?

## intent:get_dictionary

- Define [jeopardizing](key).
- Define [jockey](key).
- Define [jumper](key).
- Define [nozzle](key).
- Define [puzzles](key).
- Define [quartz](key).
- Define [red](key).
- Define [trust](key).
- Define [vocalize](key).
- Define the word [immunize](key).
- Define the word [jazz](key).
- Define the word [sand](key).
- Define the word [aberration](key).
- Define the word [brazen](key).
- Define the word [clandestine](key).
- Definition of the word [carrot](key).
- Definition of the word [describe](key).
- Definition of the word [plant](key).
- Definition of the word [tomorrow](key).
- Definition of the word [unpublicized](key).
- What is the meaning of [jobs](key)?
- What is the meaning of [machine](key)?
- What is the meaning of [connive](key)?
- What is the meaning of [extol](key)?
- What is the meaning of [flabbergasted](key)?
- What is the meaning of the word [minimize](key)?
- What is the meaning of the word [gratuitous](key)?
- What is the meaning of the word [infamy](key)?
- What is the meaning of the word [inveterate](key)?
- What is the meaning of the word [bravado](key)?
- What's the meaning of the word [buzz](key)?
- What's the meaning of the word [quickest](key)?
- What's the meaning of the word [smart](key)?
- What's the meaning of the word [subjectively](key)?

## intent:get_thesaurus

- What is the [antonym](type) of the word [bear](key)?
- What is the [antonym](type) of the word [produce](key)?
- What is the [antonym](type) of the word [waft](key)?
- What is the [antonym](type) of the word [unrequited](key)?
- What is the [antonyms](type) of the word [expansion](key)?
- What is the [antonyms](type) of the word [sycophant](key)?
- What is the [antonyms](type) of the word [suave](key)?
- What is the [antonyms](type) of the word [scintillating](key)?
- What is the [opposite](type) of [forge](key)?
- What is the [opposite](type) of [propriety](key)?
- What is the [opposite](type) of [philistine](key)?
- What is the [opposite](type) of [narcissist](key)?
- What is the [synonym](type) of the word [initiate](key)?
- What is the [synonym](type) of the word [mercenary](key)?
- What is the [synonym](type) of the word [lurid](key)?
- What is the [synonym](type) of the word [junket](key)?
- What is the [synonyms](type) of the word [explosive](key)?
- What is the [synonyms](type) of the word [idyllic](key)?
- What is the [synonyms](type) of the word [indelicate](key)?
- What is the [synonyms](type) of the word [finagle](key)?
- What's the [antonym](type) of [down](key)?
- What's the [antonym](type) of [fiasco](key)?
- What's the [antonym](type) of [equanimity](key)?
- What's the [antonym](type) of [caustic](key)?
- What's the [opposite](type) of [happy](key)?
- What's the [opposite](type) of [love](key)?
- What's the [opposite](type) of [angry](key)?
- What's the [opposite](type) of [brusque](key)?
- What's the [opposite](type) of [understanding](key)?
- What's the [opposite](type) of [bravado](key)?
- What's the [synonym](type) of [down](key)?
- What's the [synonym](type) of [angst](key)?
- What's the [synonym](type) of [antidote](key)?
- [Antonym](type) for [misinform](key)?
- [Antonym](type) for [angst](key)?
- [Antonym](type) for [anomaly](key)?
- [Antonym](type) of [orange](key)?
- [Antonym](type) of [dichotomy](key)?
- [Antonym](type) of [glib](key)?
- [Antonym](type) of the word [tranquilizer](key)?
- [Antonym](type) of the word [gregarious](key)?
- [Antonym](type) of the word [heresy](key)?
- [Antonyms](type) for [lie](key)?
- [Antonyms](type) for [insidious](key)?
- [Antonyms](type) for [litany](key)?
- [Antonyms](type) of the word [expert](key)?
- [Antonyms](type) of the word [ogle](key)?
- [Antonyms](type) of the word [ostentatious](key)?
- [Synonym](type) of [invent](key)?
- [Synonym](type) of [peevish](key)?
- [Synonym](type) of [revel](key)?
- [Synonym](type) of [scintillating](key)?
- [Synonym](type) of the word [confidence](key)?
- [Synonym](type) of the word [stoic](key)?
- [Synonym](type) of the word [ubiquitous](key)?
- [Synonyms](type) of [Strategies](key)?
- [Synonyms](type) of [vile](key)?
- [Synonyms](type) of [zealous](key)?
- [Synonyms](type) of [discover](key)?

## intent:unit_conversion

- Convert [1](amount) [pound](base) to [kilograms](conversion)
- Convert [10](amount) [pounds](base) to [grams](conversion)
- Convert [1000](amount) [pounds](base) to [ounces](conversion)
- Convert [100000](amount) [pounds](base) to [grams](conversion)
- Convert [1](amount) [ounce](base) to [kilograms](conversion)
- Convert [12](amount) [ounces](base) to [grams](conversion)
- Convert [1548](amount) [ounces](base) to [pounds](conversion)
- Convert [123895](amount) [ounces](base) to [grams](conversion)
- Convert [1](amount) [minute](base) to [seconds](conversion)
- Convert [25](amount) [hours](base) to [days](conversion)
- Convert [2548](amount) [minute](base) to [seconds](conversion)
- Convert [208796](amount) [seconds](base) to [weeks](conversion)
- Convert [1](amount) [minute](base) to [years](conversion)
- Convert [66](amount) [hours](base) to [days](conversion)
- Convert [1000](amount) [day](base) to [years](conversion)
- Convert [754193](amount) [milliseconds](base) to [minutes](conversion)
- Convert [1](amount) [yard](base) to [meters](conversion)
- Convert [69](amount) [miles](base) to [feet](conversion)
- Convert [1000](amount) [feet](base) to [kilometers](conversion)
- Convert [328467](amount) [meters](base) to [kilometesr](conversion)
- Convert [1](amount) [centimer](base) to [yards](conversion)
- Convert [87](amount) [mile](base) to [inches](conversion)
- Convert [1000](amount) [yard](base) to [centimeters](conversion)
- Convert [426589](amount) [inches](base) to [feet](conversion)
- Convert [1](amount) [cup](base) to [fluids](conversion)
- Convert [91](amount) [pints](base) to [cups](conversion)
- Convert [1000](amount) [quarts](base) to [gallons](conversion)
- Convert [100000](amount) [fluids](base) to [quarts](conversion)
- Convert [1](amount) [gallon](base) to [fluids](conversion)
- Convert [15](amount) [cups](base) to [quarts](conversion)
- Convert [7896](amount) [quarts](base) to [pints](conversion)
- Convert [753695](amount) [pints](base) to [gallons](conversion)
- Convert [5](amount) degress [fahrenheit](base) to [celsius](conversion)
- Convert [98](amount) degress [fahrenheit](base) to [celsius](conversion)
- Convert [102](amount) degress [fahrenheit](base) to [celsius](conversion)
- Convert [0](amount) degress [celsius](base) to [fahrenheit](conversion)
- Convert [20](amount) degress [celsius](base) to [fahrenheit](conversion)
- Convert [102](amount) degress [celsius](base) to [fahrenheit](conversion)
- How many [seconds](conversion) in a [minute](base)?
- How many [hours](conversion) in a [year](base)?
- How many [minutes](conversion) in a [hour](base)?
- How many [feet](conversion) in a [mile](base)?
- How many [meters](conversion) in a [kilometer](base)?
- How many [inches](conversion) in a [yard](base)?
- How many [cups](conversion) in a [gallon](base)?
- How many [fluids](conversion) in a [pint](base)?
- How many [ounces](conversion) in a [pound](base)?
- How many [seconds](conversion) in a [1](amount) [minute](base)?
- How many [hours](conversion) in a [1](amount) [year](base)?
- How many [minutes](conversion) in a [10](amount) [hour](base)?
- How many [feet](conversion) in a [10](amount) [miles](base)?
- How many [meters](conversion) in a [1](amount) [kilometer](base)?
- How many [inches](conversion) in a [100](amount) [yards](base)?
- How many [cups](conversion) in a [1000](amount) [gallons](base)?
- How many [fluids](conversion) in a [1](amount) [pint](base)?
- How many [ounces](conversion) in a [10000](amount) [pounds](base)?
- [1](amount) [ounce](base) is how many [cups](conversion)?
- [10](amount) [inches](base) is how many [miles](conversion)?
- [1000](amount) [pints](base) is how many [gallons](conversion)?
- [1](amount) pound](base) is how many [grams](conversion)?
- [30](amount) [centimeters](base) is how many [yards](conversion)?
- [4125](amount) [cups](base) is how many [pints](conversion)?
- What is [5](amount) degrees [Fahrenheit](base) in [celsius](conversion)?
- What is [7853](amount) [ounces](base) in [pounds](conversion)?
- What is [14](amount) [kilograms](base) in [grams](conversion)?
- What is [72](amount) [fluids](base) in [pints](conversion)?
- What is [5](amount) [gallons](base) in [cups](conversion)?
- What is [1475268](amount) [milliseconds](base) in [hours](conversion)?

<!-- ## intent:light_control

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

## intent:finance_search

- what's the current price of [AAPL](ticker)
- how's [GE](ticker) performing
- how's the market doing?
- is [bitcoin](ticker) up or down?

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

- My name is [Alice](name)
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
-->
