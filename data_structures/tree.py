"""Tree implementation for sorting and curriculum organization."""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)


class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def traverse(self, node=None):
        current = node or self.root
        values = [current.value]

        for child in current.children:
            values.extend(self.traverse(child))

        return values
