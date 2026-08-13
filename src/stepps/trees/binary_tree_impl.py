from collections import deque

from stepps.nodes import BinaryNode
from stepps.trees.binary_tree import BinaryTree


class BinaryTreeImpl[T](BinaryTree[T]):
    """
    Provide the default implementation of a binary tree.
    """

    def __init__(self) -> None:
        """
        Initialize an empty binary tree.
        """
        self.root: BinaryNode[T] | None = None
        self._size = 0

    def is_empty(self) -> bool:
        """
        Return whether the tree is empty.

        :return: ``True`` if the tree contains no nodes, otherwise ``False``.
        """
        return self.root is None

    def clear(self) -> None:
        """
        Remove all nodes from the tree.
        """
        self.root = None
        self._size = 0

    def size(self) -> int:
        """
        Return the number of nodes in the tree.

        :return: The number of nodes in the tree.
        """
        return self._size

    def find(self, value: T) -> BinaryNode[T] | None:
        """
        Find the first node containing ``value``.

        :param value: The value to search for.
        :return: The matching node, or ``None`` if the value is not found.
        """
        if self.root is None:
            return None

        queue: deque[BinaryNode[T]] = deque([self.root])

        while queue:
            node = queue.popleft()

            if node.value == value:
                return node

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return None

    def contains(self, value: T) -> bool:
        """
        Return whether ``value`` exists in the tree.

        :param value: The value to search for.
        :return: ``True`` if the value exists, otherwise ``False``.
        """
        return self.find(value) is not None

    def __contains__(self, value: T) -> bool:
        """
        Return whether ``value`` exists in the tree.

        :param value: The value to search for.
        :return: ``True`` if the value exists, otherwise ``False``.
        """
        return self.contains(value)

    def height(self) -> int:
        """
        Return the height of the tree.

        :return: The height of the tree.
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
        Return the number of leaf nodes in the tree.

        :return: The number of leaf nodes.
        """
        if self.root is None:
            return 0

        count = 0
        queue: deque[BinaryNode[T]] = deque([self.root])

        while queue:
            node = queue.popleft()

            if node.is_leaf():
                count += 1
                continue

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return count

    def count_internal_nodes(self) -> int:
        """
        Return the number of internal nodes in the tree.

        :return: The number of internal nodes.
        """
        if self.root is None:
            return 0

        count = 0
        queue: deque[BinaryNode[T]] = deque([self.root])

        while queue:
            node = queue.popleft()

            if node.has_children():
                count += 1

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return count

    def insert(self, value: T) -> BinaryNode[T]:
        """
        Insert a value into the tree.

        :param value: The value to insert.
        :raises NotImplementedError: Binary tree insertion is defined by
            concrete tree implementations.
        """
        raise NotImplementedError

    def delete(self, value: T) -> bool:
        """
        Delete a value from the tree.

        :param value: The value to delete.
        :raises NotImplementedError: Binary tree deletion is defined by
            concrete tree implementations.
        """
        raise NotImplementedError

    def __len__(self) -> int:
        """
        Return the number of nodes in the tree.

        :return: The number of nodes in the tree.
        """
        return self._size

    def __bool__(self) -> bool:
        """
        Return whether the tree contains at least one node.

        :return: ``True`` if the tree is not empty, otherwise ``False``.
        """
        return not self.is_empty()

    def __repr__(self) -> str:
        """
        Return the string representation of the tree.

        :return: A string containing the tree type and node count.
        """
        return f"{self.__class__.__name__}(size={self._size})"