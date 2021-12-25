from commands.command import Command
import pywhatkit


class GoogleCommand(Command):
    def must_contain_keyword(self):
        return True

    def keyword(self):
        return "google"

    def __init__(self, engine):
        super().__init__(engine)

    def setConfig(self, config):
        self._config = config
        self.after_google_response = config["after_google_response"]

    # overriding abstract method
    def execute(self, input):
        text = self.getCommandParams(input)
        pywhatkit.search(text)
        if self.after_google_response:
            self.say(self.after_google_response)
        return True
