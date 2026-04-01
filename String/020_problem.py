#Reverse a string
s = input("Enter a string: ")   #Input string from user
print(s[::-1])                  #Use slicing to reverse the string. The [::-1] slice notation means to take the string and step backwards, effectively reversing it. The result is printed to the console.

#using for loop 
s = input("Enter a string: ")   #Input string from user
rev_str = ""                      #Initialize an empty string to store the reversed string
for char in s:
    rev_str = char + rev_str           #Prepend each character to the rev_str, effectively reversing the string
    print(rev_str)                      #Print the reversed string to the console


#Using recursion
def rev_string(s):            #Definition of a recursive function that takes a string as an argument
    if len(s) == 0:           #Base case: if the string is empty, return an empty string
        return s
    else:
        return rev_string(s[1:]) + s[0]   #Recursive case: call the function on the substring starting from the second character and append the first character at the end
s = input("Enter a string: ")   #Input string from user
print(rev_string(s))             #Call the recursive function and print the reversed string to the console

#using built-in function
s = input("Enter a string: ")   #Input string from user
print(''.join(reversed(s)))     #Use the built-in reversed() function to reverse the string and join the characters back together using ''.join(). The result is printed to the console.

#using stack
s = input("Enter a string: ")   #Input string from user
stack = []                      #Initialize an empty list to be used as a stack
for char in s:                    #Loop through each character in the input string
    stack.append(char)            #Push each character onto the stack
rev_str = ""                      #Initialize an empty string to store the reversed string
while stack:                       #While the stack is not empty
    rev_str += stack.pop()         #Pop characters from the stack and append them to rev_str, effectively reversing the string
print(rev_str)                      #Print the reversed string to the console

#using list comprehension
s = input("Enter a string: ")   #Input string from user
rev_str = ''.join([s[i] for i in range(len(s)-1, -1, -1)])  #Use a list comprehension to create a list of characters in reverse order and join them back together using ''.join(). The result is stored in rev_str.
print(rev_str)                      #Print the reversed string to the console

#using recursion with slicing
def rev_string(s):            #Definition of a recursive function that takes a string as an argument
    if len(s) == 0:           #Base case: if the string is empty, return an empty string
        return s
    else:
        return rev_string(s[1:]) + s[0]   #Recursive case: call the function on the substring starting from the second character and append the first character at the end
s = input("Enter a string: ")   #Input string from user
print(rev_string(s))             #Call the recursive function and print the reversed string to the console

#using recursion with slicing and a helper function
def rev_string_helper(s, index):  #Definition of a helper function that takes a string and an index as arguments
    if index < 0:              #Base case: if the index is less than 0, return an empty string
        return ""
    else:
        return s[index] + rev_string_helper(s, index - 1)  #Recursive case: append the character at the current index to the result of calling the helper function with the index decremented by 1
def rev_string(s):            #Definition of the main function that takes a string as an argument
    return rev_string_helper(s, len(s) - 1)  #Call the helper function with the string and the index of the last character
s = input("Enter a string: ")   #Input string from user
print(rev_string(s))             #Call the main function and print the reversed string to the console

#time complexity of all the above methods is O(n) where n is the length of the input string, as each method processes each character of the string once to reverse it.
    