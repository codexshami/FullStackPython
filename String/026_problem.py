#Check if a string is a valid palindrome
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Get input from the user
string = input("Enter a string: ")
# Check if the string is a valid palindrome and print the result
if is_palindrome(string):
    print(f"'{string}' is a valid palindrome.")
else:
    print(f"'{string}' is not a valid palindrome.")

# Using two pointers to check for palindrome
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        # Move left pointer to the next alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer to the previous alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1
        # Compare characters at left and right pointers (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
# Get input from the user
string = input("Enter a string: ")
# Check if the string is a valid palindrome and print the result
if is_palindrome(string):
    print(f"'{string}' is a valid palindrome.")
else:    
    print(f"'{string}' is not a valid palindrome.")

# Time complexity: O(n) where n is the length of the input string, because we need to iterate through the string once to clean it and once to check if it's a palindrome. The space complexity is O(n) in the worst case, if all characters in the string are alphanumeric and we need to create a new string that is the same length as the input string.  