from nodes import BinaryNode
from .base_iterator import BinaryTreeIterator


class PostOrderIterator(BinaryTreeIterator):
    """
    Traverses a binary tree in Postorder.
    Left -> Right -> Root
    """

    def __init__(self, root: BinaryNode):
        self._stack = []

        if root is not None:
            self._stack.append((root, False))

    def __next__(self):

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