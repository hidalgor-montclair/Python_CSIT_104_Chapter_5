# Let's loop through numbers 1 to 10 to demonstrate the 'break' and 'continue' statements.

# First, we'll show 'break' in action.
print("Demonstrating 'break':")

for i in range(1, 11):  # Loop from 1 to 10
    if i == 5:  # When 'i' equals 5, we want to stop the loop
        print(f"Breaking the loop at i = {i}")
        break  # This will exit the loop completely
    print(i)  # Print the current number if we're not breaking

print("\nDemonstrating 'continue':")

# Now, we'll show 'continue' in action.
for i in range(1, 11):  # Loop from 1 to 10
    if i == 5:  # When 'i' equals 5, we'll skip it
        print(f"Skipping the number {i}")
        continue  # This will skip the rest of the loop for 'i == 5'
    print(i)  # Print the current number if we're not skipping it

print("\nAll done!")
