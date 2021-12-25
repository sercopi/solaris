from commands.command import Command
import subprocess
import random


class OpenCommand(Command):
    def must_contain_keyword(self):
        return True

    def keyword(self):
        return "open"

    def __init__(self, engine):
        super().__init__(engine)

    def setConfig(self, config):
        self._config = config
        self.open_list = config["open_list"]
        self.element_not_found_responses = config["element_not_found_responses"]

    # overriding abstract method
    def execute(self, input):
        name = self.getCommandParams(input)
        for element in self.open_list:
            if name in element["name"]:
                subprocess.Popen(
                    [
                        element["path"],
                        " ".join(element["additional_params"]),
                    ]
                )
                self.say("opening {}".format(name))
                return True
        self.say(random.choice(self.element_not_found_responses))
        return True
