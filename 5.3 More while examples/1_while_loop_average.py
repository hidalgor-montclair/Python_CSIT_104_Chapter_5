'''
This program calculates the average of a list of positive integers.
The list of numbers ends when the user enters 0, which is called a sentinel value.
Example: If you input 10, 1, 6, 3, 0, it will calculate the average as (10 + 1 + 6 + 3) / 4 = 5.
'''

# Step 1: Initialize the sum of the values and the number of values.
# These variables will keep track of the total sum of the numbers and how many numbers have been entered.
values_sum = 0  # This variable will hold the sum of all the numbers.
num_values = 0  # This variable will count how many numbers were entered.

# Step 2: Ask the user to input the first number.
# The first number entered by the user will be stored in 'curr_value'.
curr_value = int(input("Enter a positive number (or 0 to stop): "))

# Step 3: Start the while loop to get more numbers.
# The loop will keep running as long as the number entered is greater than 0.
while curr_value > 0:
    
    # Add the current number to the sum of all previous numbers.
    values_sum += curr_value  # This updates the total sum by adding the current value to 'values_sum'.
    
    # Increase the count of numbers by 1.
    num_values += 1  # This counts how many numbers have been entered.
    
    # Ask the user to enter another number.
    curr_value = int(input("Enter another positive number (or 0 to stop): "))

# Step 4: Once the user enters 0, the loop ends, and the average is calculated and displayed.
# The average is calculated by dividing the total sum by the number of values entered.
# We also round the average to 0 decimal places using ':0f' for easy reading.
print(f'Average: {values_sum / num_values:.0f}')  # This prints the average as a whole number.
