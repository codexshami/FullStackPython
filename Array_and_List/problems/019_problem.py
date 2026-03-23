#find the union of two arrays
def union(arr1, arr2):                 #create a function that takes two arrays as arguments
    set1 = set(arr1)                   #convert the first array to a set to remove duplicates and allow for efficient lookups
    set2 = set(arr2)                   #convert the second array to a set to remove duplicates and allow for efficient lookups
    return list(set1.union(set2))      #return the union of the two sets as a list
arr1 = [1, 2, 3, 4, 5]               #define the first array
arr2 = [4, 5, 6, 7, 8]               #define the second array
print(union(arr1, arr2))              #call the function and print the union of the two arrays
#logic method without function:
arr1 = [1, 2, 3, 4, 5]               #define the first array
arr2 = [4, 5, 6, 7, 8]               #define the second array
union_arr = []                        #initialize an empty list to store the union of the two arrays
for num in arr1:                    #loop through each number in the first array
    if num not in union_arr:           #if the current number is not already in the union_arr list
        union_arr.append(num)          #append it to the union_arr list
for num in arr2:                    #loop through each number in the second array
    if num not in union_arr:           #if the current number is not already in the union_arr list
        union_arr.append(num)          #append it to the union_arr list
print(union_arr)                 #print the union of the two arrays