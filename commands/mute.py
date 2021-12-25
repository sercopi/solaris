from commands.command import Command
import pyautogui


class MuteCommand(Command):
    def must_equal_keyword(self):
        return True

    def keyword(self):
        return "mute"

    def __init__(self, engine):
        super().__init__(engine)

    # overriding abstract method
    def execute(self, _):
        pyautogui.press("volumemute")
        return True
