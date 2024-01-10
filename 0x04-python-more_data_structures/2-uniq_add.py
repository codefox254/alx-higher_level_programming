#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Use set to keep track of unique integers and sum them up
    unique_set = set(my_list)
    result = sum(unique_set)
    return result

# Example usage:
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
total = uniq_add(my_list)

print(total)
