class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def upsideDownBinaryTree(root):
    if root is None:
        return None
        
    globalroot = [None]
        
    def dfs(node, parentNode, rightNode):
        oldleft = node.left
        oldright = node.right
            
        # We are currently at the first leaf node.
        if node.left is None and node.right is None:
            globalroot[0] = node
            
        # For all nodes do the following work. 
        node.left = rightNode
        node.right = parentNode
            
        if oldleft is not None:
            dfs(oldleft, node, oldright)
        
    dfs(root, None, None)
    return globalroot[0]


def dfs(root):
    output = []
    def helper(node):
        output.append(node.val)
        if node.left:
            helper(node.left)
        if node.right:
            helper(node.right)
    
    helper(root)
    return output

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
newroot = upsideDownBinaryTree(root)
print("The new tree", dfs(newroot))   