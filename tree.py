class TreeNode:
    def __init__(self, cargo = None, left = None, right = None):
        self.cargo = cargo
        self.left = left
        self.right = right
    def __str__(self):
        return '('+str(self.cargo)+')'
    
class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root
        