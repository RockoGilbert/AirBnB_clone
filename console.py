#!/usr/bin/python3
"""AirBnB console"""


import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """AirBnB console"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        exit()

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        exit()

    def emptyline(self):
        """handles empty line and enter"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it to a JSON file, and prints the id
        """
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
        """
        Prints the string representation of an instance
        based on the class name and id
        """
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
        """
        Deletes an instance based on the class name and id
        """
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
            delete = None
            all_objs = storage.all()
            for key in all_objs.keys():
                if key == obj_name:
                    delete = key
            if delete is not None:
                all_objs.pop(delete)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of instances if
        no class name is passed, or prints a string representation
        of a class
        """
        obj_list = []
        if arg == "":
            all_objs = storage.all()
            for key in all_objs.values():
                obj_list.append(key.__str__())
            print(obj_list)
        elif arg not in ["Amenity", "BaseModel", "City",
                         "Place", "Review", "State", "User"]:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            for key in all_objs.values():
                if key.__class__.__name__ == arg:
                    obj_list.append(key.__str__())
            print(obj_list)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """
        class_name = None
        class_id = None
        class_attr_name = None
        class_attr_val = None
        if arg != "":
            try:
                class_name = arg.split(" ")[0]
                class_id = arg.split(" ")[1]
                class_attr_name = arg.split(" ")[2]
                class_attr_val = arg.split(" ")[3]
            except IndexError:
                pass
        if class_name is None:
            print("** class name missing **")
        elif class_name not in ["Amenity", "BaseModel", "City",
                                "Place", "Review", "State", "User"]:
            print("** class doesn't exist **")
        elif class_id is None:
            print("** instance id missing **")
        elif class_attr_name is None:
            print("** attribute name missing **")
        elif class_attr_val is None:
            print("** value missing **")
        else:
            obj_name = class_name + "." + class_id
            id_check = False
            all_objs = storage.all()
            all_obj_keys = storage.all().keys()
            for key in all_obj_keys:
                if key == obj_name:
                    obj = all_objs.get(key)
                    setattr(obj, class_attr_name, class_attr_val)
                    id_check = True
            if id_check is not True:
                print("** no instance found **")


if __name__ == '__main__':
        HBNBCommand().cmdloop()
