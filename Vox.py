from os import path
from pocketsphinx import pocketsphinx
import speech_recognition
import pyaudio as pAud
from pygame import mixer
import boto3
from keys import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
import settings


def listen_for_wake(key_phrase):
    config = pocketsphinx.Decoder.default_config()
    config.set_string('-hmm', path.join(settings.MODEL_DIR, 'en-us/en-us'))
    config.set_string('-dict', path.join(settings.MODEL_DIR,
                                         'en-us/cmudict-en-us.dict'))
    config.set_string('-keyphrase', key_phrase)
    config.set_float('-kws_threshold', 1)
    config.set_string('-logfn', 'text.log')

    pyaudio = pAud.PyAudio()
    stream = pyaudio.open(format=pAud.paInt16, channels=1,
                          rate=16000, input=True, frames_per_buffer=1024)
    stream.start_stream()

    decoder = pocketsphinx.Decoder(config)
    decoder.start_utt()
    mixer.init()
    print("Waiting for wakeup ...")

    while True:
        buf = stream.read(1024)
        if buf:
            decoder.process_raw(buf, False, False)
        else:
            break
        if decoder.hyp() is not None:
            print(f"Key phrase '{key_phrase}' detected...")
            if (not play_audio("wake_chime.mp3")):
                exit()

            if (not play_audio("greeting.mp3")):
                get_tts(text="How can I help?", file_name="wake_greeting.mp3")
            listen_for_command()
            decoder.end_utt()
            print("Waiting for wakeup ...")
            decoder.start_utt()


def get_tts(text, file_name):

    polly_client = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name='us-west-2').client('polly')

    response = polly_client.synthesize_speech(VoiceId='Joanna',
                                              OutputFormat='mp3',
                                              Text=text)

    with open(file_name, 'wb') as f:
        f.write(response['AudioStream'].read())

    play_audio(audio_file=file_name)


def play_audio(audio_file):
    audio_file = settings.MEDIA_DIR + audio_file
    if path.isfile(audio_file):
        try:
            mixer.music.load(audio_file)
            mixer.music.play()
            while(mixer.music.get_busy()):
                continue
            return True
        except:
            print("Error playing file...")
            return False
    else:
        print("Audio file not found...")
        return False


def listen_for_command():
    mic = speech_recognition.Microphone()
    sr = speech_recognition.Recognizer()
    with mic as source:
        sr.adjust_for_ambient_noise(source)
        try:
            print("Listening...")
            audio = sr.listen(source)
        except speech_recognition.WaitTimeoutError:
            print("No input received ...")
    try:
        print("Decoding...")
        print("Hypothesis: ", sr.recognize_sphinx(audio))
    except:
        print("FAIL")


if __name__ == "__main__":
    listen_for_wake("hey ava")
