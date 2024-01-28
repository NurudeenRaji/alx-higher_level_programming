#!/usr/bin/python3
""" Inheritance task module """


class MyList(list):
    """
    A class MyList that inherits from list
    """

    def print_sorted(self):
        """ A method tht prints the list in sorted form """

        print(sorted(self))
