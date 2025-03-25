def binary_search(arr, target):  
    left, right = 0, len(arr) - 1  
    
    while left <= right:  
        mid = left + (right - left) // 2  # To avoid potential overflow  
        print(mid)
        
        # Check if the target is present at mid  
        if arr[mid] == target:  
            return mid  # Target found  
        # If target is greater, ignore the left half  
        elif arr[mid] < target:  
            left = mid + 1  
        # If target is smaller, ignore the right half  
        else:  
            right = mid - 1  
    
    return -1  # Target not found  

# Example usage:  
numbers = [1, 3, 5, 7, 9, 11, 13]  
target = 7  
result = binary_search(numbers, target)  

if result != -1:  
    print(f"Element found at index {result}")  
else:  
    print("Element not found in the array")