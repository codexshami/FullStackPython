#Find the Largest element in array 

#short method:

def largest(arr):                   #create a function and pass the array as an argument
    return max(arr)                 #use the built-in max() function to find and return the largest element in the array
arr = [3, 5, 7, 2, 8]               #define an array with some elements
print(largest(arr))                 #call the function and print the largest element

#logic method without function:

arr = [3, 5, 7, 2, 8]               #define an array with some elements
largest = arr[0]                    #initialize largest variable with the first element of the array
for i in range(1, len(arr)):        #loop through the rest of the elements in the array
    if arr[i] > largest:            #if the current element is greater than the largest element found so far
        largest = arr[i]            #update the largest variable with the current element
print(largest)                      #print the largest element