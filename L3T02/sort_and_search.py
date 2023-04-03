# My suggest would be a Binary Search

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
target = 9

result = binary_search(arr, target)

if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found in array")


# This implementation first initializes left and right indices to the beginning and end of the array, respectively. It then repeatedly computes the middle index mid of the remaining search interval and compares the value at that index to the target value. If the value at mid is equal to the target, the algorithm returns the index of mid. If the value at mid is less than the target, the search interval is narrowed to the right half of the remaining search space, and the algorithm repeats the process. Similarly, if the value at mid is greater than the target, the search interval is narrowed to the left half of the remaining search space.

# I think binary search is a good choice in this case because the given array is not initially sorted, but it can be easily sorted using a sorting algorithm such as quicksort or mergesort. Once the array is sorted, binary search can be used to efficiently locate the index of the target value. Compared to linear search, which would require iterating over each element of the array in the worst case, binary search has a time complexity of O(log n), where n is the size of the array, making it much more efficient for large arrays.

# -----------------------------------------------------------------------#
# Research and implement the Insertion sort on this array

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
insertion_sort(arr)
print(arr)

# -----------------------------------------------------------------------#

# Implement a searching algorithm you haven’t tried yet in this Task on the
# sorted array to find the number 9. Add a comment to explain where you
# would use this algorithm in the real world.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
target = 9

result = linear_search(arr, target)

if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found in array")
