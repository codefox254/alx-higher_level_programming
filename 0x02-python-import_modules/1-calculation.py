# Import the functions add, sub, mul, and div from the file calculator_1.py
from calculator_1 import add, sub, mul, div

a = 10
b = 5

# Check if the code is executed directly or imported
if __name__ == "__main__":
# Print the result of the addition using the function add and the variables a and b
print("{} + {} = {}".format(a, b, add(a, b)))
# Print the result of the subtraction using the function sub and the variables a and b
print("{} - {} = {}".format(a, b, sub(a, b)))
# Print the result of the multiplication using the function mul and the variables a and b
print("{} * {} = {}".format(a, b, mul(a, b)))
# Print the result of the division using the function div and the variables a and b
print("{} / {} = {}".format(a, b, div(a, b)))
