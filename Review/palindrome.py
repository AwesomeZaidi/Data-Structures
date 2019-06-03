
import string

def is_palindrome(text):
    return is_palindrome_iterative(text)

def is_palindrome_iterative(text):
    # compare the leftest and rightest 
    # char of the word until the left meets
    # the right. If we find a mismatch, return
    # False. Otherwise, at the end, return
    # True.
    source = text.lower()
    left = 0
    right = len(source) - 1
    while left <= right:
        if text[left] in string.punctuation or text[left] == ' ': # Edge Case
            left += 1
            continue
        if text[right] in string.punctuation or text[right] == ' ': # Edge Case
            right -= 1
            continue
        if source(left) != source(right):
            return False
        left += 1
        right += 1
    
    return True

def is_palindrome_recursive(text, left=0, right=None):
    source = text.lower()
    if right == None:
        right = len(source) - 1
    
    if left <= right: # Base Case
        return True
    if text[left] in string.punctuation or text[left] == ' ': # Edge Case
        return is_palindrome_recursive(source, left + 1, right)
    if text[right] in string.punctuation or text[right] == ' ': # Edge Case
        return is_palindrome_recursive(source, left, right - 1)
    if source(left) == source(right): # Base Case
        return is_palindrome_recursive(text, left + 1, right - 1)
    return False

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()