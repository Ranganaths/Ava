from rasa_nlu.model import Interpreter
from pyaudio import PyAudio
from pocketsphinx import pocketsphinx
import ava_settings as settings
from os import path
from pygame import mixer
import ava_api_keys as keys
import pyaudio as pAudio
import json
import ava_actions as actions
import speech_recognition
import boto3
from ava_actions import AvaActions


class Ava (AvaActions):

    def __init__(self):
        self.interpreter = Interpreter.load(settings.RASA_MODEL_DIR)
        self.stream = PyAudio().open(format=pAudio.paInt16, channels=1,
                                     rate=16000, input=True, frames_per_buffer=1024)
        self.config = pocketsphinx.Decoder.default_config()

        self.config.set_string(
            '-hmm', path.join(settings.SPHINX_MODEL_DIR, 'en-us/en-us'))
        self.config.set_string('-dict', path.join(settings.SPHINX_MODEL_DIR,
                                                  'en-us/cmudict-en-us.dict'))
        self.config.set_string('-keyphrase', settings.WAKE_PHRASE)
        self.config.set_float('-kws_threshold', 1)
        self.config.set_string('-logfn', 'text.log')
        self.decoder = pocketsphinx.Decoder(self.config)
        self.listen_for_wake()

    def listen_for_wake(self):
        self.stream.start_stream()
        self.decoder.start_utt()
        mixer.init()
        print("Waiting for wakeup ...")
        while True:
            buf = self.stream.read(1024)
            if buf:
                self.decoder.process_raw(buf, False, False)
            else:
                break
            if self.decoder.hyp() is not None:
                print(f"Key phrase '{settings.WAKE_PHRASE}' detected...")
                if (not self.play_audio("wake_chime.mp3")):
                    exit()

                if (not self.play_audio("wake_greeting.mp3")):
                    self.get_tts(text="How can I help?",
                                 file_name="wake_greeting.mp3")
                self.listen_for_input()
                self.decoder.end_utt()
                print("Waiting for wakeup ...")
                self.decoder.start_utt()

    def get_tts(self, text, file_name):
        print("Converting text to speech...")
        polly_client = boto3.Session(aws_access_key_id=keys.POLLY_ACCESS_KEY_ID,
                                     aws_secret_access_key=keys.POLLY_SECRET_ACCESS_KEY, region_name='us-west-2').client('polly')

        response = polly_client.synthesize_speech(VoiceId='Joanna',
                                                  OutputFormat='mp3',
                                                  Text=text)
        print("Creating Audio file...")
        with open(settings.MEDIA_DIR+file_name, 'wb') as f:
            f.write(response['AudioStream'].read())

        self.play_audio(audio_file=file_name)

    def play_audio(self, audio_file):
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

    def listen_for_input(self):
        mic = speech_recognition.Microphone()
        sr = speech_recognition.Recognizer()
        hyp = None
        with mic as source:
            sr.adjust_for_ambient_noise(source)
            try:
                print("Listening...")
                audio = sr.listen(source, timeout=2)
                print("Decoding...")
                hyp = sr.recognize_google(audio)
            except speech_recognition.WaitTimeoutError as e:
                print("No input detected timeout...")
            except speech_recognition.UnknownValueError as e:
                if (not self.play_audio("decode_error.mp3")):
                    self.get_tts(
                        text="I'm sorry, but I was not able to understand that command.", file_name="decode_error.mp3")
            except speech_recognition.RequestError as e:
                print("Google request error: ", e)
                print("Running backup decode Sphinx...")
                try:
                    hyp = sr.recognize_google(audio)
                except speech_recognition.UnknownValueError as e:
                    print("Sphinx recognition error: ", e)
                    if (not self.play_audio("decode_error.mp3")):
                        self.get_tts(text="I'm sorry, but I was not able to understand that command.",
                                     file_name="decode_error.mp3")
            else:
                self.process_input_intent(hyp)

    def process_input_intent(self, hypothesis):
        print("Processing intent...")
        print(f"HYPOTHESIS:{hypothesis}")
        result = self.interpreter.parse(hypothesis)
        intent = result['intent']['name']
        confidence = result['intent']['confidence']
        print(f"INTENT: {intent}")
        print(f"CONFIDENCE_SCORE: {confidence}")
        try:
            print("Executing intent action...")
            response = getattr(self, intent)(result)
            print(f"RESULT: {response}")
            self.respond_intent_result(response)
        except Exception as e:
            print(f"Failed intent action...\n\tERROR: {e} ")

    def respond_intent_result(self, result):
        if(not self.play_audio(result['file'])):
            self.get_tts(text=result['tts'], file_name=result['file'])


if __name__ == "__main__":
    Ava()
