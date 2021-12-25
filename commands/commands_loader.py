from commands.google import GoogleCommand
from commands.mute import MuteCommand
from commands.save import SaveCommand
from commands.say import SayCommand
from commands.play import PlayCommand
from commands.screenshot import ScreenshotCommand
from commands.powerDown import PowerDownCommand
from commands.open import OpenCommand
from commands.write import WriteCommand


class CommandsLoader:
    def __init__(self, commands_list, engine):
        self.commands_list = commands_list
        self.engine = engine

    def load_commands(self):
        commands = [
            SayCommand(self.engine),
            PlayCommand(self.engine),
            PowerDownCommand(self.engine),
            ScreenshotCommand(self.engine),
            GoogleCommand(self.engine),
            SaveCommand(self.engine),
            MuteCommand(self.engine),
            WriteCommand(self.engine),
            OpenCommand(self.engine),
        ]
        must_equal_keyword_commands = []
        must_contain_keyword_commands = []
        for command in commands:
            command.setConfig(self.commands_list.get(command.keyword(), {}))
            if command.must_contain_keyword():
                must_contain_keyword_commands.append(
                    {"keyword": command.keyword(), "command": command}
                )
            if command.must_equal_keyword():
                must_equal_keyword_commands.append(
                    {"keyword": command.keyword(), "command": command}
                )
        len(must_contain_keyword_commands) or must_contain_keyword_commands.sort(
            key=lambda command: self.commands_list[command["keyword"]]["priority"]
        )
        len(must_equal_keyword_commands) or must_equal_keyword_commands.sort(
            key=lambda command: self.commands_list[command["keyword"]]["priority"]
        )
        return {
            "must_contain_keyword_commands": must_contain_keyword_commands,
            "must_equal_keyword_commands": must_equal_keyword_commands,
        }
