#Replace a substring in a string
def replace_substring(s, old, new):
    return s.replace(old, new)  #Use the built-in replace() method to replace all occurrences of the old substring with the new substring in the string s. The result is returned.
# Get input from the user
string = input("Enter a string: ")
old_substring = input("Enter the substring to be replaced: ")
new_substring = input("Enter the new substring: ")
# Replace the substring and print the result
result = replace_substring(string, old_substring, new_substring)
print(f"String after replacement: {result}")

#Using logic for interview
def replace_substring(s, old, new):
    result = ""  # Initialize an empty string to store the result
    i = 0  # Initialize an index variable to keep track of our position in the string
    while i < len(s):  # Loop through the string until we reach the end
        if s[i:i+len(old)] == old:  # Check if the substring starting at index i matches the old substring
            result += new  # If it matches, append the new substring to the result
            i += len(old)  # Move the index forward by the length of the old substring
        else:
            result += s[i]  # If it doesn't match, append the current character to the result
            i += 1  # Move to the next character
    return result  # Return the final string with replacements
# Get input from the user
string = input("Enter a string: ")  
old_substring = input("Enter the substring to be replaced: ")
new_substring = input("Enter the new substring: ")
# Replace the substring and print the result
result = replace_substring(string, old_substring, new_substring)
print(f"String after replacement: {result}")
#time complexity: O(n*m) where n is the length of the input string and m is the length of the old substring, because in the worst case we may need to check each character of the string against the old substring. The space complexity is O(n) in the worst case, if all characters in the string are replaced
