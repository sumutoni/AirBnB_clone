#!/usr/bin/python3
"""console module, that contains the class HBNBCommand
"""
import cmd
from models.base_model import BaseModel
import json
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""

    prompt = '(hbnb) '
    CLASS_NAME = ["BaseModel"]

    def do_EOF(self, line):
        """exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, name):
        """Create a new instance of BaseModel"""
        if name:
            if name in type(self).CLASS_NAME:
                b1 = eval(name + "()")
                b1.save()
                print(b1.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, name_id):
        """Prints the string representation of an instance
           based on the class name and id"""
        if name_id:
            split_name_id = name_id.split()
            if len(split_name_id) == 2:
                key_name_id = split_name_id[0] + "." + split_name_id[1]
                if split_name_id[0] in type(self).CLASS_NAME:
                    if key_name_id in storage.all().keys():
                        value = storage.all()[key_name_id]
                        print(value)
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            elif len(split_name_id) == 1:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def emptyline(self):
        """configure how an empty + ENTER behave"""
        pass

    def do_destroy(self, name_id):
        """ Deletes an instance based on the class name and id
            (save the change into the JSON file)"""
        if name_id:
            split_name_id = name_id.split()
            if len(split_name_id) == 2:
                key_name_id = split_name_id[0] + "." + split_name_id[1]
                if split_name_id[0] in type(self).CLASS_NAME:
                    if key_name_id in storage.all().keys():
                        del storage.all()[key_name_id]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            elif len(split_name_id) == 1:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, name):
        """Create a new instance of BaseModel"""
        list_all = []
        if name:
            if name in type(self).CLASS_NAME:
                for key, value in storage.all().items():
                    list_all.append(str(value))
                print(list_all)
            else:
                print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                list_all.append(str(value))
            print(list_all)

    def do_update(self, attr):
        """Update an instance based on the class name and id"""
        if attr:
            split_attr = attr.split()
            if len(split_attr) >= 2:
                key_attr = split_attr[0] + "." + split_attr[1]
                if split_attr[0] in type(self).CLASS_NAME:
                    if key_attr in storage.all().keys():
                        if len(split_attr) >= 3:
                            if len(split_attr) >= 4:
                                priv_attr = ["id", "created_at", "updated_at"]
                                key = split_attr[2]
                                value = split_attr[3]
                                if split_attr[2] not in priv_attr:
                                    attr_dct = storage.all()[key_attr]
                                    get_dt = attr_dct.to_dict()
                                    get_dt[key] = value
                                    updated_cls = eval(split_attr[0])(**get_dt)
                                    storage.all()[key_attr] = updated_cls
                                    storage.save()
                            else:
                                print("** value missing **")
                        elif len(split_attr) == 2:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            elif len(split_attr) == 1:
                print("** instance id missing **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    import sys

    HBNBCommand().cmdloop()
