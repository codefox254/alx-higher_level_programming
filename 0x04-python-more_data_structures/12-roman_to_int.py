#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check if the input is valid
    if roman_string is None or type(roman_string) != str:
        return 0
    # Define a dictionary of Roman symbols and values
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # Initialize the result as zero
    result = 0
    # Loop through the characters of the Roman numeral
    for i in range(len(roman_string)):
        # Get the value of the current symbol
        value = data[roman_string[i]]
        # If the next symbol exists and is larger than the current one, subtract the value
        if i < len(roman_string) - 1 and data[roman_string[i + 1]] > value:
            result -= value
        # Otherwise, add the value
        else:
            result += value
    # Return the result
    return result
