# Import things as these are very important for printing stuff on console
from random import randrange as rand
from time import sleep


# A very beautiful function which will keep printing a string with a random character, until the expected character
# is drawn
def print_string(current_string, expected_character):
    while True:
        some_random_character = rand(0, 127)
        print("\r" + current_string + chr(some_random_character), end="")
        sleep(0.1)  # Comment this line to see the result instantly
        if chr(some_random_character) == expected_character:
            break


my_string = "Hello World"
current_str = ""

# Try to get the matching character for every character in the string. Good Luck!
for letter in my_string:
    print_string(current_str, letter)
    current_str += letter
