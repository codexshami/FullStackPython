#find the second largest element in an array
#short method:
def second_largest(arr):            #create a function and pass the array as an argument
    unique_arr = list(set(arr))     #use a set to remove duplicates and convert it back to a list
    unique_arr.sort()              #sort the unique elements in ascending order
    return unique_arr[-2]          #return the second last element, which is the second largest
arr = [3, 5, 7, 2, 8]               #define an array with some elements
print(second_largest(arr))         #call the function and print the second largest element
#logic method without function:
arr = [3, 5, 7, 2, 8]               #define an array with some elements
largest = second_largest = float('-inf')  #initialize largest and second_largest to negative infinity
for num in arr:                    #loop through each number in the array
    if num > largest:               #if the current number is greater than the largest found so far
        second_largest = largest     #update second_largest to be the old largest
        largest = num               #update largest to be the current number
    elif largest > num > second_largest:  #if the current number is between largest and second_largest
        second_largest = num         #update second_largest to be the current number    
print(second_largest)             #print the second largest element