#!python

from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        test_set = Set([1, 2, 3])
        assert test_set.map.length() == 3
        assert test_set.contains(1) == True
        assert test_set.contains(4) == False        
    
    def test_contains(self):
        test_set = Set(['a','b','c','d','e'])
        assert test_set.contains('a') == True
        assert test_set.contains('b') == True
        assert test_set.contains('c') == True
        assert test_set.contains('f') == False
        assert test_set.contains('g') == False
        assert test_set.contains('h') == False
    
    def test_add(self):
        test_set = Set([])
        test_set.add('a')
        test_set.add('b')
        test_set.add('c')
        assert test_set.contains('a') == True
        assert test_set.contains('b') == True
        assert test_set.contains('c') == True
        assert test_set.contains('d') == False
        assert test_set.contains('e') == False
        assert test_set.contains('f') == False

    def test_remove(self):
        test_set = Set([])
        test_set.add('a')
        test_set.add('b')
        test_set.add('c')
        assert test_set.contains('a') == True
        assert test_set.contains('b') == True
        assert test_set.contains('c') == True
        test_set.remove('a')
        test_set.remove('b')
        test_set.remove('c')
        assert test_set.contains('a') == False
        assert test_set.contains('b') == False
        assert test_set.contains('c') == False

    def test_union(self):
        test_set = Set([1,2,3,4,5])
        other_set = Set([1,2,3,7])
        unions = test_set.union(other_set)
        union_items = unions.map.keys()
        assert union_items == [1,2,3,4,5,7]

    def test_intersection(self):
        test_set = Set([1,2,3,4,5])
        other_set = Set([1,2,3,7])
        unions = test_set.intersection(other_set)
        union_items = unions.map.keys()
        assert union_items == [1,2,3]

    def test_difference(self):
        test_set = Set([1,2,3,4,5])
        other_set = Set([1,2,3,7])
        unions = test_set.difference(other_set)
        union_items = unions.map.keys()
        assert union_items == [1,2,3]

if __name__ == '__main__':
    unittest.main()
