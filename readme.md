## Python Assistant

A simple, for fun project assistant in python to execute commands on voice recognition "like" Alexa.

Speech recognition is performed using the simple Google API for speech recognition. Text to speech by using the "pyttsx" library and other tasks with other libraries like "pyautogui"

The commands are created based on an abstract command class that holds useful and required methods for them to work.

They are executed in a Manager class (named Solaris :P, [ref.] https://es.wikipedia.org/wiki/Solaris_(novela))

The CommandsLoader Class is used to initialize and separate the commands in 2 lists: commands that "Must contain" a keyword and commands that "Must equal a keyword".

It is built like this to ensure that the commands that must equal exactly a keyword are searched for first in the list of commands and 2 different commands with the same word in their keywords don´t overlap.

An example.:

Lets say we have 2 different but similar commands: "Mute" and "Mute (someone)"

- The command "Mute" is an "equal keyword command", if I say "mute", the assistant should mute the general volume

- The command "Mute (someone)" is a "Must contain keyword command" and could be a command used to mute someone in a call when we can´t do it directly (we are running a full screen application)

Separating the commands in this 2 lists makes sure that the list of equal keyword commands is searched for first, so if I say only "Mute" the first command is used and not the second one (which also contains the word "mute").

Every command inherits an "execute()" abstract function that must be implemented and contains the command´s logic that will be executed by the manager.

Configuration for the commands is stored in the config.json file. An contains examples of possible configurations for the built in commands.

You can add your own commands simply by writting the class in the "commands" folder, instantiating it into the "commands_loader" and adding its configuration into the "config.json".

This is my first python project so any words of improvement are greatly appreciated:

sergiiosercopi@gmail.com -> email
