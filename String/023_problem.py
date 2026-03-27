#count the frequency of each character in the string and return the first character that has a frequency of 1
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

#time complexity: O(n) where n is the length of the input string, because we need to iterate through the string twice (once to count the characters and once to find the first non-repeating character). The space complexity is also O(n) in the worst case, if all characters in the string are unique.