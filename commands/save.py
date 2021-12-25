from commands.command import Command
import pyautogui


class SaveCommand(Command):
    def must_equal_keyword(self):
        return True

    def keyword(self):
        return "safe"

    def __init__(self, engine):
        super().__init__(engine)

    def setConfig(self, config):
        self._config = config
        self.save_response = config["save_response"]

    # overriding abstract method
    def execute(self, _):
        pyautogui.hotkey("ctrl", "s")
        self.say(self.save_response)
        return True
