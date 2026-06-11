# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        self.dfs(root)

        return self.diameter
    
    def dfs(self, cur): # return max height between left and right subtrees
        if not cur:
            return 0
        
        left = self.dfs(cur.left)
        right = self.dfs(cur.right)
        self.diameter = max(self.diameter, left + right)
        return max(left, right) + 1
    
