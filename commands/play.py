from commands.command import Command
import pywhatkit


class PlayCommand(Command):
    def must_contain_keyword(self):
        return True

    def keyword(self):
        return "play"

    def __init__(self, engine):
        super().__init__(engine)

    # overriding abstract method
    def execute(self, input):
        video = self.getCommandParams(input)
        if not video:
            return True
        self.say("playing " + video)
        pywhatkit.playonyt(video)
        return True
