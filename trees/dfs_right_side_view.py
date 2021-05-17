class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    if root is None:
        return []
        
    rightSide = [] 
    def helper(node, level):
            
        if level == len(rightSide):
            rightSide.append(node.val)
            
        for child in [node.right, node.left]:
            if child:
                helper(child, level+1)
        
    helper(root, 0)
    return rightSide

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print("The right view", rightSideView(root))