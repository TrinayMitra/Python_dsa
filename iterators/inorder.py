from nodes import BinaryNode
from .base_iterator import BinaryTreeIterator


class InOrderIterator(BinaryTreeIterator):
    """
    Traverses a binary tree in Inorder.
    Left -> Root -> Right
    """

    def __init__(self, root: BinaryNode):
        self._stack = []
        self._current = root

    def __next__(self):

        while self._current is not None:
            self._stack.append(self._current)
            self._current = self._current.left

        if not self._stack:
            raise StopIteration

        node = self._stack.pop()
        self._current = node.right

        return node