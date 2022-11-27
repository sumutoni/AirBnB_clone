#!/usr/bin/python3
""" This module is for the console; command intepreter for The AirBnB
project. It is the main entry point of the command interpreter"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """implementation of the console and its commands"""

    prompt = '(hbnb)'
    classes = {'BaseModel': BaseModel, 'User': User}

    def do_quit(self, arg):
        """command to quit program"""
        sys.exit()

    def do_EOF(self, arg):
        """command to quit program when EOF or ctrl+D is encountered"""
        sys.exit()

    def emptyline(self):
        """empty line won't execute anything"""
        pass

    def do_create(self, arg=""):
        """reates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if arg == "":
            print("** class name missing **")
        elif arg not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            model = HBNBCommand.classes[arg]()
            model.save()
            print(model.id)

    def do_show(self, arg=""):
        """Prints the string representation of an instance
        based on the class name and id"""
        if arg == "":
            print("** class name missing **")
        arg = [i.strip() for i in arg.split()]
        if arg[0] in HBNBCommand.classes.keys():
            if len(arg) == 1:
                print("** instance id missing ** ")
            else:
                key = "{}.{}".format(arg[0], arg[1])
                if key in storage.all().keys():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg=""):
        """ Deletes an instance based on the class name and id"""
        if arg == "":
            print("** class name missing **")
        arg = [i.strip() for i in arg.split()]
        if arg[0] in HBNBCommand.classes.keys():
            if len(arg) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(arg[0], arg[1])
                if key in storage.all().keys():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """ Prints all string representation of all
        instances based or not on the class name"""
        instances = []
        if len(arg) == 0:
            for v in storage.all().values():
                instances.append(v.__str__())
            print(instances)
        else:
            if arg in HBNBCommand.classes.keys():
                for k, v in storage.all().items():
                    if k == arg:
                        instances.append(v.__Str__())
            else:
                print("** class doesn't exist **")
        print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        if check_class(arg) is True:
            arg = [i.strip() for i in arg.split()]
            key = "{}.{}".format(arg[0], arg[1])
            values = storage.all()
            if len(arg) == 2:
                print("** attribute name missing **")
            elif len(arg) == 3:
                print("** value missing **")
            elif values[key] not in values.values():
                print("** no instance found **")
            else:
                setattr(values[key], arg[2], arg[3])
                storage.save()

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if check_class(arg) is True:
            arg = [i.strip() for i in arg.split()]
            elements = storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key in elements:
                del storage.all()[key]
            else:
                print("** no instance found **")

    def check_class(self, arg):
        """checks if class exists"""
        if len(arg) == 0:
            print("** class name missing **")
            return False
        arg = [i.strip() for i in arg.split()]
        if arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        else:
            return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
