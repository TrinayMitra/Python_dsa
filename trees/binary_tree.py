from collections import deque
from typing import Generic, TypeVar

from nodes import BinaryNode
from iterators import (
    InOrderIterator,
    PreOrderIterator,
    PostOrderIterator,
    LevelOrderIterator,
)

T = TypeVar("T")


class BinaryTree(Generic[T]):
    """
    Base class for all binary tree implementations.
    """

    def __init__(self) -> None:
        self.root: BinaryNode[T] | None = None
        self._size: int = 0

    # =====================================================
    # Basic Properties
    # =====================================================

    def is_empty(self) -> bool:
        """
        Returns True if the tree has no nodes.
        """
        return self.root is None

    def clear(self) -> None:
        """
        Removes all nodes from the tree.
        """
        self.root = None
        self._size = 0

    def size(self) -> int:
        """
        Returns the number of nodes in the tree.
        """
        return self._size

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return not self.is_empty()

    # =====================================================
    # Traversals
    # =====================================================

    def preorder(self) -> PreOrderIterator[T]:
        """
        Returns a preorder iterator.
        """
        return PreOrderIterator(self.root)

    def inorder(self) -> InOrderIterator[T]:
        """
        Returns an inorder iterator.
        """
        return InOrderIterator(self.root)

    def postorder(self) -> PostOrderIterator[T]:
        """
        Returns a postorder iterator.
        """
        return PostOrderIterator(self.root)

    def levelorder(self) -> LevelOrderIterator[T]:
        """
        Returns a level-order iterator.
        """
        return LevelOrderIterator(self.root)

    def __iter__(self) -> InOrderIterator[T]:
        """
        Default iterator (inorder).
        """
        return self.inorder()

    # =====================================================
    # Searching
    # =====================================================

    def find(self, value: T) -> BinaryNode[T] | None:
        """
        Finds and returns the first node containing value.

        Returns:
            BinaryNode if found, otherwise None.
        """
        for node in self.levelorder():
            if node.value == value:
                return node

        return None

    def contains(self, value: T) -> bool:
        """
        Returns True if value exists in the tree.
        """
        return self.find(value) is not None

    def __contains__(self, value: T) -> bool:
        return self.contains(value)

    # =====================================================
    # Tree Statistics
    # =====================================================

    def height(self) -> int:
        """
        Returns the height of the tree.

        Empty tree -> -1
        Single node -> 0
        """
        if self.root is None:
            return -1

        queue: deque[tuple[BinaryNode[T], int]] = deque([(self.root, 0)])
        max_height = 0

        while queue:
            node, level = queue.popleft()
            max_height = max(max_height, level)

            if node.left is not None:
                queue.append((node.left, level + 1))

            if node.right is not None:
                queue.append((node.right, level + 1))

        return max_height

    def count_leaves(self) -> int:
        """
        Returns the number of leaf nodes.
        """
        count = 0

        for node in self.levelorder():
            if node.is_leaf():
                count += 1

        return count

    def count_internal_nodes(self) -> int:
        """
        Returns the number of internal (non-leaf) nodes.
        """
        count = 0

        for node in self.levelorder():
            if not node.is_leaf():
                count += 1

        return count

    def insert(self, value: T) -> BinaryNode[T]:
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement insert()."
        )

    def delete(self, value: T) -> bool:
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement delete()."
        )

    # =====================================================
    # String Representation
    # =====================================================

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(size={self._size})"
