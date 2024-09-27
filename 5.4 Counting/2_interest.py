'''
Program that calculates savings and interest over a number of years.
'''

# Step 1: Set up initial savings and interest rate.
initial_savings = 10000  # The starting amount of money in savings.
interest_rate = 0.05  # 5% yearly interest rate (0.05 represents 5%).

# Step 2: Display the initial savings and interest rate to the user.
print(f'Initial savings of ${initial_savings}')  # Prints the initial savings amount.
print(f'at {interest_rate*100:.0f}% yearly interest.\n')  # Converts the interest rate to a percentage and displays it.

# Step 3: Ask the user for the number of years they want to calculate the savings for.
years = int(input('Enter years: '))  # The user inputs the number of years.
print()  # Prints a blank line for clarity in the output.

# Step 4: Initialize the savings to the initial savings amount.
savings = initial_savings

# Set up a loop variable to track which year we are on.
i = 1  # Loop variable, starts at year 1.

# Step 5: Loop through each year to calculate the savings.
while i <= years:  # The loop will run for the number of years the user entered.
    
    # Display the savings at the beginning of each year.
    print(f' Savings at beginning of year {i}: ${savings:.2f}')  # Shows the savings for the current year, formatted to 2 decimal places.
    
    # Calculate the new savings amount by adding interest.
    # The interest is calculated as 'savings * interest_rate', and it is added to the savings.
    savings = savings + (savings * interest_rate)
    
    # Move to the next year.
    i = i + 1  # Increment the year by 1 for the next loop.

# Step 6: After the loop finishes, print a blank line for spacing.
print('\n')
