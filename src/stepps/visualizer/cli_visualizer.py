from stepps.trees.binary_tree import BinaryTree
from stepps.visualizer.tree_visualizer import TreeVisualizer


class CliTreeVisualizer[T](TreeVisualizer[BinaryTree[T]]):
    """
    Define the interface for CLI-based binary tree visualization.
    """

    ...