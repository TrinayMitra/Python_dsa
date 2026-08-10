from typing import TypeVar

from nodes import BinaryNode

from .base_iterator import BinaryTreeIterator

T = TypeVar("T")


class PreOrderIterator(BinaryTreeIterator[BinaryNode[T]]):
    """
    Traverses a binary tree in Preorder.
    Root -> Left -> Right
    """

    def __init__(self, root: BinaryNode[T] | None) -> None:
        self._stack: list[BinaryNode[T]] = []

        if root is not None:
            self._stack.append(root)

    def __next__(self) -> BinaryNode[T]:
        if not self._stack:
            raise StopIteration

        node = self._stack.pop()

        if node.right is not None:
            self._stack.append(node.right)

        if node.left is not None:
            self._stack.append(node.left)

        return node
