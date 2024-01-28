#!/usr/bin/python3
""" Inheritance task module """


class MyList(list):
    """
    A class MyList that inherits from list
    """

    def print_sorted(self):
        """ A method tht prints the list in sorted form """

        if not isinstance(self, list):
            raise ValueError("List expected.")
        if None in self:
            raise ValueError("List elements must be numbers")
        if not all(isinstance(x, int) for x in self):
            raise ValueError("List must be a list of numbers.")

        print(sorted(self))
