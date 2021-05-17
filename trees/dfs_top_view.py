class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def topView(root):
    if root is None:
        return []
    
    dict = {}
    def helper(node, x, y):
        if x not in dict:
            dict[x] = {}
        
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
        elem = -1
        for y in sorted(dict[x].keys()):
            if elem < 0:
                elem = dict[x][y][0]
        output.append(elem)
    
    return output

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(8)
root.left.left = TreeNode(4)
root.left.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.right = TreeNode(7)
print("The top view", topView(root))