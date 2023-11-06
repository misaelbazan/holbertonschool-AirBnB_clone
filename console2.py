#!/usr/bin/python3
"""
This module
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """This class builds a customized cmd from the cmd module and
    inherits all its attributes and methods.
    Attributes:
        prompt - defines a customize prompt
    """
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, stop, line):
        """This method is called after each command is executed
        Return:
            True - indicates that we want to exit de command loop
            stop -
        """
        if line == 'EOF':
            return True
        return stop

    def emptyline(self):
        """This method defines what to do when and empty line is executed
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
