class BinaryNode:
    """
    Represents a node in a binary tree.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def is_leaf(self):
        """
        Returns True if the node has no children.
        """
        return self.left is None and self.right is None

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def has_children(self):
        return self.left is not None or self.right is not None

    def child_count(self):
        return int(self.left is not None) + int(self.right is not None)

    def sibling(self):
        if self.parent is None:
            return None

        if self.parent.left is self:
            return self.parent.right

        return self.parent.left

    def __repr__(self):
        return f"BinaryNode({self.value})"