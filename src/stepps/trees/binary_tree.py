from collections import deque

from stepps.nodes import BinaryNode


class BinaryTree[T]:
    """
    Base class for binary tree implementations.

    :ivar root: The root node of the tree, or ``None`` if the tree is empty.
    :ivar _size: The number of nodes currently contained in the tree.
    """

    def __init__(self) -> None:
        """
        Initialize an empty binary tree.
        """
        self.root: BinaryNode[T] | None = None
        self._size: int = 0

    # =====================================================
    # Basic Properties
    # =====================================================

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

    # =====================================================
    # Searching
    # =====================================================

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

    # =====================================================
    # Tree Statistics
    # =====================================================

    def height(self) -> int:
        """
        Return the height of the tree.

        An empty tree has a height of ``-1`` and a tree containing
        a single node has a height of ``0``.

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

        An internal node is a node that has at least one child.

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
        :return: The node containing the inserted value.
        :raises NotImplementedError: If the tree implementation does not
            provide insertion behavior.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement insert()."
        )

    def delete(self, value: T) -> bool:
        """
        Delete a value from the tree.

        :param value: The value to delete.
        :return: ``True`` if the value was deleted.
        :raises NotImplementedError: If the tree implementation does not
            provide deletion behavior.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement delete()."
        )

    # =====================================================
    # String Representation
    # =====================================================

    def __repr__(self) -> str:
        """
        Return the string representation of the tree.

        :return: A string containing the tree type and node count.
        """
        return f"{self.__class__.__name__}(size={self._size})"
