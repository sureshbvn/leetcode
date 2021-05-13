# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two 
# nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of 
# edges between them.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    def helper(node):
        if node is None:
            return [0, 0]
            
            
        if node.left is None and node.right is None:
            return [0,1]
            
        l = helper(node.left)
        r = helper(node.right)
        nd = max(l[0], r[0], l[1]+r[1])
        return [nd, max(l[1], r[1])+1]
        
    return helper(root)[0]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print("The diameter of the tree", diameterOfBinaryTree(root))