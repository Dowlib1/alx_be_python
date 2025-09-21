# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Validate that the input is positive
while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))

# Initialize row counter for while loop
row = 1

# Use while loop for rows
while row <= size:
    # Use for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    # Print newline after each row
    print()
    row += 1
