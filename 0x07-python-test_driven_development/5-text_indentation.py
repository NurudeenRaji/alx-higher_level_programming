#!/usr/bin/python3
"""
A function to print a text
"""


def text_indentation(text):
    """
    prints a text with 2 newlines after these characters: ., ? and :

    text_indentation: name of function
    text(param): the text to print
    return: nothing
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in [".", "?", ":"]:
        text = text.replace(i, i + "\n\n")

    lines = text.splitlines()

    for line in lines:
        print(line.strip())
