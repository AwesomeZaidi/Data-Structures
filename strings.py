#!python

# Helper Function(s)
def find_pattern_index(text, pattern, list = None):
    '''
        Goes through text array to find a pattern, returns index where it's is found.
    '''
    new_list = []
    for i in range(len(text)):
        if text[i:i+len(pattern)] == pattern:
            if list == []:
                new_list.append(i)
            else:
                return i
    
    if new_list != []: # We found all the starting indexes
        print('returning new_list:', new_list)
        return new_list

    if list == []: # We didn't find any starting indexes so we need to return an empty list with this check.
        return []  
    
    return None # This will be called for find_index func.

def contains(text, pattern):
    # in Recursiive solution add arguments:  text_index = 0, pattern_index = 0
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    
    # ***Recursive Solution 🎢***
    # if text[text_index] == pattern[pattern_index]:
    #     if pattern_index == len(pattern)-1:  # Base Case - Found the the end of the pattern 🎉
    #         return True
    #     print('found a match - ', 'text[text_index]:', text[text_index], 'pattern[pattern_index]', pattern[pattern_index])
    #     contains(text, pattern, text_index + 1, pattern_index + 1)
    # else:
    #     if pattern_index == len(pattern)-1:  # Didn't find the end of the pattern 😫
    #         print('we didnt find the pattern 😫')
    #         return False
    #     contains(text, pattern, text_index + 1, pattern_index)
    # return True

    # Refactor by Dylanator    
    if len(pattern) == 0:
        return True
    
    for i in range(len(text)):
        if text[i:i+len(pattern)] == pattern:
            return True
    
    return False


    # # ***Iterative Solution 🚶‍*** 
    # if len(pattern) == 0:
    #     return True
    
    # contains_pattern = False
    # pattern_index = 0   # Keep track of the index in pattern to compare
    
    # for char in text:
    #     if char == pattern[pattern_index]:       # Match Found 
    #         if pattern_index == len(pattern)-1:  # Found the the final match 🎉
    #             contains_pattern = True
    #             break
    #         pattern_index += 1   # Look at the next index of the pattern
    #         contains_pattern = True      # The pattern is existant thus far.
    #     else:   # Didn't Find a Match
    #         pattern_index = 0   # Reset pattern index
    #         if char == pattern[pattern_index]:  # Check if curr char is equal to the resetted pattern char 
    #             if pattern_index == len(pattern)-1:  # Found the the end of the pattern 🎉
    #                 contains_pattern = True
    #                 break
    #             pattern_index += 1
    #             contains_pattern = True   # Does this line conflict with the next line?
    #         contains_pattern = False      # Pattern hasn't been found yet
    
    # return contains_pattern


    # One Easy Way 😛
    # if pattern not in text: 
    #     return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # ***Iterative Solution 🚶‍***    
    if len(pattern) == 0:
        return 0
    
    return find_pattern_index(text, pattern)

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    starting_idxs = []

    if len(pattern) == 0:
        return [idx for idx, ltr in enumerate(text)] 

    return find_pattern_index(text, pattern, starting_idxs)

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))
    pass

def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    # main()
    print(find_all_indexes('abc', ''))
