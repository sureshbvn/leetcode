import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalOrder(root):
        
    if root is None:
        return []
        
    dict = {}
        
    queue = collections.deque([[root, 0]])
    while len(queue) > 0:
        numnodes = len(queue)
        for i in range(0, numnodes):
            item = queue.popleft()
            node = item[0]
            xlevel = item[1]
                
            # Check if xlevel is already present in the map.
            if xlevel in dict:
                dict[xlevel].append(node.val)
            else:
                dict[xlevel] = [node.val]
            
            if node.left:
                queue.append([node.left, xlevel-1])
            if node.right:
                queue.append([node.right, xlevel+1])
        
    output = []
    # Iterate the map and prepare the output.
    for key in sorted(dict.keys()):
        output.append(dict[key])
        
    return output

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print("The vertical order", verticalOrder(root))               