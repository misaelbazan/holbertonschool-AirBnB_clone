#!/usr/bin/python3
"""
This module
"""

import sys
import cmd
import json
import re
from models.base_model import BaseModel
from models import storage


classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """This class builds a customized cmd from the cmd module and
    inherits all its attributes and methods.
    Attributes:
        prompt - defines a customize prompt
    """
    prompt = "(hbnb) "

    def validate_classname(args, check_id=False):
        """Function that validates the classname and instance id entry
        """
        if len(args) < 1:
            print("** class name missing **")
            return False
        if args[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2 and check_id:
            print("** instance id missing **")
            return False
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to JSON file
            and prints the id
        """
        args = arg.split()
        if not validate_classname(args):
            return

        new_obj = classes[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """Print the string representation of an instance
        """
        args = arg.split()
        if not validate_classname(args, check_id=True):
            return
        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        print(req_instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (saves the id into JSON file
        """
        args = arg.split()
        if not validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return

        del instance_objs[key]
        storage.save()

    def do_all(self, arg):
        """Prints string representation of all instances, based
        or not on the class name
        """
        args = arg.split()
        all_dict = storage.all()

        if len(args) < 1:
            print(["{}".format(str(v)) for _, v in all_dict.items()])
            return
        if args[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        else:
            print(["{}".format(str(v)) for _, v in all_dict.items()\
                    if type(v).__name__ == args[0]])
            return

    def do_update(self, arg: str):
        """Updates an instance based on the class name and id by adding
        or updating atribute (SAVE to the JSON file)
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split(maxsplit=3)

        # Validate arguments
        if not validate_classname(args, check_id=True):
            return
        # Retrieve the instance
        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        # Assigning the found JSON obj from arg to a variable
        match_json = re.findall(r"{.*}", arg)
        # Check if any JSON were found in the input
        if match_json:
            payload = None
            try:
                # Attemp to parse the first JSON obj into a dict
                payload: dict = json.loads(match_json[0])
            except Exception:
                print("** invalid syntax **")
                return
            # Iterate over each k, v pair in the parsed JSON data
            for k, v in payload.items():
                # Update the req_instance with the corresponding
                # attribute, value
                setattr(req_instance, k, v)

        if not validate_attrs(args):
            return
        first_word = re.findall(r"^[\"\'](.*?)[\"\']", args[3])
        if first_word:
            setattr(req_instance, args[2], first_word[0])
        storage.save()

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


def validate_classname(args, check_id=False):
    """Function that validates the classname and instance id entry
    """
    if len(args) < 1:
        print("** class name missing **")
        return False
    if args[0] not in classes:
        print("** class doesn't exist **")
        return False
    if len(args) < 2 and check_id:
        print("** instance id missing **")
        return False
    return True


def validate_attrs(args):
    """Funtion that validates instance attribute names and values
    """
    if len(args) < 3:
        print("** attribute name missing **")
        return False
    if len(args) < 4:
        print("** value missing **")
        return False
    return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
