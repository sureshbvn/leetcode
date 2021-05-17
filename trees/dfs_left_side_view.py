class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

def leftSideView(root):
    if root is None:
        return []
    
    leftSide = []
    def helper(node, level):
        
        if level==len(leftSide):
            leftSide.append(node.val)
        
        if node.left:
            helper(node.left, level+1)
        if node.right:
            helper(node.right, level+1)
    
    helper(root, 0)
    return leftSide

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print("The right view", leftSideView(root))