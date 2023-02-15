class Node:

    def __init__(self, root, left=None, right=None, x=0, y=0) -> None:
        self.root = root
        self.left = left
        self.right = right
        self.x = x
        self.y = y

    def insert(self, value):
        if value < self.root:
            if self.left is None:
                self.x -= 50
                self.y += 50
                self.left = Node(value, x=self.x, y=self.y)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.x += 50
                self.y += 50
                self.right = Node(value, x=self.x, y=self.y)
            else:
                self.right.insert(value)