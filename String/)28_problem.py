#Implement the strstr() function.
#Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
def strstr(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
# Get input from the user
haystack = input("Enter the haystack string: ")
needle = input("Enter the needle string: ")
# Find the index of the first occurrence of needle in haystack and print the result
result = strstr(haystack, needle)
if result != -1:
    print(f"The index of the first occurrence of '{needle}' in '{haystack}' is: {result}")  
else:    
    print(f"'{needle}' is not part of '{haystack}'.")

#Logic for interview
def strstr(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):  # Loop through the haystack string until the point where the remaining substring is shorter than the needle
        if haystack[i:i+len(needle)] == needle:  # Check if the substring of haystack starting at index i and of length equal to needle matches the needle
            return i  # If it matches, return the index i
    return -1  # If we finish the loop without finding a match, return -1
# Get input from the user
haystack = input("Enter the haystack string: ")
needle = input("Enter the needle string: ")
# Find the index of the first occurrence of needle in haystack and print the result
result = strstr(haystack, needle)
if result != -1:
    print(f"The index of the first occurrence of '{needle}' in '{haystack}' is: {result}")
else:
    print(f"'{needle}' is not part of '{haystack}'.")   
    
#time complexity: O((n-m+1)*m) where n is the length of the haystack and m is the length of the needle, because in the worst case we may need to check each substring of haystack against the needle. The space complexity is O(1) because we are using a constant amount of extra space.
