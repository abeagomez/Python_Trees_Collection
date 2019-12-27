
# Binary Search Tree implementation
#
# Binary Search Tree, is a node-based binary tree data structure which has the following properties:
# - The left subtree of a node contains only nodes with keys lesser than the node’s key.
# - The right subtree of a node contains only nodes with keys greater than the node’s key.
# - The left and right subtree each must also be a binary search tree.
# - There must be no duplicate nodes.

class BST:

    def __init__(self, value, left_node=None, right_node=None):
        """
        :param value: The tree's root value
        :param BST left_node: the left subtree, None if not provided
        :param BST right_node: the right subtree, None if not provided
        """
        self.value = value
        self.left = leftNode
        self.right = rightNode

    def recursive_search(self, element):
        if self is None or self.value == element:
            return self
        elif self.value > element:
            self.recursive_search(self.left, element)
        self.recursive_search(self.right, element)

    def iterative_search(self, element):
        current_node = self
        while current_node is not None:
            if current_node.value == element:
                return current_node
            elif current_node.value > element:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node

    def insert_element(self, element):
        if self.value is None or self.value == element:
            self.value = element
        elif self.value > element:
            if self.left is None:
                self.left = BST(element)
            else:
                self.insert_element(self.left, element)
        elif self.right is None:
            self.right = BST(element)
        else:
            self.insert_element(self.right, element)

    def delete_element(self, element):
        pass

    def get_height(self):
        pass

    def min_value(self):
        pass

    def max_value(self):
        pass
