# This is our starting power of 2, starting at 2.
curr_power = 2

# 'user_char' is a variable that stores the user's response. 
# It starts as 'y' (which means "yes") so the loop will run at least once.
user_char = 'y'

# This while loop will keep running as long as 'user_char' is 'y'.
while user_char == 'y':
    
    # Print the current power of 2.
    print(curr_power)
    
    # Multiply 'curr_power' by 2 to get the next power of 2.
    curr_power = curr_power * 2
    
    # Ask the user if they want to continue the loop. 
    # If they type 'y', the loop will run again. If they type anything else, the loop will stop.
    user_char = input("Do you want to continue? Type 'y' for yes or anything else to stop: ")

# When the loop finishes, print 'Done' to indicate that the program is over.
print('Done')
