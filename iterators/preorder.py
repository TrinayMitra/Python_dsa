from nodes import BinaryNode
from .base_iterator import BinaryTreeIterator


class PreOrderIterator(BinaryTreeIterator):
    """
    Traverses a binary tree in Preorder.
    Root -> Left -> Right
    """

    def __init__(self, root: BinaryNode):
        self._stack = []

        if root is not None:
            self._stack.append(root)

    def __next__(self):

        if not self._stack:
            raise StopIteration

        node = self._stack.pop()

        if node.right is not None:
            self._stack.append(node.right)

        if node.left is not None:
            self._stack.append(node.left)

        return node