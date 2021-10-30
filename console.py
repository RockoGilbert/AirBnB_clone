#!/usr/bin/python3
"""Console for AirBnB project"""
import cmd
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex
from shlex import split


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """Controls the HBNB terminal """
    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    if __name__ == '__main__':
        HBNBCommand().cmdloop()

    def do_show(self, args):
        """Prints the string representation of an
        instance based on the class name and id"""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__myClasses:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            for key, obj in models.storage.all().items():
                if obj.id == args[1] and obj.__class__.__name__ == args[0]:
                    print(obj.__str__())
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__myClasses:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            my_objs = models.storage.all()
            for k, obj in my_objs.items():
                if obj.id == args[1] and obj.__class__.__name__ == args[0]:
                    del(my_objs[k])
                    models.storage.save()
                    return
            print("** no instance found **")

    def do_all(self, args):
        '''all:
        Print a list of all active objects in storage.
        '''
        if args:
            try:
                getattr(models, args.split(' ')[0])
                print([str(models.storage.all()[key])
                      for key in models.storage.all()
                       if key.split('.')[0] == args])
            except Exception:
                return print("** class doesn't exist **")
        else:
            print([str(models.storage.all()[key])
                  for key in models.storage.all()])

    def do_update(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute """
        args = shlex.split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__myClasses:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            my_objs = models.storage.all()
            for i, obj in my_objs.items():
                if obj.id == args[1] and obj.__class__.__name__ == args[0]:
                    if len(args) == 2:
                        print("** attribute name missing **")
                        return
                    elif len(args) == 3:
                        print("** value missing **")
                        return
                    else:
                        new_att = args[3]
                        if hasattr(obj, str(args[2])):
                            new_att = (type(getattr(obj, args[2])))(args[3])
                        obj.__dict__[args[2]] = new_att
                        models.storage.save()
                        return
            print("** no instance found **")