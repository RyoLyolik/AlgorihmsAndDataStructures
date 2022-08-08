class Node:
    def __init__(self, val:int):
        self.parent = None
        self.left = None
        self.right = None
        self.value = val

    def __repr__(self):
        return str(self.value)

class Tree:
    def __init__(self, val:float, l=None, r=None):
        self.parent = Node(val)
        self.left = None
        self.right = None
        self.parent.left = self.left
        self.parent.right = self.right
        self.value = self.parent.value

    @staticmethod
    def __insertion(node, val):
        if val < node.value:
            if node.left is None:
                node.left = Node(val)
                node.left.parent = node
                return None

            Tree.__insertion(node.left, val)
            return None
        if node.right is None:
            node.right = Node(val)
            node.right.parent = node
            return None

        Tree.__insertion(node.right, val)
        return None

    def insert(self, val):
        self.__insertion(self.parent, val)
        self.left = self.parent.left
        self.right = self.parent.right

    # def search(self, val):


if __name__ == '__main__':
    t = Tree(3)
    print(t.parent)
    t.insert(2)

    t.insert(4)
    t.insert(5)
    t.insert(3.5)
    print(t.right.left)