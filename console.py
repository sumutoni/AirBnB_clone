#!/usr/bin/python3
""" This module is for the console; command intepreter for The AirBnB
project. It is the main entry point of the command interpreter"""
import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """implementation of the console and its commands"""

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """command to quit program"""
        sys.exit()

    def do_EOF(self, arg):
        """command to quit program when EOF or ctrl+D is encountered"""
        sys.exit()

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
