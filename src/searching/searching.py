# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start >= end:
        return -1

    mid = int(len(arr[start:end+1])/2) + start

    if arr[mid] == target:
        return mid
        
    elif arr[mid] > target:
        end = mid
        
    else:
        start = mid

    return binary_search(arr, target, start, end)
        
        

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

