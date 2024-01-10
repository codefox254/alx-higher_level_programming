#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Check if the index is within the valid range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Use list slicing to delete the element at the specified index
    new_list = my_list[:idx] + my_list[idx + 1:]

    return new_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3

    # Call the delete_at function
    new_list = delete_at(my_list, idx)

    # Print the results
    print(new_list)
    print(my_list)
