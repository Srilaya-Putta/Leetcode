# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        currentNodes = [root]
        while len(currentNodes) > 0:
            newNodes = []
            for c in currentNodes:
                if c.left:
                    newNodes.append(c.left)
                if c.right:
                    newNodes.append(c.right)
            if newNodes == []:
                return currentNodes[0].val
            currentNodes = newNodes
        return root.val
