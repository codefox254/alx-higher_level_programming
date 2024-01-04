# Import the function add from the file add_0.py
from add_0 import add

a = 1
b = 2

# Check if the code is executed directly or imported
if __name__ == "__main__":
# Print the result of the addition using the function add and the variables a and b
print("{} + {} = {}".format(a, b, add(a, b)))
