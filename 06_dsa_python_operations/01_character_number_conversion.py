# Given a string containing letters and digits:

# Input: "aB3x7Z2"

# For every character:

# If it is a digit → convert it to integer.
# If it is a lowercase letter → find its alphabet position.
# If it is uppercase → convert it to lowercase and find its alphabet position.

from typing import List

def convert_character(input_string: str) -> List[int]:

    result = []

    for char in input_string:
    
        if char.isdigit():
            result.append(ord(char)-ord('0'))
        elif char.islower():
            result.append(ord(char)-97)
        elif char.isupper():
            result.append(ord(char.lower())-97)

    return result


result = convert_character("aB3x7Z2")

print(result)
