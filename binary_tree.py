class Tree_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Binary_tree:
    def __init__(self):
        self.root = None

    def new_root(self, data):
        self.root = Tree_node(data)

    def bst_add(self, current, data):
        if self.root is None:
            self.root = Tree_node(data)
            return

        if current.data > data:
            if current.left is None:
                current.left = Tree_node(data)
            else:
                self.bst_add(current=current.left, data=data)
        else:
            if current.right is None:
                current.right = Tree_node(data)
            else:
                self.bst_add(current=current.right, data=data)

    def find_node(self, value):
        node = self.root

        while node is not None:
            if node.data == value:
                return node
            if value > node.data:
                if node.right is not None:
                    node = node.right
                else:
                    return
            if value < node.data:
                if node.left is not None:
                    node = node.left
                else:
                    return
        return None

    def DFS(self, node):
        if node is None:
            return

        self.DFS(node.left)
        print(f"[{node.data}]", end="")
        self.DFS(node.right)

    def BFS(self):
        pass


def print_tree_func(current_root, level):
    print(f"({current_root.data})")
    level += 1

    if current_root.left is not None:
        print(level*"\t\t", end='')
        print(f"____{level}|l", end='')
        print_tree_func(current_root=current_root.left, level=level)

    if current_root.right is not None:
        print(level*"\t\t", end='')
        print(f"____{level}|r", end='')
        print_tree_func(current_root=current_root.right, level=level)


def bst_add_func(root, data):
    if root is None:
        new_node = Tree_node(data)
        return new_node

    if root.data > data:
        root.left = bst_add_func(root.left, data)
    else:
        root.right = bst_add_func(root.right, data)

    return root


def delete_node(root, data):
    pass














