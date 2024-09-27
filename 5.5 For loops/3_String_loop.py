# This program adds an underscore ('_') after every character in the string "Take me to the moon."

# Step 1: Create an empty string called 'my_str' that will hold the new string with underscores.
my_str = ''  # This starts as an empty string, but we will keep adding to it.

# Step 2: Use a for loop to go through each character in the sentence "Take me to the moon."
for character in "Take me to the moon.":  # 'character' will be each letter or symbol in the string.
    
    # Step 3: Add the current character followed by an underscore to 'my_str'.
    my_str += character + '_'  # For each character, we add it and an underscore to 'my_str'.

# Step 4: Print the final result after the loop finishes.
print(my_str)  # This prints the new string with an underscore after every character.
