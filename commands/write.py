from commands.command import Command
import pyautogui
import random
from speech_recognition import Microphone


class WriteCommand(Command):
    def must_equal_keyword(self):
        return True

    def must_contain_keyword(self):
        return True

    def keyword(self):
        return "enter"

    def __init__(self, engine):
        super().__init__(engine)

    def setConfig(self, config):
        self._config = config
        self.open_up_responses = config["open_up_responses"]
        self.confirmation_responses = config["confirmation_responses"]
        self.languages = config["languages"]
        self.default_language = config["default_language"]

    def listen(self, language):
        try:
            with Microphone() as source:
                voice = self.listener.listen(source)
                text = self.listener.recognize_google(voice, language=language)
                return text
        except Exception as e:
            print(e)
            print(e.with_traceback(None))
            return False

    # overriding abstract method
    def execute(self, input):
        language = self.getCommandParams(input)
        language_code = self.languages.get(language, self.default_language)
        self.say(random.choice(self.open_up_responses))
        text = self.listen(language_code)
        print(text)
        if not text:
            return True
        self.write(text)
        if self.confirm(random.choice(self.confirmation_responses)):
            pyautogui.press("enter")
        return True
