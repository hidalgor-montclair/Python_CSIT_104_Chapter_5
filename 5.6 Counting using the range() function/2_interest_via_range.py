'''Program that calculates savings and interest over a number of years.'''

# Step 1: Set the initial savings amount and the interest rate.
initial_savings = 10000  # You start with $10,000 in savings.
interest_rate = 0.05  # The interest rate is 5%, which means you gain 5% more money every year.

# Step 2: Ask the user to input the number of years.
# This will tell the program how many years to calculate interest for.
years = int(input('Enter years: '))  # The user enters how many years they want to calculate savings for.
print()  # Prints a blank line for neat output.

# Step 3: Initialize the savings to the initial savings amount.
savings = initial_savings  # Start with the initial savings value of $10,000.

# Step 4: Use a for loop to calculate and print the savings for each year.
# The 'range(years)' will make the loop run as many times as the number of years entered.
for i in range(years):  # 'i' starts at 0 and increases by 1 each loop until it reaches the number of years.
    # Step 5: Print the savings for the current year.
    # 'i' is the current year, and 'savings' is the amount you have for that year.
    print(f' Savings in year {i}: ${savings:.2f}')  # Displays the savings for each year with two decimal places.
    
    # Step 6: Update the savings by adding the interest.
    # The interest is calculated as 'savings * interest_rate', which is added to the current savings.
    savings = savings + (savings * interest_rate)  # Update savings with the new amount, including the interest.

# Step 7: After the loop finishes, print a blank line for spacing.
print('\n')  # This adds an extra blank line after the loop for better readability.
