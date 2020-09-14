def linear_search(arr, target):
    # Your code here
    if len(arr) == 0:
        return -1

    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1



# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    # Your code here
    while left <= right:
       midpoint = left + right // 2 # middle is one

       if arr[midpoint] == target:
           return midpoint

       if arr[midpoint] > target:
           right = midpoint - 1

       if arr[midpoint] < target:
            left = midpoint + 1


    return -1  # not found
arr = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
linear_search(arr, -6)


