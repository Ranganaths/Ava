from rasa_nlu.model import Interpreter
from pyaudio import PyAudio, paInt16
from pocketsphinx import pocketsphinx
from os import path, remove, rename
from pygame import mixer, event
from ava_skills import AvaSkills
import ava_api_keys as keys
import ava_settings as settings
import json
import speech_recognition
import boto3
import time


class Ava (AvaSkills):

    def __init__(self):
        self.interpreter = Interpreter.load(settings.RASA_MODEL_DIR)
        self.stream = PyAudio().open(format=paInt16, channels=1,
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
        print("Waiting for wakeup ...")
        while True:
            buf = self.stream.read(1024)
            if buf:
                self.decoder.process_raw(buf, False, False)
            else:
                break
            if self.decoder.hyp() is not None:
                global t0
                t0 = time.time()
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

    def get_tts(self, text, file_name, save=True):
        print("Converting text to speech...")
        polly_client = boto3.Session(aws_access_key_id=keys.POLLY_ACCESS_KEY_ID,
                                     aws_secret_access_key=keys.POLLY_SECRET_ACCESS_KEY, region_name='us-west-2').client('polly')

        response = polly_client.synthesize_speech(VoiceId='Joanna',
                                                  OutputFormat='mp3',
                                                  Text=text)
        print("Creating Audio file...")
        with open(settings.MEDIA_DIR+file_name, 'wb') as f:
            f.write(response['AudioStream'].read())
        self.play_audio(audio_file=file_name, save=save)

    def play_audio(self, audio_file, save=True):
        audio_file = settings.MEDIA_DIR + audio_file
        is_file = path.isfile(audio_file)
        if is_file:
            mixer.init()
            try:
                mixer.music.load(audio_file)
                mixer.music.play()
                print("Playing Audio: ", audio_file)
                while(mixer.music.get_busy()):
                    continue
                mixer.music.stop()
            except Exception as e:
                print("Error playing file...", e)
                return False
            finally:
                if(not save):
                    # A weird bug exists where we can't delete a file via remove or File Explorer even after quiting the mixer. The issue appears to only occur with mp3's that were created from this script.
                    # To circumvent temporarily we do a quick load of a dummy file so taht we can delete our intended file. This doesn't effect the normal flow of the function.
                    mixer.music.load(settings.MEDIA_DIR + "dummy.wav")
                    remove(audio_file)
                mixer.quit()
                print("Done playing...")
        else:
            print("Audio file not found...")
            return False
        return True

    def listen_for_input(self):
        sr = speech_recognition.Recognizer()
        mic = speech_recognition.Microphone()
        hyp = None
        with mic as source:
            # sr.adjust_for_ambient_noise(source)
            try:
                global t0
                print(time.time() - t0)
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
            self.get_tts(
                text=result['tts'], file_name=result['file'], save=result['save'])
