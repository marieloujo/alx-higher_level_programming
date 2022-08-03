#!/usr/bin/python3
"""
This is the "5-text_indentation" module.
The 5-text_indentation module supplies one function,
text_indentation(text):.
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): text should print
    """
    is_beginning_of_line = True
    if type(text) is not str:
        raise TypeError("text must be a string")
    for letter in text:
        if is_beginning_of_line:
            if letter == ' ':
                continue
        print(letter, end='')
        if letter in ".?:":
            print("\n")
            is_beginning_of_line = True
        elif letter == '\n':
            is_beginning_of_line = True
        else:
            is_beginning_of_line = False
