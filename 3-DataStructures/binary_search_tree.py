class Root:
    def __init__(self, val):
        self.value = val
        self.left: Node = None
        self.right: Node = None

    def delete(self):
        if self.left is not None:
            self.left.deep_delete()

        if self.right:
            self.right.deep_delete()

    def __repr__(self):
        return str(self.value)


class Node:
    def __init__(self, val: float):
        self.parent = None
        self.left: Node = None
        self.right: Node = None
        self.value = val

    def __repr__(self):
        return str(self.value)

    def deep_delete(self):
        if self.left:
            self.left.deep_delete()
        if self.right:
            self.right.deep_delete()
        self.delete()

    def delete(self):
        is_left = False
        if self.parent.left is self:
            is_left = True

        if self.left and self.right:
            least = self.right.least_node()
            self.value = least.value
            least.delete()

        elif self.left:
            self.left.parent = self.parent
            if is_left:
                self.parent.left = self.left
            else:
                self.parent.right = self.left

        elif self.right:
            self.parent.left = self.right
            if is_left:
                self.right.parent = self.parent
            else:
                self.parent.right = self.right

        elif not (self.left or self.right):
            if is_left:
                self.parent.left = None
            else:
                self.parent.right = None

    def least_node(self):
        node = self.left
        while node.left is not None:
            node = node.left

        return node

    def greatest_node(self):
        node = self.right
        while node.right is not None:
            node = node.right

        return node


class Tree:
    def __init__(self, val: float):
        self.root = Root(val)
        self.root.left = None
        self.root.right = None
        self.value = self.root.value

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
        self.__insertion(self.root, val)

    @staticmethod
    def __search(node, val):
        if val < node.value:
            if node.left is None:
                return None

            return Tree.__search(node.left, val)
        if val > node.value:
            if node.right is None:
                return None

            return Tree.__search(node.right, val)

        return node

    def find(self, val) -> [Node, Root]:
        node = Tree.__search(self.root, val)
        return node

    def delete(self, val):
        node = self.find(val)
        if node is not None:
            node.delete()

    def least_node(self):
        if self.root.left:
            return self.root.left.least_node()
        return self.root

    def greatest_node(self):
        if self.root.right:
            return self.root.right.greatest_node()
        return self.root

    @staticmethod
    def __traverse(node):
        if node is not None:
            Tree.__traverse(node.left)
            # print(node)
            Tree.__traverse(node.right)

    def traverse_tree(self):
        Tree.__traverse(self.root)

if __name__ == '__main__':
    import random
    t = Tree(500)
    n = 10000000
    random_list = [int(random.uniform(0.0,1.0)*n) for i in range(n)]
    print("Insertion")
    k = 0
    for i in range(n):
        if (i%100000)==0:
            k+=1
            print("Ok", k)
        t.insert(random_list[i])
    print("Start")
    t.traverse_tree()

