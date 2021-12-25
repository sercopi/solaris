from commands.command import Command
import pywhatkit
from datetime import datetime
import os


class ScreenshotCommand(Command):
    def must_equal_keyword(self):
        return True

    def keyword(self):
        return "screenshot"

    def __init__(self, engine):
        super().__init__(engine)

    def setConfig(self, config):
        self._config = config
        self.screenshot_folder = config["screenshot_folder"]
        self.screenshot_taken_response = config["screnshot_taken_response"]
        self.screenshot_folder_doesnt_exist_response = config[
            "screenshot_folder_doesnt_exist_response"
        ]

    # overriding abstract method
    def execute(self, input):
        if not os.path.isdir(self.screenshot_folder):
            self.say(self.screenshot_folder_doesnt_exist_response)
            return True
        pywhatkit.take_screenshot(
            "{}/{}.png".format(
                self.screenshot_folder,
                datetime.now().strftime("%d_%m_%Y_%H_%M_%S"),
            ),
            0,
        )
        if self.screenshot_taken_response:
            self.say(self.screenshot_taken_response)
        return True
