from collections import deque
from typing import TypeVar

from nodes import BinaryNode
from .base_iterator import BinaryTreeIterator

T = TypeVar("T")


class LevelOrderIterator(BinaryTreeIterator[BinaryNode[T]]):
    """
    Traverses a binary tree level by level.
    """

    def __init__(self, root: BinaryNode[T] | None) -> None:
        self._queue: deque[BinaryNode[T]] = deque()

        if root is not None:
            self._queue.append(root)

    def __next__(self) -> BinaryNode[T]:
        if not self._queue:
            raise StopIteration

        node = self._queue.popleft()

        if node.left is not None:
            self._queue.append(node.left)

        if node.right is not None:
            self._queue.append(node.right)

        return node