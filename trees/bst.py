from nodes import BinaryNode
from .binary_tree import BinaryTree


class BST(BinaryTree):
    """
    Binary Search Tree implementation.
    """

    def __init__(self):
        super().__init__()

    # =====================================================
    # INSERT
    # =====================================================

    def insert(self, value):

        new_node = BinaryNode(value)

        if self.root is None:
            self.root = new_node
            self._size = 1
            return new_node

        current = self.root
        parent = None

        while current is not None:

            parent = current

            if value < current.value:
                current = current.left

            elif value > current.value:
                current = current.right

            else:
                # duplicate
                return current

        new_node.parent = parent

        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        self._size += 1

        return new_node

    # =====================================================
    # FIND
    # =====================================================

    def find(self, value):

        current = self.root

        while current is not None:

            if value == current.value:
                return current

            if value < current.value:
                current = current.left

            else:
                current = current.right

        return None

    # =====================================================
    # MINIMUM
    # =====================================================

    def minimum(self, node=None):

        if node is None:
            node = self.root

        if node is None:
            return None

        while node.left is not None:
            node = node.left

        return node

    # =====================================================
    # MAXIMUM
    # =====================================================

    def maximum(self, node=None):

        if node is None:
            node = self.root

        if node is None:
            return None

        while node.right is not None:
            node = node.right

        return node

    # =====================================================
    # SUCCESSOR
    # =====================================================

    def successor(self, node):

        if node is None:
            return None

        if node.right is not None:
            return self.minimum(node.right)

        parent = node.parent

        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent

        return parent

    # =====================================================
    # PREDECESSOR
    # =====================================================

    def predecessor(self, node):

        if node is None:
            return None

        if node.left is not None:
            return self.maximum(node.left)

        parent = node.parent

        while parent is not None and node == parent.left:
            node = parent
            parent = parent.parent

        return parent

    # =====================================================
    # DELETE
    # =====================================================

    def _transplant(self, u, v):

        if u.parent is None:
            self.root = v

        elif u == u.parent.left:
            u.parent.left = v

        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def delete(self, value):

        node = self.find(value)

        if node is None:
            return False

        # Case 1
        if node.left is None:
            self._transplant(node, node.right)

        # Case 2
        elif node.right is None:
            self._transplant(node, node.left)

        # Case 3
        else:

            successor = self.minimum(node.right)

            if successor.parent != node:

                self._transplant(successor, successor.right)

                successor.right = node.right
                successor.right.parent = successor

            self._transplant(node, successor)

            successor.left = node.left
            successor.left.parent = successor

        self._size -= 1

        return True

    # =====================================================
    # EXTRA
    # =====================================================

    def min(self):
        return self.minimum()

    def max(self):
        return self.maximum()

    def __repr__(self):
        return f"BST(size={self._size})"