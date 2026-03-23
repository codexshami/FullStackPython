#check if an array is sorted

#short method:
def is_sorted(arr):                 #create a function and pass the array as an argument
    return arr == sorted(arr)       #compare the original array with the sorted version of the array and return True if they are the same, otherwise return False   
arr = [1, 2, 3, 4, 5]               #define an array with some elements
print(is_sorted(arr))                #call the function and print whether the array is sorted or not

#logic method without function:
arr = [1, 2, 3, 4, 5]               #define an array with some elements
is_sorted = True                    #initialize a variable to keep track of whether the array is sorted
for i in range(1, len(arr)):        #loop through the array starting from the second element
    if arr[i] < arr[i - 1]:         #if the current element is less than the previous element
        is_sorted = False           #set is_sorted to False and break out of the loop
        break
print(is_sorted)                    #print whether the array is sorted or not
