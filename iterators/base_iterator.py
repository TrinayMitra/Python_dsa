from abc import ABC, abstractmethod


class BinaryTreeIterator(ABC):

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass