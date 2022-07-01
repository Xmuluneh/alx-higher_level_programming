#!/usr/bin/python3
"""MY function text_indentation:
                               split special character

     """


def text_indentation(text):
    """Args:
         text a string type
         Raises:
             TypeError : if the text is not string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    special_character = ['.', ':', '?']
    for x in text:
        print(x, end="")
        if x in special_character:
            print("\n\n", end='')
