
# Binary Search Tree implementation
#
# Binary Search Tree, is a node-based binary tree data structure which has the following properties:
# - The left subtree of a node contains only nodes with keys lesser than the node’s key.
# - The right subtree of a node contains only nodes with keys greater than the node’s key.
# - The left and right subtree each must also be a binary search tree.
# - There must be no duplicate nodes.

class BST:

    def __init__(self, value):
        """
        :param value: The tree's root value
        """
        self.value = value
        self.left = None
        self.right = None

    def get_right_subtree(self):
        return self.right

    def get_left_subtree(self):
        return self.left

    def recursive_search(self, element):
        if self is None or self.value == element:
            return self
        elif self.value > element:
            self.left.recursive_search(element)
        self.right.recursive_search(element)

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
        if self.value is None:
            self.value = element
        elif self.value > element:
            if self.left is None:
                self.left = BST(element)
            else:
                self.left.insert_element(element)
        elif self.right is None:
            self.right = BST(element)
        else:
            self.right.insert_element(element)

    def inorder_traversal(self):
        if self.left is not None:
            self.left.inorder_traversal()
        print(self.value)
        if self.right is not None:
            self.right.inorder_traversal()

    def delete_element(self, element):
        # When we delete a node, three possibilities arise.
        # 1. Node to be deleted is leaf: Simply remove from the tree.
        # 2. Node to be deleted has only one child: Replace the node with it's child
        # 3. Node to be deleted has two children: Find inorder successor of the node.
        # Copy contents of the inorder successor to the node and delete the inorder successor.
        # Note that inorder predecessor can also be used.
        pass

    def get_height(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.get_height() + 1
        elif self.right is None:
            return self.left.get_height() + 1
        return max(self.left.get_height() + 1, self.right.get_height() + 1)

    def min_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def max_value(self):
        current_node = self
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.value


#TESTING SECTION
tree = BST(5)
tree.insert_element(4)
tree.insert_element(6)
tree.insert_element(32)
tree.insert_element(1)

#tree.inorder_traversal()
#print(tree.min_value())
#print(tree.max_value())
print(tree.get_height())