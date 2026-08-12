from abc import ABC, abstractmethod
from collections.abc import Iterator
from typing import Self


class BinaryTreeIterator[T](ABC, Iterator[T]):
    """
    Base class for all binary tree iterators.

    This class defines the iterator interface used by binary tree
    traversal implementations.
    """

    def __iter__(self) -> Self:
        """
        Return the iterator itself.

        :return: The current iterator instance.
        """
        return self

    @abstractmethod
    def __next__(self) -> T:
        """
        Return the next item in the traversal.

        :return: The next item produced by the iterator.
        :raises StopIteration: When there are no more items to traverse.
        """
        ...
