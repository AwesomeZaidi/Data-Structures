
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, list):
        self.head = None
        self.tail = None
        self.size = 0
        if list is not None:
            for item in list:
                self.append(item)

    def insert_at_index(self, index, item):
        if index == 0:
            self.prepend(item)
        if index == self.size:
            self.append(item)
        prev_node = self.head

        # go through till we get to that index
        for _ in range(index-1):
            prev_node = prev_node.next
        
        new_node = Node(item)
        new_node.next = prev_node
        prev_node.next = new_node
        self.size += 1

    def append(self, item):
        node = Node(item)

        if node is None:
            self.head = item
        else:
            self.tail.next = node
        
        self.tail = node
        self.size += 1

    def prepend(self, item):
        node = Node(item)

        if node is None:
            self.tail = item
        else:
            node.next = self.head
        
        self.head = node
        
        self.size += 1

  