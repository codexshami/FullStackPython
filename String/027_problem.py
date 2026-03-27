#Find the longest substring without repeating characters in a given string
def longest_substring_without_repeating_characters(s):
    char_index = {}
    longest = 0
    start = 0
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        longest = max(longest, i - start + 1)
    return longest
# Get input from the user
string = input("Enter a string: ")
# Find the longest substring without repeating characters and print the result
result = longest_substring_without_repeating_characters(string)
print(f"The length of the longest substring without repeating characters is: {result}")

#using logic for interview
def longest_substring_without_repeating_characters(s):
    char_index = {}  # Initialize a dictionary to store the last index of each character
    longest = 0  # Initialize a variable to keep track of the longest substring length
    start = 0  # Initialize a variable to keep track of the starting index of the current substring
    for i, char in enumerate(s):  # Iterate through the string with index and character
        if char in char_index and char_index[char] >= start:  # Check if the character has been seen before and is within the current substring
            start = char_index[char] + 1  # If it has, move the start index to one position after the last occurrence of the character
        char_index[char] = i  # Update the last index of the character
        longest = max(longest, i - start + 1)  # Update the longest length if the current substring is longer
    return longest  # Return the length of the longest substring without repeating characters
# Get input from the user
string = input("Enter a string: ")
# Find the longest substring without repeating characters and print the result
result = longest_substring_without_repeating_characters(string)
print(f"The length of the longest substring without repeating characters is: {result}")


#time complexity: O(n) where n is the length of the input string, because we need to iterate through the string once. The space complexity is O(min(m, n)) where m is the size of the character set and n is the length of the input string, because in the worst case we may need to store all characters in the current substring in the hash map.