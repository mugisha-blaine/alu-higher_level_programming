#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    length = 0
    while length < len(text) and text[length] == ' ':
        length += 1

    while length < len(text):
        print(text[length], end="")
        if text[length] == "\n" or text[length] in ".?:":
            if text[length] in ".?:":
                print("\n")
            length += 1
            while length < len(text) and text[length] == ' ':
                length += 1
            continue
        length += 1
