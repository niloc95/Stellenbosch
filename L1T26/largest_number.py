def largest_number(lst):
    # Base case: The list has only one element, return that element
    if len(lst) == 1:
        return lst[0]
    else:
        # Recursive case: we calling largest_number on the sub-list starting from the second element
        max_num = largest_number(lst[1:])
        # Compare the first element of the original list to the maximum number found in the sub-list
        if lst[0] > max_num:
            # If the first element is greater, return it as the maximum
            return lst[0]
        else:
            # Otherwise, return the maximum number found in the sub-list
            return max_num

print(largest_number([1, 4, 5, 3]))  # Output: 5
print(largest_number([3, 1, 6, 8, 2, 4, 5]))  # Output: 8

def foo(a, b=4, c=6):
    print( b, c)
 
foo(20, c=12)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)