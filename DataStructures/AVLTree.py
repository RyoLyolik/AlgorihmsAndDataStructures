from binary_search_tree import Tree, Node


class AVLNode(Node):
    def __init__(self, val: float, parent=None, is_brother=True):
        super().__init__(val, parent=parent)
        self.left: AVLNode = None
        self.right: AVLNode = None
        self.height = 1

    def deep_delete(self):
        if self.left:
            self.left.deep_delete()
        if self.right:
            self.right.deep_delete()
        self.delete()

    @staticmethod
    def delete(root, val):
        if not root:
            return root
        elif val < root.value:
            root.left = AVLNode.delete(root.left, val)
        elif val > root.value:
            root.right = AVLNode.delete(root.right, val)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = root.right.least_node()
            root.value = temp.value
            root.right = AVLNode.delete(root.right,
                                        temp.value)
        if root is None:
            return root

        root.height = AVLTree.update_height(root)
        diff = AVLNode.get_difference(root)

        if diff > 1:
            if AVLNode.get_difference(root.left) >= 0:
                return AVLNode.rotate_right(root)
            else:
                root.left = AVLNode.rotate_left(root.left)
                return AVLNode.rotate_right(root)
        if diff < -1:
            if AVLNode.get_difference(root.left) <= 0:
                return AVLNode.rotate_left(root.left)
            else:
                root.right = AVLNode.rotate_right(root)
                return AVLNode.rotate_left(root.left)
        return root

    @staticmethod
    def rotate_left(node):
        if node.right:
            r = node.right
            rl = r.left
            r.left = node
            node.right = rl

            node.height = AVLTree.update_height(node)
            r.height = AVLTree.update_height(r)

            return r
        return node

    @staticmethod
    def rotate_right(node):
        if node.left:
            l = node.left
            lr = l.right
            l.right = node
            node.left = lr
            node.height = AVLTree.update_height(node)
            l.height = AVLTree.update_height(l)

            return l
        return node

    @staticmethod
    def get_difference(node):
        if not node.left and node.right:
            difference = -node.right.height
        elif not node.height and node.right:
            difference = node.left.height
        elif node.left and node.right:
            difference = node.left.height - node.right.height
        else:
            difference = 0
        return difference

    def __gt__(self, other):
        if isinstance(other, AVLNode):
            return self.value > other.value
        raise TypeError

    def __lt__(self, other):
        if isinstance(other, AVLNode):
            return self.value < other.value
        raise TypeError

    def __ge__(self, other):
        if isinstance(other, AVLNode):
            return self.value >= other.value
        raise TypeError

    def __le__(self, other):
        if isinstance(other, AVLNode):
            return self.value <= other.value
        raise TypeError

    def __iter__(self):
        if self.left:
            return self.__iter__(self.root)
        return self

    def __next__(self):
        if self.left:
            return self.left

class AVLTree(Tree):
    def __init__(self, val: float):
        super(AVLTree, self).__init__(val)
        self.root = AVLNode(val)

    @staticmethod
    def update_height(node):
        if node.left and node.right:
            h = 1 + max(node.left.height, node.right.height)
        elif not node.left and node.right:
            h = 1 + node.right.height
        elif node.left and not node.right:
            h = 1 + node.left.height
        else:
            h = 1
        return h

    @staticmethod
    def __insertion(node, val, par=None):
        if node is None:
            return AVLNode(val, par)
        if val < node.value:
            node.left = AVLTree.__insertion(node.left, val, node)
        else:
            node.right = AVLTree.__insertion(node.right, val, node)

        node.height = AVLTree.update_height(node)
        return AVLTree.balance(node, val)

    def insert(self, val):
        self.root = AVLTree.__insertion(self.root, val, self.root.parent)

    @staticmethod
    def balance(root, value):
        diff = AVLNode.get_difference(root)
        if diff > 1:
            if value < root.left.value:
                return AVLNode.rotate_right(root)
            root.left = AVLNode.rotate_left(node=root.left)
            return AVLNode.rotate_right(root)

        if diff < -1:
            if value > root.right.value:
                return AVLNode.rotate_left(root)
            root.right = AVLNode.rotate_right(node=root.right)
            return AVLNode.rotate_left(root)
        return root

    def delete(self, val):
        AVLNode.delete(self.root, val)

    def traverse_inorder(self):
        return AVLTree.__traverse_inorder(self.root)

    @staticmethod
    def __traverse_inorder(node):
        if node.left is not None:
            AVLTree.__traverse_inorder(node.left)
        yield node
        if node.right is not None:
            AVLTree.__traverse_inorder(node.right)

if __name__ == '__main__':
    t = AVLTree(0)
    for i in range(10):
        t.insert(i)
    x = iter(t)
    for i in x:
        print(i)
