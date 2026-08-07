from abc import ABC, abstractmethod


class BinaryTreeIterator(ABC):
    """
    Base class for all binary tree iterators.
    """

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass