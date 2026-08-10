from typing import TypeVar

from nodes import BinaryNode
from .base_iterator import BinaryTreeIterator

T = TypeVar("T")


class PostOrderIterator(BinaryTreeIterator[BinaryNode[T]]):
    """
    Traverses a binary tree in Postorder.
    Left -> Right -> Root
    """

    def __init__(self, root: BinaryNode[T] | None) -> None:
        self._stack: list[tuple[BinaryNode[T], bool]] = []

        if root is not None:
            self._stack.append((root, False))

    def __next__(self) -> BinaryNode[T]:
        while self._stack:
            node, visited = self._stack.pop()

            if visited:
                return node

            self._stack.append((node, True))

            if node.right is not None:
                self._stack.append((node.right, False))

            if node.left is not None:
                self._stack.append((node.left, False))

        raise StopIteration
