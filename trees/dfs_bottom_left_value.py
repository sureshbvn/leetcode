class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

def findBottomLeftValue(root):
    leftLevel = [0,0]

    def helper(node, level):
            
        if level == leftLevel[0]:
            leftLevel[1]= node.val
            leftLevel[0] = leftLevel[0]+1
            
        if node.left:
                helper(node.left, level+1)
        if node.right:
                helper(node.right, level+1)
        
    helper(root, 0)
    return leftLevel[-1]
            
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print("The bottom left value", findBottomLeftValue(root))