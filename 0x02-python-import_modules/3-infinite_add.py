# Import the sys module to access the command-line arguments
import sys

# Check if the code is executed directly or imported
if __name__ == "__main__":
# Initialize a variable to store the sum of the arguments
sum = 0
# Loop through the arguments, starting from the second one (the first one is the file name)
for arg in sys.argv[1:]:
# Cast the argument into an integer and add it to the sum
sum += int(arg)
# Print the sum, followed by a new line
print(sum)
