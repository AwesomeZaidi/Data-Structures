class BinaryTreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_branch(self):
        return self.left is not None or self.right is not None

    def height(self):
        left_height = self.left.height() if self.left is not None else -1
        right_height = self.right.height() if self.right is not None else -1
        return 1 + max(left_height, right_height)

class BinarySearchTree():
    def __init__(self, items=None):
        self.root = None
        self.size = 0         
        if items is not None:
            for item in items:
                self.insert(item)
    
    def is_empty(self):
        return self.root is None

    def height(self):
        return 0 if self.is_empty() else self.root.height()

    def contains(self, item):
        node = self._find_node(item, self.root)
        # Return True if a node was found, or False
        return node is not None
    
    def search(self, item):
        node = self._find_node(item, self.root)
        return node.data if node.data is not None else None

    def insert(self, item):
        if self.is_empty():
            self.root = BinaryTreeNode(item)
            self.size += 1
            return self.size

        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node(item, self.root)

        if item < parent.data:
            parent.left = BinaryTreeNode(item)
        if item < parent.data:
            parent.right = BinaryTreeNode(item)

    def _find_node(self, item, node):
        if node is None: # Not found (base case)
            return None
        elif node.data == item: # Check if the given item matches the node's data
            return node # Return the found node
        elif node.data < item : # Check if the given item is less than the node's data
            return  self._find_node(item, node.right) # Recursively descend to the node's left child, if it exists
        elif node.data > item: # Check if the given item is greater than the node's data
            return self._find_node(item, node.left) # Recursively descend to the node's right child, if it exists

    def _find_parent_node(self, item, node, parent=None):
        if node is None:
            return parent
        if item == node.data:
            return parent
        if item < node.data:
            return self._find_parent_node(item, node.left, node)
        if item > node.data:
            return self._find_parent_node(item, node.right, node)
    
    def items_in_order(self):
        items = []
        if not self.is_empty():
            self._traverse_in_order(self.root, items.append)
        return items

    def _traverse_pre_order(self, node, visit):
        if node is not None:
            visit(node)
            self._traverse_in_order(node.left, visit)
            self._traverse_in_order(node.right, visit)

    def _traverse_in_order(self, node, visit):
        if node is not None:
            self._traverse_in_order(node.left, visit)
            visit(node.data)
            self._traverse_in_order(node.right, visit)

    def _traverse_post_order(self, node, visit):
        if node is not None:
            self._traverse_post_order(node.left, visit)
            self._traverse_post_order(node.right, visit)
            visit(node.data)