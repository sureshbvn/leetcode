# Given the root of a binary search tree and a node p in it, return the in-order 
# successor of that node in the BST. 
# If the given node has no in-order successor in the tree, return null.
# The successor of a node p is the node with the smallest key greater than p.val.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderSuccessor(root, p):
    succ = None

    while root is not None:
        if p.val >= root.val:
            root = root.right
        else:
            succ = root
            root = root.left
    return succ





root = TreeNode(7)
root.left = TreeNode(4)
root.right = TreeNode(10)
root.left.left = TreeNode(2)
root.left.left.right = TreeNode(3)
root.right.left = TreeNode(8)
root.right.right = TreeNode(12)
node = inorderSuccessor(root, root.left.left)
print(node.val)
