class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def maxDepth(root): 
    def helper(node):
        if node is None:
            return 0
            
        return max(helper(node.left), helper(node.right)) + 1
        
    return helper(root)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print("The height of the tree", maxDepth(root))
    

        