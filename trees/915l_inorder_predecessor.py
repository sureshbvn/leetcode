class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderPredecessor(root, p):
    pred = None

    while root is not None:
        if p.val > root.val:
            pred = root
            root = root.right
        else:
            root = root.left
    return pred

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
node = inorderPredecessor(root, root.left)
print("The inorder predecssor", node.val) 
    

