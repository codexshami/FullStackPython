#find the intersection of two arrays
def intersection(arr1, arr2):          #create a function that takes two arrays as arguments
    set1 = set(arr1)                   #convert the first array to a set to remove duplicates and allow for efficient lookups
    set2 = set(arr2)                   #convert the second array to a set to remove duplicates and allow for efficient lookups
    return list(set1.intersection(set2))  #return the intersection of the two sets as a list
arr1 = [1, 2, 3, 4, 5]               #define the first array
arr2 = [4, 5, 6, 7, 8]               #define the second array
print(intersection(arr1, arr2))       #call the function and print the intersection of the two arrays
#logic method without function:
arr1 = [1, 2, 3, 4, 5]               #define the first array
arr2 = [4, 5, 6, 7, 8]               #define the second array
intersection_arr = []                 #initialize an empty list to store the intersection of the two arrays
for num in arr1:                    #loop through each number in the first array
    if num in arr2:                   #if the current number is also in the second array
        intersection_arr.append(num)    #append it to the intersection_arr list
print(intersection_arr)             #print the intersection of the two arrays