from stepps.iterators.base_iterator import BinaryTreeIterator
from stepps.nodes import BinaryNode


class PreOrderIterator[T](BinaryTreeIterator[BinaryNode[T]]):
    """
    Iterate over a binary tree using preorder traversal.

    Nodes are visited in the following order:

    .. code-block:: text

        Root -> Left -> Right

    :param root: The root node of the tree to traverse.
    """

    def __init__(self, root: BinaryNode[T] | None) -> None:
        """
        Initialize the preorder iterator.

        :param root: The root node of the tree to traverse.
        """
        self._stack: list[BinaryNode[T]] = []

        if root is not None:
            self._stack.append(root)

    def __next__(self) -> BinaryNode[T]:
        """
        Return the next node in the preorder traversal.

        :return: The next node in the traversal.
        :raises StopIteration: If all nodes have been visited.
        """
        if not self._stack:
            raise StopIteration

        node = self._stack.pop()

        if node.right is not None:
            self._stack.append(node.right)

        if node.left is not None:
            self._stack.append(node.left)

        return node
