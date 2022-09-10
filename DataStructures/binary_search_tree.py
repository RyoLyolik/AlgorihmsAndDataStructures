from queue_ import Queue_

class Node:
    def __init__(self, val: float, parent = None):
        self.parent = parent
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
        self.root = Node(val)
        self.root.left = None
        self.root.right = None
        self.value = self.root.value

    @staticmethod
    def __insertion(node, val):
        if val < node.value:
            if node.left is None:
                node.left = Node(val, parent=node)
                return None

            Tree.__insertion(node.left, val)
            return None
        if node.right is None:
            node.right = Node(val, parent=node)
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

    def find(self, val) -> [Node]:
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
    def __traverse_preorder(node):
        print(node)
        if node.left is not None:
            Tree.__traverse_preorder(node.left)
        if node.right is not None:
            Tree.__traverse_preorder(node.right)

    def traverse_preorder(self):
        return Tree.__traverse_preorder(self.root)

    @staticmethod
    def __traverse_inorder(node):
        if node.left is not None:
            Tree.__traverse_inorder(node.left)
        print(node)
        if node.right is not None:
            Tree.__traverse_inorder(node.right)

    def traverse_inorder(self):
        return Tree.__traverse_inorder(self.root)

    @staticmethod
    def __traverse_postorder(node):
        if node.left is not None:
            Tree.__traverse_postorder(node.left)
        if node.right is not None:
            Tree.__traverse_postorder(node.right)

        print(node)

    def traverse_postorder(self):
        return Tree.__traverse_postorder(self.root)

    def breadth_first_search(self):
        q = Queue_(self.root)

        while not q.is_empty():
            node = q.dequeue()
            yield node
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)


if __name__ == '__main__':
    import random

    n = 20
    t = Tree(n // 2)
    random_list = [int(random.uniform(0.0, 1.0) * n) for i in range(n)]
    print("Insertion")
    k = 0
    for i in range(n):
        t.insert(random_list[i])
    print("Traverse")
    g=t.breadth_first_search()
    for i in g:
        print(i)


