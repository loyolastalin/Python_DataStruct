class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.root = self._insert(data, self.root)

    def _insert(self, data, current):
        if not current:
            return Node(data)
        if current.data > data:
            current.left = self._insert(data, current.left)
        elif current.data < data:
            current.right = self._insert(data, current.right)
        else:
            raise Exception("duplicate node not allowed")
        current.height = max(self._height(current.left), self._height(current.right)) + 1

        balance = self._balance(current)

        # left, left
        if balance > 1 and data < current.left.data:
            return self._rightRotate(current)
        # right, right
        if balance < -1 and data > current.right.data:
            return self._leftRotate(current)

        # left, right
        if balance > 1 and data < current.left.data:
            current.left = self._leftRotate(current.left)
            return self._rightRotate(current)

        # right, right
        if balance < -1 and data < current.right.data:
            current.right = self._rightRotate(current.right)
            return self._leftRotate(current)

        return current

    def _height(self, current):
        if not current:
            return 0
        return current.height

    def _balance(self, current):
        if not current:
            return 0
        return self._height(current.left) - self._height(current.right)

    def _rightRotate(self, root):
        newRoot = root.left
        rootRightNode = newRoot.right
        newRoot.right = root
        root.left = rootRightNode
        root.height = max(self._height(root.left), self._height(root.right)) + 1
        newRoot.height = max(self._height(newRoot.left), self._height(newRoot.right)) + 1
        return newRoot

    def _leftRotate(self, root):
        newRoot = root.right
        newRootLeftNode = newRoot.left
        newRoot.left = root
        root.right = newRootLeftNode
        root.height = max(self._height(root.left), self._height(root.right)) + 1
        newRoot.height = max(self._height(newRoot.left), self._height(newRoot.right)) + 1
        return newRoot

    def inorder_traversal(self):
        self._print(self.root)

    def _print(self, current):
        if current:
            self._print(current.left)
            print("Data " + str(current.data) + " height " + str(current.height))
            self._print(current.right)


avl = AVL_Tree()
avl.insert(3)
avl.insert(4)
avl.insert(6)
avl.insert(0)
avl.insert(-1)
avl.insert(8)
avl.inorder_traversal()
