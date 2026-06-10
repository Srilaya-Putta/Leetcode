# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.c += 1
            if self.c == k:
                self.a = node.val
                return self.a
            dfs(node.right)

        self.a = self.c = 0
        dfs(root)
        return self.a
