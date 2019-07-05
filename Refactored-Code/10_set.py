
hashtable = __import__('8_hashtables', fromlist=['HashTable'])
HashTable = hashtable.HashTable


class Set(object):

    def __init__(self, elements=None):
        """Initialize this new empty set structure with the given initial size."""
        self.map = HashTable()
        self.size = 0 # property that tracks the number of elements in constant time
        if elements is not None:
            for element in elements:
                self.size += 1 
                self.map.set(element, True)
    
    def contains(self, element):
        """return a boolean indicating whether element is in this set."""
        # return element in self.elements -> return self.elements.___contains__(element)
        return self.map.contains(element)

    def add(self, element):
        """add element to this set, if not present already"""
        # check if its unique by 
        # if not self.contains(element):
        if self.map.contains(element) == False:
            self.map.set(element, None)
        self.size += 1
        return self.size

    def remove(self, element):
        """remove element from this set, if present, or else raise KeyError"""
        # if element in self.elements:
        # if self.elements.___contains__(element):
        # if self.contains(element):
        self.map.delete(element)
        self.size -= 1
        return self.size
        # else:
        #     raise KeyError('Element not found: {}'.format(element))
    
    def union(self, other_set):
        """return a new set that is the union of this set and other_set"""
        new_set = Set()
        # for element in self.map:
        # for element in self.elements.__iter__():
        for element in self.map.keys():
            new_set.add(element) # or new_set.add(element.data[0]) ?

        for element in other_set.map.keys():
            if not new_set.contains(element):
                new_set.add(element)

        return new_set
    
    def intersection(self, other_set):
        """return a new set that is the intersection of this set and other_set"""
        new_set = Set()
        for element in other_set.map.keys():
            if self.contains(element):
                new_set.add(element)

        return new_set

    def difference(self, other_set):
        """return a new set that is the difference of this set and other_set"""
        new_set = Set()
        for element in self.map.keys():
            if other_set.contains(element):
                new_set.add(element)

        return new_set
        
    def issubset(self, other_set):
        """Return true if all the elements in a set exist in the other set, False if not."""
        for item in self.map.keys():
            if item not in other_set.map.keys():
                return False
        return True