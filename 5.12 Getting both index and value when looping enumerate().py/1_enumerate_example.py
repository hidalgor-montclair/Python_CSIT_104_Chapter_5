# Normal list of items (fruits)
fruits = ['apple', 'banana', 'cherry', 'date']

# First: Normal list iteration (without enumerate)
print("Normal list iteration (without index):")
for fruit in fruits:
    print(f"Fruit: {fruit}")  # We only get the fruit value, no index

print("\n")  # Adds a blank line to separate outputs for clarity

# Second: Using enumerate() to get both index and value
print("List iteration using enumerate (with index and value):")
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")  # We get both index and value

