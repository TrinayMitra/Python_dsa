from stepps.iterators.base_iterator import BinaryTreeIterator
from stepps.nodes import BinaryNode


class InOrderIterator[T](BinaryTreeIterator[BinaryNode[T]]):
    """
    Iterate over a binary tree using inorder traversal.

    The traversal visits nodes in the following order:

    .. code-block:: text

        Left -> Root -> Right

    :param root: The root node of the tree to traverse.
    """

    def __init__(self, root: BinaryNode[T] | None) -> None:
        self._stack: list[BinaryNode[T]] = []
        self._current: BinaryNode[T] | None = root

    def __next__(self) -> BinaryNode[T]:
        """
        Return the next node in the inorder traversal.

        :return: The next node in the traversal.
        :raises StopIteration: If all nodes have been visited.
        """
        while self._current is not None:
            self._stack.append(self._current)
            self._current = self._current.left

        if not self._stack:
            raise StopIteration

        node = self._stack.pop()
        self._current = node.right

        return node
