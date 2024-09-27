# This program prints out a list of names, first in the original order and then in reverse order.

# Step 1: Create a list of names.
names = [
    'Biffle',  # First name in the list
    'Bowyer',  # Second name in the list
    'Busch',   # Third name in the list
    'Gordon',  # Fourth name in the list
    'Patrick'  # Fifth name in the list
]

# Step 2: Use a for loop to print each name in the original order.
# The 'end=" "' means the names will be printed on the same line, separated by spaces and '|'.
for name in names:
    print(name, '|', end=' ')  # This prints the name followed by a '|', but stays on the same line.

# Step 3: Move to a new line for the reverse printing.
print('\nPrinting in reverse:')  # The '\n' moves the print to the next line.

# Step 4: Use another for loop, but this time we use the reversed() function to print the names in reverse order.
for name in reversed(names):  # 'reversed()' gives the names in reverse order.
    print(name, '|', end=' ')  # This prints each name in reverse order, followed by a '|', and stays on the same line.
