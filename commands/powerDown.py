from commands.command import Command


class PowerDownCommand(Command):
    def must_equal_keyword(self):
        return True

    def keyword(self):
        return "power down"

    def __init__(self, engine):
        super().__init__(engine)

    # overriding abstract method
    def execute(self, _):
        self.say("Good night, Sergio")
        return False
