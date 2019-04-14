

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if array:
        if array[0] == item: # base case - first index is key
            return index
        s = linear_search_recursive(array[1:], item, index+1) # recursion        
        if s is not False:
            print('here found s:', s)
            return s

    
    return None # returns false if key not found

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left = 0
    right = len(array) # O(n)
    # if left >= right: # edge case if we get an empty array
    #     return None 
    while left <= right: # what that condition is
        mid = right - left // 2
        if mid == item: # base base
            return mid 
        else:
            if array[mid] < item:
                right = mid - 1
            else: # array[mid] > item
                left = mid + 1

    return None # or raise error
    

def binary_search_recursive(array, item, left=0, right=None):
    if len(array) == 0:
        return None
    
    if right is None:
        right = len(array)-1

    if left > right:
        return None

    mid_index = (right + left) // 2
    mid = array[mid_index]
    # if mid > item and item > array[mid_index-1]:
    #     print('oh yes')
    #     return None
    # elif mid < item and item < array[mid_index-1]:
    #     print('oh yes')
        # return None
    # if mid_index == left or mid_index == right:
    #     return None
    if mid == item: # Base Case
        # print('mid == item HOORAY!', mid, item)
        return mid_index
    elif mid > item:
        # print('min > item', mid, item)
        return binary_search_recursive(array, item, left, mid_index -1)
    elif mid < item:
        return binary_search_recursive(array, item, mid_index + 1, right)

# print(binary_search_recursive([1,2,3,4,5,6,7,8,9,10], 2.5))