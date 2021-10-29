#!/usr/bin/python3
"""Console for AirBnB project"""
import cmd
import models
import readline


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

    if __name__ == '__main__':
        HBNBCommand().cmdloop()