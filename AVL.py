# AVL Tree
#
# An AVL tree is a self-balancing binary search tree. In an AVL tree, the heights of the two child subtrees
# of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore
# this property. Lookup, insertion, and deletion all take O(log n) time in both the average and worst cases, where
# n is the number of nodes in the tree prior to the operation. Insertions and deletions may require the tree to
# be rebalanced by one or more tree rotations.

class AVL:
    def __init__(self, value):
        """
        :param value: The tree's root value
        """
        self.value = value
        self.left = None
        self.right = None

    def get_height(self):
        pass

    def insert(self, value):
        # Let the newly inserted node be w
        # 1) Perform standard BST insert for w.
        # 2) Starting from w, travel up and find the first unbalanced node. Let z be the first
        # unbalanced node, y be the child of z that comes on the path from w to z and x be the
        # grandchild of z that comes on the path from w to z.
        # 3) Re-balance the tree by performing appropriate rotations on the subtree rooted with z.
        # There can be 4 possible cases that needs to be handled as x, y and z can be arranged
        # in 4 ways. Following are the possible 4 arrangements:
        #    a) y is left child of z and x is left child of y (Left Left Case)
        #    b) y is left child of z and x is right child of y (Left Right Case)
        #    c) y is right child of z and x is right child of y (Right Right Case)
        #    d) y is right child of z and x is left child of y (Right Left Case)
        pass

    def delete(self, value):
        pass

    def get_balance(self):
        pass

    def rotate_right(self):
        pass

    def rotate_left(self):
        pass

    def search_recursive(self):
        pass

    def search_iterative(self):
        pass

    def preorder(self):
        pass

