def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


# Example usage
arr = [1, 3, 5, 7, 9]
target = 5
result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")