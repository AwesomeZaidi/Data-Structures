# Unscrambled these words to find a word...?
# given a string - unscramble it to find a word in the dictionary.

# Python3 code to convert tuple  
# into string 
import functools 
import operator  
from itertools import permutations
from collections import defaultdict

dictionary =  ['hi', 'hello', 'cool']
final_words = []

def convertTuple(tup): 
    str = functools.reduce(operator.add, (tup)) 
    return str

def check_for_word_in_dict(word):
    if defaultdict[word] != None:
        final_words.append(word)


def unscramble_word(word):
    # Find every permutation of this word and check if its in the dictionary
    for word in permutations(word):
        str_word = convertTuple(word)
        check_for_word_in_dict(word)
    
    return final_words

print(unscramble_word('hlloe'))