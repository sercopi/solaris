# abstract base class command
from abc import ABC, ABCMeta, abstractmethod, abstractproperty
import pyautogui
from speech_recognition import Recognizer, Microphone
import random
import unicodedata


class Command(ABC):
    __metaclass__ = ABCMeta

    confirmation_default_questions = ["is it ok?"]

    def must_contain_keyword(self):
        return False

    def must_equal_keyword(self):
        return False

    def setConfig(self, config):
        self._config = config

    def getConfig(self):
        return self._config

    @abstractproperty
    def keyword(self):
        ...

    def __init__(self, engine):
        self.engine = engine
        self.listener = Recognizer()

    @abstractmethod
    def execute(self, input):
        ...

    def listen(self):
        ...

    def confirm(self, question):
        self.say(question or random.choice(self.confirmation_default_questions))
        try:
            with Microphone() as first_source:
                voice = self.listener.listen(first_source)
                text = self.listener.recognize_google(voice)
                print(text)
                return text == "yes"
        except Exception as R:
            print(R)
            return False

    def getCommandParams(self, command):
        return command.replace(self.keyword() + " ", "").replace(self.keyword(), "")

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def write(self, text):
        pyautogui.write(
            "".join(
                c
                for c in unicodedata.normalize("NFD", text)
                if unicodedata.category(c) != "Mn"
            )
        )
