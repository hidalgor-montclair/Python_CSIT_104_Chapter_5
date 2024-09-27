# This program calculates the total revenue for the week and the average daily revenue.

# Step 1: A list of daily revenues is created, where each element represents the revenue for a day of the week.
daily_revenues = [
    2356.23,  # Monday's revenue
    1800.12,  # Tuesday's revenue
    1792.50,  # Wednesday's revenue
    2058.10,  # Thursday's revenue
    1988.00,  # Friday's revenue
    2002.99,  # Saturday's revenue
    1890.75   # Sunday's revenue
]

# Step 2: Initialize a variable 'total' to store the sum of all daily revenues.
total = 0  # This starts at 0, and we'll add each day's revenue to it.

# Step 3: Use a for loop to go through each day's revenue and add it to the total.
for day in daily_revenues:  # The loop goes through each value (revenue) in the 'daily_revenues' list.
    total += day  # This adds the current day's revenue to 'total'.

# Step 4: Calculate the average revenue by dividing the total by the number of days.
# len(daily_revenues) gives us the number of days (which is 7 in this case).
average = total / len(daily_revenues)

# Step 5: Print the total revenue for the week, formatted to 2 decimal places.
print(f'Weekly revenue: ${total:.2f}')  # Displays the total revenue with two decimal places.

# Step 6: Print the average daily revenue, formatted to 2 decimal places.
print(f'Daily average revenue: ${average:.2f}')  # Displays the average revenue with two decimal places.
