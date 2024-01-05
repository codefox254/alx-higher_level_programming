#!/usr/bin/python3

def max_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return None

    # Initialize max_value with the first element of the list
    max_value = my_list[0]

    # Iterate through the list to find the maximum value
    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value

if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]

    # Call the max_integer function
    max_value = max_integer(my_list)

    # Print the result
    print("Max: {}".format(max_value))
