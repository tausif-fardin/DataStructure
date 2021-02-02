# Using Divide and Conquer Strategy

def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)


element = 14
array = [10, 11, 12, 14, 144]
print(binary_search_recursive(array, element, 0, len(array)))
