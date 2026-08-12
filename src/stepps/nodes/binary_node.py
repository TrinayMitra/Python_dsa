from __future__ import annotations


class BinaryNode[T]:
    """
    Represent a node in a binary tree.

    :ivar value: The value stored in the node.
    :ivar left: The left child of the node, if any.
    :ivar right: The right child of the node, if any.
    :ivar parent: The parent of the node, if any.
    """

    def __init__(self, value: T) -> None:
        """
        Initialize a binary tree node.

        :param value: The value to store in the node.
        """
        self.value: T = value
        self.left: BinaryNode[T] | None = None
        self.right: BinaryNode[T] | None = None
        self.parent: BinaryNode[T] | None = None

    def is_leaf(self) -> bool:
        """
        Return whether the node has no children.

        :return: ``True`` if the node has no children, otherwise ``False``.
        """
        return self.left is None and self.right is None

    def has_left(self) -> bool:
        """
        Return whether the node has a left child.

        :return: ``True`` if a left child exists, otherwise ``False``.
        """
        return self.left is not None

    def has_right(self) -> bool:
        """
        Return whether the node has a right child.

        :return: ``True`` if a right child exists, otherwise ``False``.
        """
        return self.right is not None

    def has_children(self) -> bool:
        """
        Return whether the node has at least one child.

        :return: ``True`` if the node has one or more children, otherwise ``False``.
        """
        return self.left is not None or self.right is not None

    def child_count(self) -> int:
        """
        Return the number of children of the node.

        :return: The number of children, either ``0``, ``1``, or ``2``.
        """
        return int(self.left is not None) + int(self.right is not None)

    def sibling(self) -> BinaryNode[T] | None:
        """
        Return the sibling of the node.

        :return: The sibling node, or ``None`` if the node has no parent or
            sibling.
        """
        if self.parent is None:
            return None

        if self.parent.left is self:
            return self.parent.right

        return self.parent.left

    def __repr__(self) -> str:
        """
        Return the string representation of the node.

        :return: A string containing the node's value.
        """
        return f"BinaryNode({self.value})"
