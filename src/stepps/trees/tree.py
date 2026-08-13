from abc import ABC, abstractmethod


class Tree[T](ABC):
    """
    Define the common interface for tree implementations.
    """

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Return whether the tree is empty.

        :return: ``True`` if the tree contains no nodes, otherwise ``False``.
        """
        ...

    @abstractmethod
    def clear(self) -> None:
        """
        Remove all nodes from the tree.
        """
        ...

    @abstractmethod
    def size(self) -> int:
        """
        Return the number of nodes in the tree.

        :return: The number of nodes in the tree.
        """
        ...

    def __len__(self) -> int:
        """
        Return the number of nodes in the tree.

        :return: The number of nodes in the tree.
        """
        return self.size()

    def __bool__(self) -> bool:
        """
        Return whether the tree contains at least one node.

        :return: ``True`` if the tree is not empty, otherwise ``False``.
        """
        return not self.is_empty()
