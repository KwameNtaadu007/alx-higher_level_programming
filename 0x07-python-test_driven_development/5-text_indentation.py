#!/usr/bin/python3

"""
This Module defines a function that prints 2 new lines after ".?:" occur

"""

def text_indentation(text):
    """
    Prints two new lines after specific punctuation characters in the given text.

    Args:
        text (str): The input text to process.

    Raises:
        TypeError: If the `text` argument is not a string.

    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    #Punctuation characters that require two new lines
    punctuations = ".?:"

    #Make a copy of the original text
    processed_text = text

    #Iterate over each punctuation character
    for punctuation in punctuations:
        #Replace each occurrence of the punctuation character with the character followed by two new lines
        processed_text = processed_text.replace(punctuation, punctuation + "\n\n")

    #Print the processed text without the trailing new lines
    print(processed_text, end="")

