class Square:
    # Private instance attribute: size
    def __init__(self, size=0):
        # Instantiation with size
        self.size = size

    @property
    def size(self):
        # Property def size(self): to retrieve it
        return self.__size

    @size.setter
    def size(self, value):
        # Property setter def size(self, value): to set it
        # Size must be a number (float or integer), otherwise raise a TypeError exception with the message size must be a number
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        # If size is less than 0, raise a ValueError exception with the message size must be >= 0
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        # Public instance method: def area(self): that returns the current square area
        return self.size ** 2

    def __eq__(self, other):
        # Square instance can answer to comparators: ==, !=, >, >=, < and <= based on the square area
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

