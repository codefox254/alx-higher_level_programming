#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Create a new list to store True or False
    result_list = []

    # Iterate through the original list
    for num in my_list:
        # Check if the number is divisible by 2
        is_divisible = num % 2 == 0
        # Append the result to the new list
        result_list.append(is_divisible)

    return result_list

if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]

    # Call the divisible_by_2 function
    list_result = divisible_by_2(my_list)

    # Iterate through the lists to print results
    i = 0
    while i < len(list_result):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
        i += 1
