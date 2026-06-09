# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # If it's empty -> true
        if not root:
            return True
        
        # Feed the left, right tree into the checking function
        return self.isMirror(root.left, root.right)
    

    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:

        # If not left and not right -> True
        if not left and not right:
            return True
        
        # If either left/right is empty or their value (two sides of the mirror) doesn't match -> False
        if not left or not right or left.val != right.val:
            return False 
        
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

        
