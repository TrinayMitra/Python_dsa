import pytest

from stepps.nodes import BinaryNode
from stepps.trees import BinaryTreeImpl


class ConcreteBinaryTree(BinaryTreeImpl[int]):
    """
    Concrete binary tree used for testing ``BinaryTreeImpl``.
    """

    def insert(self, value: int) -> BinaryNode[int]:
        raise NotImplementedError

    def delete(self, value: int) -> bool:
        raise NotImplementedError


@pytest.fixture
def tree():
    tree = ConcreteBinaryTree()

    root = BinaryNode(50)
    root.left = BinaryNode(30)
    root.right = BinaryNode(70)
    root.left.left = BinaryNode(20)
    root.left.right = BinaryNode(40)
    root.right.left = BinaryNode(60)
    root.right.right = BinaryNode(80)

    tree.root = root
    tree._size = 7

    return tree


# =====================================================
# Basic Properties
# =====================================================


def test_new_tree_is_empty():
    tree = ConcreteBinaryTree()

    assert tree.is_empty()
    assert len(tree) == 0
    assert tree.size() == 0
    assert not tree


def test_size(tree):
    assert tree.size() == 7
    assert len(tree) == 7
    assert tree


def test_clear(tree):
    tree.clear()

    assert tree.is_empty()
    assert tree.size() == 0
    assert len(tree) == 0


# =====================================================
# Search
# =====================================================


def test_find_existing(tree):
    node = tree.find(40)

    assert node is not None
    assert node.value == 40


def test_find_missing(tree):
    assert tree.find(999) is None


def test_contains(tree):
    assert 60 in tree


def test_not_contains(tree):
    assert 100 not in tree


# =====================================================
# Tree Statistics
# =====================================================


def test_height(tree):
    assert tree.height() == 2


def test_empty_tree_height():
    tree = ConcreteBinaryTree()

    assert tree.height() == -1


def test_leaf_count(tree):
    assert tree.count_leaves() == 4


def test_empty_tree_leaf_count():
    tree = ConcreteBinaryTree()

    assert tree.count_leaves() == 0


def test_internal_nodes(tree):
    assert tree.count_internal_nodes() == 3


def test_empty_tree_internal_nodes():
    tree = ConcreteBinaryTree()

    assert tree.count_internal_nodes() == 0


# =====================================================
# Representation
# =====================================================


def test_repr(tree):
    assert repr(tree) == "ConcreteBinaryTree(size=7)"
