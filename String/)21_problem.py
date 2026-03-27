#Check teo srting are anagram or not
def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)
# Get input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
# Check if the strings are anagrams and print the result
if is_anagram(string1, string2):
    print("The strings are anagrams.")
else:    
    print("The strings are not anagrams.")

#Using collections.Counter
from collections import Counter
def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Use Counter to count the frequency of characters in both strings and compare
    return Counter(str1) == Counter(str2)
# Get input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
# Check if the strings are anagrams and print the result
if is_anagram(string1, string2):
    print("The strings are anagrams.")
else:    
    print("The strings are not anagrams.")

#using a dictionary to count character frequencies
def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Create a dictionary to count character frequencies for the first string
    char_count = {}
    
    # Count characters in the first string
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Subtract character counts based on the second string
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False  # If a character in str2 is not in str1, they are not anagrams
    
    # Check if all counts are zero
    return all(count == 0 for count in char_count.values())
# Get input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
# Check if the strings are anagrams and print the result
if is_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

#removing punctuation and special characters before checking for anagrams
import string
def is_anagram(str1, str2):
    # Remove spaces, punctuation, and convert to lowercase
    translator = str.maketrans("", "", string.punctuation)
    str1 = str1.replace(" ", "").translate(translator).lower()
    str2 = str2.replace(" ", "").translate(translator).lower()
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)
# Get input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
# Check if the strings are anagrams and print the result
if is_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

#time complexity of the above code is O(n log n) due to the sorting step, where n is the length of the strings. The space complexity is O(n) in the worst case if we consider the space used for the sorted lists or the character count dictionary.