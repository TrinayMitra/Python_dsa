from abc import ABC, abstractmethod


class TreeVisualizer[T](ABC):
    """
    Define the interface for tree visualization.
    """

    @abstractmethod
    def treevisualizer(self, tree: T) -> None:
        """
        Visualize a tree.

        :param tree: The tree to visualize.
        """
        ...
