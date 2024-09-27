# List of names
names = ['Janice', 'Clarice', 'Martin', 'Veronica', 'Jason']

# Ask the user how many names they want to print
num = int(input('Enter number of names to print: '))

# Loop through the 'names' list
for i in range(len(names)):  # 'i' is a number that goes from 0 to the length of the 'names' list
    if i == num:  # When 'i' reaches the number entered by the user, stop the loop
        break  # This 'break' statement will stop the loop if 'i' equals the input number
    print(names[i], end=' ')  # Print each name in the list on the same line, followed by a space

# The 'else' here only happens if the loop finishes without a 'break'
else:
    print()
    print('All names printed.')  # This will print if the loop was not stopped early

# Example:
# If the user enters '3', the output will be: 'Janice Clarice Martin'
# If the user enters '5', the output will be: 'Janice Clarice Martin Veronica Jason All names printed.'
