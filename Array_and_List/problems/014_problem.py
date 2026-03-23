#Remove duplicates from a sorted array

#short method:
def remove_duplicates(arr):          #create a function and pass the sorted array as an argument
    return list(set(arr))            #use the set data structure to remove duplicates and convert it back to a list
arr = [1, 2, 2, 3, 4, 4, 5]       #define a sorted array with some duplicate elements
print(remove_duplicates(arr))       #call the function and print the array with duplicates removed

#logic method without function:
arr = [1, 2, 2, 3, 4, 4, 5]       #define a sorted array with some duplicate elements
unique_arr = []                    #initialize an empty list to store unique elements
for i in range(len(arr)):          #loop through the array
    if i == 0 or arr[i] != arr[i - 1]:  #if it's the first element or the current element is not equal to the previous element
        unique_arr.append(arr[i])   #append the current element to the unique_arr list
print(unique_arr)                 #print the array with duplicates removed