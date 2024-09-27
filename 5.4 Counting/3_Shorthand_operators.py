# This program demonstrates a shorthand way to update a loop variable.
# We'll show both the short and long versions of the code.

# Step 1: Initialize the loop variable.
i = 0  # 'i' is our loop variable. It starts at 0.

# Assume 'N' is the number of times we want the loop to run.
N = int(input("Enter the number of times to repeat: "))  # Ask the user for how many times to repeat the loop.

# Step 2: Start the loop that runs as long as i is less than N.
while i < N:
    # Inside the loop, we can do any task. Let's print the current value of 'i'.
    print(f'Short version - Loop iteration {i}')  # Prints the value of 'i' before updating it.

    # Step 3: This is the shorthand operator that adds 1 to 'i'.
    i += 1  # Shorthand for i = i + 1 (this makes 'i' increase by 1 each time).

# After the loop runs with the shorthand operator, let's reset 'i' to 0 and show the longer version.

# Step 4: Now we show the longer equivalent of the shorthand operator.
i = 0  # Reset 'i' back to 0.

# Run the loop again using the longer version of the code.
while i < N:
    # Inside the loop, we can do any task. Let's print the current value of 'i'.
    print(f'Long version - Loop iteration {i}')  # Prints the value of 'i' before updating it.

    # Step 5: This is the longer version of updating 'i'.
    i = i + 1  # This is the longer way of saying "i += 1". It means the same thing.

