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

    