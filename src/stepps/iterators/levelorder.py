from collections import deque

from stepps.iterators.base_iterator import BinaryTreeIterator
from stepps.nodes import BinaryNode


class LevelOrderIterator[T](BinaryTreeIterator[BinaryNode[T]]):
    """
    Iterate over a binary tree using level-order traversal.

    Nodes are visited level by level, from left to right.

    :param root: The root node of the tree to traverse.
    """

    def __init__(self, root: BinaryNode[T] | None) -> None:
        self._queue: deque[BinaryNode[T]] = deque()

        if root is not None:
            self._queue.append(root)

    def __next__(self) -> BinaryNode[T]:
        """
        Return the next node in the level-order traversal.

        :return: The next node in the traversal.
        :raises StopIteration: If all nodes have been visited.
        """
        if not self._queue:
            raise StopIteration

        node = self._queue.popleft()

        if node.left is not None:
            self._queue.append(node.left)

        if node.right is not None:
            self._queue.append(node.right)

        return node
