from stepps.iterators.base_iterator import BinaryTreeIterator
from stepps.nodes import BinaryNode


class PostOrderIterator[T](BinaryTreeIterator[BinaryNode[T]]):
    """
    Iterate over a binary tree using postorder traversal.

    Nodes are visited in the following order:

    .. code-block:: text

        Left -> Right -> Root

    :param root: The root node of the tree to traverse.
    """

    def __init__(self, root: BinaryNode[T] | None) -> None:
        """
        Initialize the postorder iterator.

        :param root: The root node of the tree to traverse.
        """
        self._stack: list[tuple[BinaryNode[T], bool]] = []
        """
        Stack of ``(node, visited)`` tuples.

        ``node`` is the node being processed, and ``visited`` indicates
        whether the node's children have already been processed.
        """

        if root is not None:
            self._stack.append((root, False))

    def __next__(self) -> BinaryNode[T]:
        """
        Return the next node in the postorder traversal.

        :return: The next node in the traversal.
        :raises StopIteration: If all nodes have been visited.
        """
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
