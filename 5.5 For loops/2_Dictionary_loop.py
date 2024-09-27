# This program shows the channel number for different TV channels using a dictionary.

# Step 1: Create a dictionary named 'channels' where each key is a TV channel name, 
# and the value is the corresponding channel number.
channels = {
    'MTV': 35,  # MTV is on channel 35.
    'CNN': 28,  # CNN is on channel 28.
    'FOX': 11,  # FOX is on channel 11.
    'NBC': 4,   # NBC is on channel 4.
    'CBS': 12   # CBS is on channel 12.
}

# Step 2: Use a for loop to go through each channel in the dictionary.
for c in channels:  # 'c' will be each TV channel name (the keys in the dictionary).
    
    # Step 3: Print the channel name and its corresponding number.
    # 'channels[c]' is how we access the value (channel number) for each key (TV channel).
    print(f'{c} is on channel {channels[c]}')  # This will print something like "MTV is on channel 35".
