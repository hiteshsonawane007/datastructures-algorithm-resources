def linear_search(arr, target):  
    for index in range(len(arr)):  
        if arr[index] == target:  
            return index  # Return the index if the target is found  
    return -1  # Return -1 if the target is not found  

# Example usage  
numbers = [5, 3, 6, 2, 10]  
target_value = 6  
result = linear_search(numbers, target_value)  

if result != -1:  
    print(f"Target found at index: {result}")  
else:  
    print("Target not found.")