#!python
from stack import LinkedStack
from queue import LinkedQueue

class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # Check if both left child and right child have no value
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # Check if either left child or right child has a value
        return self.right is not None or self.left is not None

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Best and worst case running time: ??? under what conditions?"""

        # Depth Search to go all the way to the bottom.
        left_height = self.left.height() if self.left is not None else -1
        right_height = self.right.height() if self.right is not None else -1

        return 1 + max(left_height, right_height)


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        Best and worst case running time: ??? under what conditions?"""
        # check root node val  & calc height.
        return 0 if self.is_empty() else self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        Best case running time: ??? under what conditions?
        Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        Best case running time: ??? under what conditions?
        Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return the node's data if found, or None
        return node.data if node.data is not None else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        Best case running time: ??? under what conditions?
        Worst case running time: ??? under what conditions?"""
        # Handle the case where the tree is empty
        if self.is_empty():
            self.root = BinaryTreeNode(item) # Create a new root node
            self.size += 1 # Increase the tree size
            return self.size
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)
        
        # Check if the given item should be inserted left of parent node
        if item < parent.data:
            # Create a new node and set the parent's left child
            parent.left = BinaryTreeNode(item)
        # Check if the given item should be inserted right of parent node
        elif item > parent.data:
            # Create a new node and set the parent's right child
            parent.right = BinaryTreeNode(item)        
        # Increase the tree size
        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        Best case running time: ??? under what conditions?
        Worst case running time: ??? under what conditions?"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            if item == node.data: # Check if the given item matches the node's data
                return node # Return the found node 
            elif item < node.data:  # Check if the given item is less than the node's data
                node = node.left # Descend to the node's left child
            elif item > node.data: # Check if the given item is greater than the node's data
                node = node.left    # Descend to the node's right child
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        Best case running time: ??? under what conditions?
        Worst case running time: ??? under what conditions?"""
        # Check if starting node exists
        if node is None: # Not found (base case)
            return None
        elif item == node.data: # Check if the given item matches the node's data
            return node # Return the found node
        elif item < node.data: # Check if the given item is less than the node's data
            return  self._find_node_recursive(item, node.left) # Recursively descend to the node's left child, if it exists
        elif item > node.data: # Check if the given item is greater than the node's data
            return self._find_node_recursive(item, node.right) # Recursively descend to the node's right child, if it exists

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        Best case running time: ??? under what conditions?
        Worst case running time: ??? under what conditions?"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            if item == node.data: # Check if the given item matches the node's data
                return parent # Return the parent of the found node
            elif item < node.data:   # Check if the given item is less than the node's data
                parent = node    # Update the parent and descend to the node's left child
                node = node.left
            elif item > node.data:  # Check if the given item is greater than the node's data
                parent = node    # Update the parent and descend to the node's right child
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        if node is None: # Check if starting node exists
            return None # Not found (base case)
        if item == node.data: # Check if the given item matches the node's data
            return parent # Return the parent of the found node
        elif item < node.data:   # Check if the given item is less than the node's data
            # Recursively descend to the node's left child, if it exists
            return self._find_parent_node_recursive(item, node.left, node)
        elif item > node.data:  # Check if the given item is greater than the node's data
            return self._find_parent_node_recursive(item, node.right, node) # Recursively descend to the node's right child, if it exists

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        Best case running time: ??? under what conditions?
        Worst case running time: ??? under what conditions?"""
        # Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases
        node = self.root
        if node.data == item:
            if node.left != None and node.right != None: # if left and right are not none
                self.root = node.left # set left node to root
                node.right.parent = self.root # set right parent to left node

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            # self._traverse_in_order_recursive(self.root, items.append)
            # items.append is a  pointer to afunc you can later call
            # it hasn't been called yet.
            self._traverse_in_order_recursive(self.root, items.append)

        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """
            Traverse this binary tree with recursive in-order traversal (DFS).
            Start at the given node and visit each node with the given function.
            Running time: O(n) -> 6n
        """
        # a node has a depth a tree has a height.
        # max size of stack is the height of the tree.
        # so how much memory is being used from that?
        # The mem cost is O(log(n)) if its balanced
        # unbalanced - it will approach n
        # 2 func calls are being made for each node.
        if node is not None:
            if node.left is not None:
                self._traverse_in_order_recursive(node.left, visit) # Going down BT Left
            visit(node.data)
            if node.right is not None:
                self._traverse_in_order_recursive(node.right, visit) #Going down BT Right

    # def _traverse_in_order_iterative(self, node, visit):
        #     """
        #         Traverse this binary tree with iterative in-order traversal (DFS).
        #         Start at the given node and visit each node with the given function.
        #         Running time: O(n) -> 6n
        #     """
        #     # Traverse in-order without using recursion (stretch challenge)
        #     # the diff between recusv is you declare your own stack vs func calls making it
        #     stack = [] # could use a linked list as well
        #     done = False # tells when we're doing traversing
        #     current = node 

        #     # anytime u pushed something on the stack that means u will have to come back there soon so save it for later, then advance to its left node, then if you pop somethiing frmo the stack you visit it right away and then decend to the right side.
        #     # so popping the stack is like, let me go back, similar how we go back to a recusrive funciton call
        #     while(not done):
        #         # Reach the left most Node of the current Node 
        #         if current is not None: 
        #             # Place pointer to a tree node on the stack  
        #             # before traversing the node's left subtree 
        #             # push the cure t onto the stack
        #             stack.append(current.data)

        #             current = current.left 

        #         # BackTrack from the empty subtree and visit the Node 
        #         # at the top of the stack; however, if the stack is  
        #         # empty you are done
        #         # current is NULL and stack is not empty
        #         else:
        #             if(len(stack) > 0):
        #                 current = stack.pop()
        #                 # set current = popped_item->right 
        #                 visit(current.data)
        #                 current = current.right
        #             else:
        #                 done = True

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node is not None:
            visit(node)
            self._traverse_in_order_recursive(node.left, visit) # Traverse left subtree
            self._traverse_in_order_recursive(node.right, visit) # Traverse right subtree

    # def _traverse_pre_order_iterative(self, node, visit):
        #     """Traverse this binary tree with iterative pre-order traversal (DFS).
        #     Start at the given node and visit each node with the given function.
        #     TODO: Running time: ??? Why and under what conditions?
        #     TODO: Memory usage: ??? Why and under what conditions?"""
        #     # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node is not None:
            self._traverse_in_order_recursive(node.left, visit)
            self._traverse_in_order_recursive(node.right, visit)
            visit(node)

    # def _traverse_post_order_iterative(self, node, visit):
        #     """Traverse this binary tree with iterative post-order traversal (DFS).
        #     Start at the given node and visit each node with the given function.
        #     TODO: Running time: ??? Why and under what conditions?
        #     TODO: Memory usage: ??? Why and under what conditions?"""
        #     # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Coded with Nathan in our room 💪🏼
        Start at the given node and visit each node with the given function."""
        # Create queue to store nodes not yet traversed in level-order
        queue = LinkedQueue()
        # Enqueue given starting node
        queue.enqueue(start_node)
        # Loop until queue is empty
        while not queue.is_empty():
            # Dequeue node at front of queue
            node = queue.dequeue()
            # Visit this node's data with given function
            visit(node.data)
            # Enqueue this node's left child, if it exists
            if node.left is not None:
                queue.enqueue(node.left)
            # Enqueue this node's right child, if it exists
            if node.right is not None:
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()