# simple_utils.py - A tiny utility library

def reverse_string(text):
    """Reverses the characters in a string."""
    return text[::-1]

def count_words(sentence):
    """
    Return the number of words in a sentence.
    
    Counts tokens produced by splitting the input string on any whitespace (str.split()),
    so consecutive whitespace is treated as a single separator and leading/trailing whitespace is ignored.
    
    Parameters:
        sentence (str): Input text to count words in.
    
    Returns:
        int: Number of words (0 if the input is empty or contains only whitespace).
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from degrees Celsius to degrees Fahrenheit.
    
    Parameters:
        celsius (float | int): Temperature in degrees Celsius.
    
    Returns:
        float: Temperature converted to degrees Fahrenheit using F = (C * 9/5) + 32.
    """
    return (celsius * 9/5) + 32