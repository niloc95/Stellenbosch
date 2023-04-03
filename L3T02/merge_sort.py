def merge_sort_strings_by_length(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort_strings_by_length(left)
    right = merge_sort_strings_by_length(right)

    return merge_strings_by_length(left, right)

def merge_strings_by_length(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if len(left[i]) >= len(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

# Define three lists of strings
list1 = ["apple", "banana", "orange", "grapefruit", "pear", "watermelon", "kiwi", "pineapple", "mango", "pomegranate"]
list2 = ["cat", "dog", "elephant", "giraffe", "rhinoceros", "lion", "tiger", "zebra", "hippopotamus", "monkey"]
list3 = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "black"]

# Sort the lists by string length
sorted_list1 = merge_sort_strings_by_length(list1)
sorted_list2 = merge_sort_strings_by_length(list2)
sorted_list3 = merge_sort_strings_by_length(list3)

# Print the sorted lists
print("Sorted list 1:")
print(sorted_list1)

print("Sorted list 2:")
print(sorted_list2)

print("Sorted list 3:")
print(sorted_list3)
