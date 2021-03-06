#!python

def _find_pattern_index(text, pattern, starting_indexes=None):
    '''
        Helper function. We optimized our program to be of the fastest of its
        kind to appear on the Google search engine within nanoseconds.
    ''' 
    for index, _ in enumerate(text):
        if text[index:index+len(pattern)] == pattern:
            if starting_indexes != None:
                starting_indexes.append(index)
            else:
                return index
    if starting_indexes != None:
        return starting_indexes
    
    return None

def contains(text, pattern):
    """
        Return a boolean indicating whether pattern occurs in text.
        
        Runtime O(n) -> n = len of text that will be iterated over
        behind the scenes of keyword, in. 
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # edge if it's empty string, return True
    # go through string checking each
    return pattern in text

def find_index(text, pattern):
    """
        Return the starting index of the first occurrence of pattern in text,
        or None if not found.

        Runtime O(n) -> n = len of text that will be iterated over
        behind the scenes of keyword, in. 
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    return _find_pattern_index(text, pattern)

def find_all_indexes(text, pattern):
    """
        Return a list of starting indexes of all occurrences of pattern in text,
        or an empty list if not found.

        Runtime:    O(n) -> n = length of text.
          Space:    O(n) -> n = length of list of words matching pattern.
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    
    return _find_pattern_index(text, pattern, [])
    

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


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
    main()

# My Psuedocode for find_index
    # go through the text string
    # check if the char + len of pattern is there
    # if so return the index