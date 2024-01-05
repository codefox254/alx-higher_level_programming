#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Use the value 0 for each missing integer if the tuple is smaller than 2
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Return a tuple with the addition of the first and second elements of each argument
    result_tuple = (a[0] + b[0], a[1] + b[1])
    return result_tuple

if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)

    # Test the add_tuple function with different scenarios
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1,)))
    print(add_tuple(tuple_a, ()))
