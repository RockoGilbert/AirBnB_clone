#!/usr/bin/python3
""" console """

import cmd
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex  # for splitting the line along spaces except in double quotes

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Exits console"""
        exit()

    def emptyline(self):
        """ Handles if the line is empty """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Creates a new instance of a class"""
        if arg == "" or None:
            print("** class name missing **")
        elif arg not in ["Amenity", "BaseModel", "City", "Place",
                         "Review", "State", "User"]:
            print("** class doesn't exist **")
        else:
            if arg == "Amenity":
                new_class = Amenity()
            elif arg == "BaseModel":
                new_class = BaseModel()
            elif arg == "City":
                new_class = City()
            elif arg == "Place":
                new_class = Place()
            elif arg == "Review":
                new_class = Review()
            elif arg == "State":
                new_class = State()
            elif arg == "User":
                new_class = User()
            print(new_class.id)
            storage.new(new_class)
            storage.save()

    def do_show(self, arg):
        """Prints an instance as a string based on the class/id"""
        class_name = None
        class_id = None

        if arg != "":
            try:
                class_name = arg.split(" ")[0]
                class_id = arg.split(" ")[1]
            except IndexError:
                pass
        if class_name is None:
            print("** class name missing **")
        elif class_name not in ["Amenity", "BaseModel", "City",
                                "Place", "Review", "State", "User"]:
            print("** class doesn't exist **")
        elif class_id is None:
            print("** instance id missing **")
        else:
            obj_name = class_name + "." + class_id
            id_check = False
            all_objs = storage.all()
            for key in all_objs.keys():
                if key == obj_name:
                    obj = all_objs[key]
                    print(obj)
                    id_check = True
            if id_check is not True:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class/id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representation of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_update(self, arg):
        """Changes an instance based on value"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
