from collections import deque

from iterators import (
    InOrderIterator,
    PreOrderIterator,
    PostOrderIterator,
    LevelOrderIterator,
)


class BinaryTree:
    """
    Base class for all binary tree implementations.
    """

    def __init__(self):
        self.root = None
        self._size = 0

    # =====================================================
    # Basic Properties
    # =====================================================

    def is_empty(self):
        """
        Returns True if the tree has no nodes.
        """
        return self.root is None

    def clear(self):
        """
        Removes all nodes from the tree.
        """
        self.root = None
        self._size = 0

    def size(self):
        """
        Returns the number of nodes in the tree.
        """
        return self._size

    def __len__(self):
        return self._size

    def __bool__(self):
        return not self.is_empty()

    # =====================================================
    # Traversals
    # =====================================================

    def preorder(self):
        """
        Returns a preorder iterator.
        """
        return PreOrderIterator(self.root)

    def inorder(self):
        """
        Returns an inorder iterator.
        """
        return InOrderIterator(self.root)

    def postorder(self):
        """
        Returns a postorder iterator.
        """
        return PostOrderIterator(self.root)

    def levelorder(self):
        """
        Returns a level-order iterator.
        """
        return LevelOrderIterator(self.root)

    def __iter__(self):
        """
        Default iterator (inorder).
        """
        return self.inorder()

    # =====================================================
    # Searching
    # =====================================================

    def find(self, value):
        """
        Finds and returns the first node containing value.

        Returns:
            BinaryNode if found, otherwise None.
        """

        for node in self.levelorder():
            if node.value == value:
                return node

        return None

    def contains(self, value):
        """
        Returns True if value exists in the tree.
        """
        return self.find(value) is not None

    def __contains__(self, value):
        return self.contains(value)

    # =====================================================
    # Tree Statistics
    # =====================================================

    def height(self):
        """
        Returns the height of the tree.

        Empty tree -> -1
        Single node -> 0
        """

        if self.root is None:
            return -1

        queue = deque([(self.root, 0)])
        max_height = 0

        while queue:

            node, level = queue.popleft()
            max_height = max(max_height, level)

            if node.left is not None:
                queue.append((node.left, level + 1))

            if node.right is not None:
                queue.append((node.right, level + 1))

        return max_height

    def count_leaves(self):
        """
        Returns the number of leaf nodes.
        """

        count = 0

        for node in self.levelorder():
            if node.is_leaf():
                count += 1

        return count

    def count_internal_nodes(self):
        """
        Returns the number of internal (non-leaf) nodes.
        """

        count = 0

        for node in self.levelorder():
            if not node.is_leaf():
                count += 1

        return count

    def insert(self, value):
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement insert()."
        )


    def delete(self, value):
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement delete()."
        )

    # =====================================================
    # String Representation
    # =====================================================

    def __repr__(self):
        return f"{self.__class__.__name__}(size={self._size})"