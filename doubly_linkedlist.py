#!python
from linkedlist import LinkedList

class Node(object):
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class DoublyLinkedList(LinkedList):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def append(self, item):
        new_node = Node(item)
        # Check if this doubly linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            # insert new node after tail
            new_node.prev = self.tail
            self.tail.next = new_node
        
        self.tail = new_node


        # add to size
        self.size += 1

    