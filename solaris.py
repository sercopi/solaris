from speech_recognition import Recognizer, Microphone
from pyttsx3 import Engine
import random
import json
from commands.commands_loader import CommandsLoader


class Solaris:
    def __init__(self):
        self.listener = Recognizer()
        self.engine = Engine()
        self.setEngineProperties()
        self.load_config()
        self.load_commands()

    def say(self, text):
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def setEngineProperties(self, voiceIndex=1, rate=190, gender="male"):
        self.engine.setProperty(
            "voice", self.engine.getProperty("voices")[voiceIndex].id
        )
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("gender", gender)

    def take_command(self, voice):
        try:
            command = self.listener.recognize_google(voice).lower()
            if command == self.name:
                for repetition in range(self.repeat_command_tries):
                    with Microphone() as source:
                        print("listening for command")
                        if repetition == 0:
                            self.say(random.choice(self.attention_responses))
                        try:
                            voice = self.listener.listen(
                                source, self.general_command_timeout
                            )
                        except:
                            self.say(
                                random.choice(self.escape_repetition_commands_responses)
                            )
                            return True
                        text = self.listener.recognize_google(voice).lower()
                        if text in self.escape_repetition_commands:
                            self.say(
                                random.choice(self.escape_repetition_commands_responses)
                            )
                            return True
                        command = self.searchCommand(text)
                        if command:
                            return command.execute(text)
                        if repetition < (self.repeat_command_tries - 1):
                            self.say(random.choice(self.repeat_command_responses))
                self.say(random.choice(self.command_not_found_responses))
            return True
        except Exception as e:
            return True
        except RuntimeError as e:
            print("error")
            self.say("error")
            return False

    def listen(self):
        try:
            with Microphone() as source:
                voice = self.listener.listen(source)
            return self.take_command(voice)
        except:
            return True

    def start_solaris(self):
        self.say("calibrating")
        with Microphone() as source:
            self.listener.adjust_for_ambient_noise(source)
        self.say("waiting for commands")
        output = True
        while output == True:
            output = self.listen()
        self.say("power down")

    def load_commands(self):
        commands_list = self.config["commands"]
        commands_loader = CommandsLoader(commands_list, self.engine)
        self.commands = commands_loader.load_commands()

    def load_config(self):
        with open("config.json") as json_file:
            self.config = json.load(json_file)
        self.name = self.config["name"]
        self.attention_responses = self.config["attention_responses"]
        self.command_not_found_responses = self.config["command_not_found_responses"]
        self.repeat_command_responses = self.config["repeat_command_responses"]
        self.repeat_command_tries = self.config["repeat_command_tries"]
        self.escape_repetition_commands = self.config["escape_repetition_commands"]
        self.escape_repetition_commands_responses = self.config[
            "escape_repetition_commands_responses"
        ]
        self.general_command_timeout = self.config["general_command_timeout"]

    def searchCommand(self, text):
        return self.getCommandFromEqualKeywordCommands(
            text
        ) or self.getCommandFromContainingKeywordCommands(text)

    def getCommandFromEqualKeywordCommands(self, text):
        for command in self.commands["must_equal_keyword_commands"]:
            if command["keyword"] == text:
                return command["command"]
        return False

    def getCommandFromContainingKeywordCommands(self, text):
        for command in self.commands["must_contain_keyword_commands"]:
            if text.startswith(command["keyword"]):
                return command["command"]
        return False


Solaris().start_solaris()
