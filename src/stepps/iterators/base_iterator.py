from abc import ABC, abstractmethod
from collections.abc import Iterator
from typing import Self


class BinaryTreeIterator[T](ABC, Iterator[T]):
    """Base class for all binary tree iterators."""

    def __iter__(self) -> Self:
        return self

    @abstractmethod
    def __next__(self) -> T:
        pass
