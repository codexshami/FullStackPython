#Merge two soted array
def merge_sorted_arrays(arr1, arr2):  #create a function that takes two sorted arrays as arguments
    merged_array = []                 #initialize an empty list to store the merged array
    i = j = 0                         #initialize two pointers for each array
    while i < len(arr1) and j < len(arr2):  #loop until we reach the end of either array
        if arr1[i] < arr2[j]:         #if the current element in arr1 is smaller than the current element in arr2
            merged_array.append(arr1[i])  #append the current element from arr1 to the merged array
            i += 1                    #move the pointer for arr1 to the next element
        else:                         #if the current element in arr2 is smaller than or equal to the current element in arr1
            merged_array.append(arr2[j])  #append the current element from arr2 to the merged array
            j += 1                    #move the pointer for arr2 to the next element
    while i < len(arr1):              #if there are remaining elements in arr1 after one of the arrays has been fully traversed
        merged_array.append(arr1[i])   #append them to the merged array
        i += 1                        #move the pointer for arr1 to the next element
    while j < len(arr2):              #if there are remaining elements in arr2 after one of the arrays has been fully traversed
        merged_array.append(arr2[j])   #append them to the merged array
        j += 1                        #move the pointer for arr2 to the next element
    return merged_array               #return the merged array
arr1 = [1, 3, 5]                    #define the first sorted array
arr2 = [2, 4, 6]                    #define the second sorted array
print(merge_sorted_arrays(arr1, arr2))  #call the function and print the merged sorted array
