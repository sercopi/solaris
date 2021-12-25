from commands.command import Command


class SayCommand(Command):
    def must_contain_keyword(self):
        return True

    def keyword(self):
        return "say"

    def __init__(self, engine):
        super().__init__(engine)

    # overriding abstract method
    def execute(self, input):
        text = self.getCommandParams(input)
        if not text:
            return True
        self.say(text)
        return True
