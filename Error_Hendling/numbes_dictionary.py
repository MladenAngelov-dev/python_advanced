numbers_dictionary = {}  # Create an empty dictionary to store key-value pairs.

line = input()
while line != "Search":
    number_as_string = line

    try:
        # Try to convert the next input to an integer and add it to the dictionary.
        number = int(input())
        numbers_dictionary[number_as_string] = number

    except ValueError:
        # Handle the case where the input is not a valid integer.
        print("The variable number must be an integer")

    line = input()

line = input()
while line != "Remove":
    searched = line

    try:
        # Try to print the value associated with the key in the dictionary.
        print(numbers_dictionary[searched])
    except KeyError:
        # Handle the case where the key does not exist in the dictionary.
        print("Number does not exist in dictionary")

    line = input()

line = input()

while line != "End":
    # Store the user input as the key to be removed.
    searched = line

    try:
        # Try to delete the key-value pair from the dictionary.
        del numbers_dictionary[searched]
    except KeyError:
        # Handle the case where the key does not exist in the dictionary.
        print("Number does not exist in dictionary")

    line = input()

print(numbers_dictionary)
