from typing import Protocol

from stepps.nodes import BinaryNode
from stepps.trees.binary_tree import BinaryTree


class Comparable(Protocol):
    """
    Define the comparison operations required by a binary search tree.
    """

    def __lt__(self, other: object, /) -> bool: ...

    def __gt__(self, other: object, /) -> bool: ...


class BST[T: Comparable](BinaryTree[T]):
    """
    Represent a binary search tree.

    A binary search tree maintains the ordering property that values
    smaller than a node are stored in its left subtree and values
    greater than a node are stored in its right subtree.
    """

    def __init__(self) -> None:
        """
        Initialize an empty binary search tree.
        """
        super().__init__()

    # =====================================================
    # INSERT
    # =====================================================

    def insert(self, value: T) -> BinaryNode[T]:
        """
        Insert a value into the binary search tree.

        Duplicate values are not inserted.

        :param value: The value to insert.
        :return: The node containing ``value``. If the value already exists,
            the existing node is returned.
        """
        new_node = BinaryNode(value)

        if self.root is None:
            self.root = new_node
            self._size = 1
            return new_node

        current: BinaryNode[T] | None = self.root
        parent: BinaryNode[T] | None = None

        while current is not None:
            parent = current

            if value < current.value:
                current = current.left

            elif value > current.value:
                current = current.right

            else:
                return current

        assert parent is not None

        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        self._size += 1

        return new_node

    # =====================================================
    # FIND
    # =====================================================

    def find(self, value: T) -> BinaryNode[T] | None:
        """
        Find a node containing ``value``.

        :param value: The value to search for.
        :return: The matching node, or ``None`` if the value is not found.
        """
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

    def minimum(self, node: BinaryNode[T] | None = None) -> BinaryNode[T] | None:
        """
        Find the minimum-valued node in a subtree.

        If ``node`` is not provided, the search starts at the tree root.

        :param node: The node at which to start the search.
        :return: The minimum-valued node, or ``None`` if the tree is empty.
        """
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

    def maximum(self, node: BinaryNode[T] | None = None) -> BinaryNode[T] | None:
        """
        Find the maximum-valued node in a subtree.

        If ``node`` is not provided, the search starts at the tree root.

        :param node: The node at which to start the search.
        :return: The maximum-valued node, or ``None`` if the tree is empty.
        """
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

    def successor(self, node: BinaryNode[T] | None) -> BinaryNode[T] | None:
        """
        Find the inorder successor of a node.

        :param node: The node whose successor should be found.
        :return: The inorder successor, or ``None`` if no successor exists.
        """
        if node is None:
            return None

        if node.right is not None:
            return self.minimum(node.right)

        successor: BinaryNode[T] | None = None
        current = self.root

        while current is not None:
            if node.value < current.value:
                successor = current
                current = current.left
            elif node.value > current.value:
                current = current.right
            else:
                break

        return successor

    # =====================================================
    # PREDECESSOR
    # =====================================================

    def predecessor(self, node: BinaryNode[T] | None) -> BinaryNode[T] | None:
        """
        Find the inorder predecessor of a node.

        :param node: The node whose predecessor should be found.
        :return: The inorder predecessor, or ``None`` if no predecessor exists.
        """
        if node is None:
            return None

        if node.left is not None:
            return self.maximum(node.left)

        predecessor: BinaryNode[T] | None = None
        current = self.root

        while current is not None:
            if node.value > current.value:
                predecessor = current
                current = current.right
            elif node.value < current.value:
                current = current.left
            else:
                break

        return predecessor

    # =====================================================
    # DELETE
    # =====================================================

    def delete(self, value: T) -> bool:
        """
        Delete a value from the binary search tree.

        :param value: The value to delete.
        :return: ``True`` if the value was found and deleted, otherwise
            ``False``.
        """
        parent: BinaryNode[T] | None = None
        node = self.root

        # Find the node and its parent.
        while node is not None and node.value != value:
            parent = node

            if value < node.value:
                node = node.left
            else:
                node = node.right

        if node is None:
            return False

        # Case 1: node has no left child.
        if node.left is None:
            replacement = node.right

        # Case 2: node has no right child.
        elif node.right is None:
            replacement = node.left

        # Case 3: node has two children.
        else:
            successor_parent = node
            successor = node.right

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            if successor_parent != node:
                successor_parent.left = successor.right
                successor.right = node.right

            replacement = successor
            replacement.left = node.left

        if parent is None:
            self.root = replacement
        elif parent.left is node:
            parent.left = replacement
        else:
            parent.right = replacement

        self._size -= 1

        return True

    # =====================================================
    # EXTRA
    # =====================================================

    def min(self) -> BinaryNode[T] | None:
        """
        Return the minimum-valued node in the tree.

        :return: The minimum-valued node, or ``None`` if the tree is empty.
        """
        return self.minimum()

    def max(self) -> BinaryNode[T] | None:
        """
        Return the maximum-valued node in the tree.

        :return: The maximum-valued node, or ``None`` if the tree is empty.
        """
        return self.maximum()

    def __repr__(self) -> str:
        """
        Return the string representation of the binary search tree.

        :return: A string containing the tree type and node count.
        """
        return f"BST(size={self._size})"
