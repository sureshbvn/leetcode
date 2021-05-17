# Definition for a binary tree node.
# Given the root of a binary tree, return the vertical order 
# traversal of its nodes' values. (i.e., from top to bottom, 
#  column by column).
# If two nodes are in the same row and column, the order should
#  be from left to right.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalOrder(root):
        
    if root is None:
        return []
        
    dict = {}
    def helper(node, x, y):
        if x not in dict:
                dict[x] = {}
            
        # At this point we know x is in the hashmap.
        if y not in dict[x]:
            dict[x][y] = [node.val]
        else:
            dict[x][y].append(node.val)
                
            
        if node.left:
            helper(node.left, x-1, y+1)
        if node.right:
            helper(node.right, x+1, y+1)
        
    helper(root, 0, 0)
    output = []
    for x in sorted(dict.keys()):
        temp = []
        for y in sorted(dict[x].keys()):
            temp.extend(dict[x][y])
        output.append(temp)
    return output

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(8)
root.left.left = TreeNode(4)
root.left.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.right = TreeNode(7)
print("The vertical order traversal", verticalOrder(root))