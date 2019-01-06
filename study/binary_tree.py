class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def inorder(self, node):
        if node:
            res = []
            a = self.inorder(node.left)
            a and res.extend(a)
            res.extend([node.data])
            b = self.inorder(node.right)
            b and res.extend(b)
            return res

    def preoder(self, node):
        if node:
            print(node.data)
            self.preoder(node.left)
            self.preoder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

    def make_node(self, data, left=None, right=None):
        n = Node(data)
        n.left = left
        n.right = right
        return n


tree = BinaryTree()
n1 = tree.make_node(4)
n2 = tree.make_node(5)
n3 = tree.make_node(2, n1, n2)
n4 = tree.make_node(3)
n5 = tree.make_node(1, n3, n4)  # root

print("inorder", tree.inorder(n5))

# print("orerder")
# tree.preoder(n5)
# print("postorder")
# tree.postorder(n5)