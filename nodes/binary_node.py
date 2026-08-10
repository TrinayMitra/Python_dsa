from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class BinaryNode(Generic[T]):
    """Represents a node in a binary tree."""

    def __init__(self, value: T) -> None:
        self.value: T = value
        self.left: BinaryNode[T] | None = None
        self.right: BinaryNode[T] | None = None
        self.parent: BinaryNode[T] | None = None

    def is_leaf(self) -> bool:
        """
        Returns True if the node has no children.
        """
        return self.left is None and self.right is None

    def has_left(self) -> bool:
        return self.left is not None

    def has_right(self) -> bool:
        return self.right is not None

    def has_children(self) -> bool:
        return self.left is not None or self.right is not None

    def child_count(self) -> int:
        return int(self.left is not None) + int(self.right is not None)

    def sibling(self) -> BinaryNode[T] | None:
        if self.parent is None:
            return None

        if self.parent.left is self:
            return self.parent.right

        return self.parent.left

    def __repr__(self) -> str:
        return f"BinaryNode({self.value})"