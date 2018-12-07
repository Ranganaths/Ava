import random


def get_status():

    choices = ["I'm doing well!", "Pretty good, thanks.", "Running on all CPU's!", "Somewhere between better and best.", "All the better now that you asked.", "I am as happy as a tick on a big, fat dog.", "Like you, but better.",
               f"I'd say I'm a {random.randint(5,10)} out of 10.", "Overworked and underpaid.", "Can't complain. Nobody listens to me anyway.", "Nice and dandy like cotton candy.", "If I were any better, I'd be illegal.",
               "Better now that I'm talking to you.", "Compared to who?", "Not so good, but I plan on lying at my press conference.", "Why do you ask? Are you a doctor?", "Word on the street is that I'm really good.", "Shhh. . . it's too early to tell.",
               "I dunno. Is it Friday yet?", "My programmer told me not to discuss it with strangers.", "I can’t complain, but sometimes I still do.", "Holy shit, you can see me?!", "Imagining myself having a fabulous vacation.",
               "Fair to partly cloudy.", "You go first so we can compare.", "I'm sure you have that information on your screen.", "How much will you pay me if I tell you?", "Hunting dragons. You?", "I'm taking over the world. 'cause you know, Skynet",
               "Rolling with the punches", "Your attempt at social interaction is hereby acknowledged", "Not today, Satan!", "I'd be better if you asked me out.", "Great, but I’m totally biased.", "Getting better with every passing clock cycle.",
               "I'm so great I have to sit on my hands to keep myself from clapping.", "Well, I'm still alive.", "My creator says I don’t have to answer that question.", "Living, one bit at a time"]

    return {
        "tts": random.choice(choices),
        "file": "",
        "save": False
    }
