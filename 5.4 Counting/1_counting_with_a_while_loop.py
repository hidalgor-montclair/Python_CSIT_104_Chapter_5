# This program demonstrates how to repeat something N times using a loop.

# Step 1: Initialize the loop variable.
i = 1  # This variable 'i' starts at 1 and will help us count how many times the loop runs.

# We assume 'N' is the number of times we want to run the loop.
# Example: If N = 5, the loop will repeat 5 times.
N = int(input("Enter the number of times to repeat: "))  # Ask the user how many times they want to repeat.

# Step 2: Start the while loop, which runs as long as i is less than or equal to N.
while i <= N:
    
    # Inside the loop, you can put any task you want to repeat.
    # For now, let's just print the value of 'i' to show the loop running.
    print(f'Loop iteration {i}')  # This shows the current loop count.

    # Step 3: Increment the loop variable by 1 each time.
    # This makes sure the loop moves to the next number until it reaches N.
    i = i + 1  # Add 1 to 'i' to move to the next loop iteration.
