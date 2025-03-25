def selection_sort(arr):  
    n = len(arr)  
    # Traverse through all array elements  
    for i in range(n):  
        # Assume the minimum is the first element of the unsorted part  
        print(i)
        min_index = i  
        # Iterate through the unsorted portion of the array  
        for j in range(i+1, n):  
            # Update min_index if the element at j is less than the current minimum  
            if arr[j] < arr[min_index]:  
                min_index = j  
        # Swap the found minimum element with the first element  
        arr[i], arr[min_index] = arr[min_index], arr[i]  

# Example usage  
array = [64, 34, 25, 12, 22, 11, 90]  
selection_sort(array)  
print("Sorted array:", array)