#Remove all vowels from a string
def remove_vowels(s):
    vowels = "aeiouAEIOU"  # Define a string containing all vowels (both lowercase and uppercase)
    return ''.join(char for char in s if char not in vowels)  # Use a generator expression to create a new string that includes only characters that are not vowels, and join them together
# Get input from the user
string = input("Enter a string: ")
# Remove vowels from the input string and print the result
result = remove_vowels(string)
print(f"String after removing vowels: {result}")

#using logic fo interview
def remove_vowels(s):
    vowels = "aeiouAEIOU"  # Define a string containing all vowels (both lowercase and uppercase)
    result = ""  # Initialize an empty string to store the result
    for char in s:  # Iterate through each character in the input string
        if char not in vowels:  # Check if the character is not a vowel
            result += char  # If it's not a vowel, append it to the result string
    return result  # Return the final string with vowels removed
# Get input from the user
string = input("Enter a string: ")
# Remove vowels from the input string and print the result
result = remove_vowels(string)
print(f"String after removing vowels: {result}")


#time complexity: O(n) where n is the length of the input string, because we need to iterate through the string once to check each character. The space complexity is O(n) in the worst case, if all characters in the string are consonants and we need to create a new string that is the same length as the input string.