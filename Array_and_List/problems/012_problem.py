#Reverse and array

#short method:
def reverse(arr):                   #create a function and pass the array as an argument
    return arr[::-1]                #use slicing to reverse the array and return it 
arr = [1, 2, 3, 4, 5]               #define an array with some elements
print(reverse(arr))                 #call the function and print the reversed array

#logic method without function:
arr = [1, 2, 3, 4, 5]               #define an array with some elements
for i in range(len(arr) // 2):      #loop through half the length of the array
    arr[i], arr[-(i + 1)] = arr[-(i + 1)], arr[i]  #swap the elements at symmetric positions
print(arr)                          #print the reversed array
