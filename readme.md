# Ava

Ava is a personal assistant born out of the need for a more personalized assistant experience, while maintaining as much control over personal data. My aim with Ava is to make mundane tasks fully voice controlled and painless, as well as making Ava have fully "intelligent" conversations, reacting according to the users response. I aim to provide Ava with a wide range of skills from simple gathering of weather information or controlling of smart lights, to more complex skills like flight booking and calendar management. See below for more information on how Ava works as well as skills availabe and in development.

## How it Works

Like industry voice assistants (Alexa,Siri,Cortona,Ok,Google), Ava responds to a wake up command provided by the user, the default being "Hey Ava". This is accomplished via the [CMUSphinx](https://cmusphinx.github.io/) Speech Recogintion Toolkit, more specifically the [Pocketsphinx-Python](https://github.com/cmusphinx/pocketsphinx-python) wrapper. Microphone stream data is constantly processed until the wake up command is recognized. Once the wake up command is recognized Ava acknowledges being woken up greeting the user and then listens for further voice input.

Although pocketsphinx works relatively well, Ava will default to Google Speech Recognition when listening for input for better Speech recognition accuracy and fall back to [Pocketsphinx-Python](https://github.com/cmusphinx/pocketsphinx-python) if there is an error in recognition. To accomplish this the [Speech_Recognition](https://github.com/Uberi/speech_recognition) library is used, as it provides a wrapper for multiple Speech Recognition api's like IBM Watson, Wit.ai and of course Google Speech Recognition. The primary reasoning behind implementing it in this fashion is that Google Speech Regonition although accurate is being migrated to solely be Google Cloud Speech. In the event that the old API is full deprecated a fail safe is built in to maintain offline functionality.

The output of the above speech recognition leaves us with the text version of the voice input. Now things can get exciting. At this point we still don't know what the user wants to accomplish so somehow we must translate the text into actions. This is to say we must gather the intention behind the text. Enter Natural Language Understanding (NLU). NLU employs Machine Learning (ML) techniques to teach computers how to classify the intention of text as well as extract key data (enteties) that can then be used by a program to make decisions and execute actions. For more details you can read: [How intent Classifciation works in NLU](https://mrbot.ai/blog/natural-language-processing/understanding-intent-classification/).

We can create and train a ML model to handle intent classification but there are many existing resources that handle intent classification. However, most resources are REST API's and have limits on requests or are not free. In an effort to maintain much of Ava's functionality offline, an open sourced NLU library is needed. For this we make use of [Rasa's](https://rasa.com/) NLU library [Rasa NLU](https://rasa.com/docs/nlu/). With Rasa we can train an NLU model with our own data without sacrificing it to any of the FAANG companies. It also allows us to tweak and customize models for our data (yay!) but we just default to the TensorFlow training pipeline already provided (see config file: [rasa_nlu_config.yml](https://github.com/jmcnab57/Ava/blob/master/rasa/rasa_nlu_config.yml)). Rasa gives us a lot out of the box and offline. Rasa also gives us [Rasa Core](https://rasa.com/docs/core/) which also employs ML techniques to create a Dialogue engine. We'll make use of Rasa core in further versions of Ava to make interaction more human like.

To train Rasa I created a training dataset with multiple text examples per intent. Training data can viewed in the [rasa](https://github.com/jmcnab57/Ava/tree/master/rasa) folder under [rasa_nlu_training.md](https://github.com/jmcnab57/Ava/blob/master/rasa/rasa_nlu_training.md). Creating the training data mainly requires imagining multiple ways that a user could express a certain action or intent. This is to say, for example, multiple ways a user could request weather data. Once the trainining data markup is created it can then be fed to Rasa's trainig module which will ouput the resulting models which can be used by an interpreter to classify intent.

With a trained model we can now pass the speech recognition text into a Rasa interpreter, which will return the intent, e.g get_weather, as well as the extracted entities. With the proper intent and entities we can now call the equally named methods to handle api or database requests and compose a response for the user. The response is processed via a Text to Speech(TTS) engine. The preferred method being Amazon Polly as it provides us with very human like TTS speech functionality. Polly is a temporary solution until a good offline TTS library is identified. We might have to make our own down the line(fun project)! Now, most assistants tend to be repetitive so we only make a request to Amazon Polly once per response and then save it as an .mp3 file. Ava will always check to see if the response .mp3 already exists before requesting it from Amazon Polly. The aim being that responses are only ever cached once and we can still have TTS offline.

Now that Ava has responded she returns to an active listening stage awaiting her wake up command, "hey ava" and we can begin the process all over again!

## Available and Planned Skills

- Get Status: Ava how are you doing?
- ~~Get Weather: Is it sunny?~~
  - ~~Get Temperature: Is it freezing?.~~
- Unit Conversion: How many ounces in a cup.
- ~~Get Definition: What does Hakuna Matata mean?~~
  - ~~Get Synonyms: Another word for awesome.~~
  - ~~Get Antonym: Opposite of misnomer.~~
- Play Music: Play "Despacito" again...
- Get Stock: How money did we make?.
  - Get Cryptocurrency: When moon?
- ~~Get Time: Is it hammer time?~~
  - Set Timer: Set boiling water timer.
- OS Control: Log off.
- Get Recipe: How to make cereal?
- Movie Facts: Could Jack fit on the plank with Rose?
- Manage Calendar: Make free time?
  - Create Event: Add yoga every wednesday.
  - Update Event: Change yoga to thusrdays.
  - Delete Event: Cancel dinner with myself.
  - Get Free Time: When am i free?
  - Get Appointments: What's on the agenda?
- Get News: What did Trump do today?
- Get Restaurants: Got any food? Cause we hungry.
- Get Event: Any good concerts?

# Built With

### API's

- [Amazon Polly](https://aws.amazon.com/polly/)
- [Zomato API](https://developers.zomato.com/documentation#/)
- [Open Weather Map API](https://openweathermap.org/api)

### Python Libraries

- [Speech_Recognition](https://github.com/Uberi/speech_recognition)
- [Pocketsphinx-Python](https://github.com/cmusphinx/pocketsphinx-python)
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)
- [Rasa NLU](https://github.com/RasaHQ/rasa_nlu)
- [Rasa Core](https://github.com/RasaHQ/rasa_core)
- [Requests](http://docs.python-requests.org/en/master/)
- [Boto 3 - The AWS SDK for Python](https://github.com/boto/boto3)
- [PyGame](https://www.pygame.org/news)
- [Dateparser](https://github.com/scrapinghub/dateparser/blob/master/docs/index.rst)
