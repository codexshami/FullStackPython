#find the first non-repeating character in a string
def first_non_repeating_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

# Get input from the user
string = input("Enter a string: ")
# Find the first non-repeating character and print the result
result = first_non_repeating_char(string)
if result:
    print(f"The first non-repeating character is: {result}")
else:
    print("There is no non-repeating character.")

#using collections.OrderedDict
from collections import OrderedDict
def first_non_repeating_char(s):
    char_count = OrderedDict()
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char, count in char_count.items():
        if count == 1:
            return char
    return None

# Get input from the user
string = input("Enter a string: ")
# Find the first non-repeating character and print the result
result = first_non_repeating_char(string)
if result:
    print(f"The first non-repeating character is: {result}")
else:
    print("There is no non-repeating character.")

#using a list to maintain the order of characters
def first_non_repeating_char(s):
    char_count = {}
    char_order = []
    for char in s:
        if char not in char_count:
            char_count[char] = 1
            char_order.append(char)
        else:
            char_count[char] += 1
    for char in char_order:
        if char_count[char] == 1:
            return char
    return None
# Get input from the user
string = input("Enter a string: ")
# Find the first non-repeating character and print the result
result = first_non_repeating_char(string)   
if result:
    print(f"The first non-repeating character is: {result}")
else:
    print("There is no non-repeating character.")

#time complexity: O(n) where n is the length of the input string, since we traverse the string twice (once to count characters and once to find the first non-repeating character). The space complexity is O(k) where k is the number of unique characters in the string, due to the character count dictionary.