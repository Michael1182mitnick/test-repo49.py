# Write a Python program to create a dictionary and retrieve the value for a given key.

# Create a dictionary with some key-value pairs
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# Function to retrieve the value for a given key


def get_value_from_dict(dictionary, key):
    # Check if the key exists in the dictionary
    if key in dictionary:
        return dictionary[key]
    else:
        return "Key not found in the dictionary"


# Example usage
key_to_find = input("Enter the key you want to find: ")
value = get_value_from_dict(my_dict, key_to_find)
print(f"The value for the key '{key_to_find}' is: {value}")
