#!/usr/bin/python3
class Square:
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

# Testing the Square class
if __name__ == "__main__":
    my_square = Square(3)

    # Printing the type of my_square and its attributes
    print(type(my_square))
    print(my_square.__dict__)

    try:
        # Attempting to access size directly (will raise an error)
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        # Attempting to access __size directly (will raise an error)
        print(my_square.__size)
    except Exception as e:
        print(e)

