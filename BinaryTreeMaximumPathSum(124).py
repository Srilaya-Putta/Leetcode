# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.max_v = -(1 << 31)
        s = [0]
        self.visit(root, s)
        return self.max_v

    def visit(self, root, s):
        if not root:
            return
        if not root.left and not root.right:
            s[0] = root.val
            self.max_v = max(self.max_v, s[0])
            return
        if root.left and not root.right:
            l = [0]
            self.visit(root.left, l)
            s[0] = max(root.val, l[0] + root.val)
            self.max_v = max(
                self.max_v,
                root.val,
                l[0],
                l[0] + root.val
            )
            return
        if not root.left and root.right:
            r = [0]
            self.visit(root.right, r)
            s[0] = max(root.val, r[0] + root.val)
            self.max_v = max(
                self.max_v,
                root.val,
                r[0],
                r[0] + root.val
            )
            return
        l, r = [0], [0]
        self.visit(root.left, l)
        self.visit(root.right, r)
        s[0] = max(max(l[0], r[0]) + root.val, root.val)
        self.max_v = max(
            self.max_v,
            l[0],
            r[0],
            root.val,
            l[0] + root.val,
            r[0] + root.val,
            l[0] + root.val + r[0]
        )
