'''
This program has a simple conversation with the user.
It uses `elif` branching and a random number to give different responses each time.
'''

# Step 1: Import the random library to generate random numbers.
import random  # This allows the program to generate random numbers.

# Step 2: Greet the user and give instructions.
print('Tell me something about yourself.')  # The program starts by asking the user to share something.
print('You can type \'Goodbye\' at anytime to quit.\n')  # Tells the user how to stop the program by typing "Goodbye."

# Step 3: Get input from the user.
# The user's response is stored in the variable 'user_text'.
user_text = input()  # Waits for the user to type something.

# Step 4: Start a loop that keeps running until the user types "Goodbye".
while user_text != 'Goodbye':
    
    # Step 5: Generate a random number between 0 and 2.
    # This random number will help pick which response the program gives.
    random_num = random.randint(0, 2)  # Creates a random number: either 0, 1, or 2.
    
    # Step 6: Use if-elif-else to decide what the program says back to the user.
    
    # If the random number is 0, the program asks the user to explain more.
    if random_num == 0:
        print('\nPlease explain further.\n')  # The program asks for more details.

    # If the random number is 1, the program repeats what the user said and asks "Why do you say that?"
    elif random_num == 1:
        print(f'\nWhy do you say: "{user_text}"?\n')  # Repeats the user's input and asks why they said it.

    # If the random number is 2, the program asks what else the user can share.
    elif random_num == 2:
        print('\nWhat else can you share?\n')  # Asks the user to share more information.

    # The else case is a backup if something unexpected happens, though this should not normally run.
    else:
        print('\nUh-oh, something went wrong. Try again.\n')  # Error message in case of an issue (though it's unlikely).

    # Step 7: Ask the user for more input and continue the conversation.
    # The loop will continue until the user types "Goodbye."
    user_text = input()  # Waits for the user to type another response.

# Step 8: When the user types "Goodbye," the loop ends and the program prints a farewell message.
print('It was nice talking with you. Goodbye.\n')  # The program ends with a friendly goodbye message.
