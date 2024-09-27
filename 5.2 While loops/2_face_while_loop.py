nose = '0'  # This variable represents a nose and looks like the number zero.

# Get the first character from the user to represent the eyes and mouth.
user_input = input("Enter a character ('q' for quit): ")  # Asks the user to input a character.
user_value = user_input[0]  # Takes the first character from the user's input.

# The loop will continue as long as the user doesn't enter 'q' (which means "quit").
while user_value != 'q':
    # This prints the eyes using the character the user entered.
    # Example: If the user enters '*', the output would be ' * * '.
    print(f' {user_value} {user_value} ')
    
    # This prints the nose, which is always '0'.
    # Example: The nose is printed as ' 0 ' in the middle.
    print(f'  {nose}  ')
    
    # This prints the mouth using the same character as the eyes, repeated 5 times.
    # Example: If the user enters '*', the output would be '*****' for the mouth.
    print(user_value * 5)
    
    # This creates a blank line to separate each face.
    print('\n')

    # Ask the user again for another character or 'q' to quit.
    user_input = input("Enter a character ('q' for quit): ")  # The program waits for new input.
    user_value = user_input[0]  # Takes the first character from the user's input.

# When the user enters 'q', the loop stops, and the program says goodbye.
print('Goodbye.\n')  # The program ends with a friendly message.
