from stepps.nodes import BinaryNode

from .base_iterator import BinaryTreeIterator


class InOrderIterator[T](BinaryTreeIterator[BinaryNode[T]]):
    """
    Traverses a binary tree in Inorder.
    Left -> Root -> Right
    """

    def __init__(self, root: BinaryNode[T] | None) -> None:
        self._stack: list[BinaryNode[T]] = []
        self._current: BinaryNode[T] | None = root

    def __next__(self) -> BinaryNode[T]:
        while self._current is not None:
            self._stack.append(self._current)
            self._current = self._current.left

        if not self._stack:
            raise StopIteration

        node = self._stack.pop()
        self._current = node.right

        return node
