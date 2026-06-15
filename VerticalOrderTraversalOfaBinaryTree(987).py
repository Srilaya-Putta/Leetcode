class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []
        
        def dfs(node, row, col):
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)
        nodes.sort()
        
        result = []
        from collections import defaultdict
        col_map = defaultdict(list)
        
        for col, row, val in nodes:
            col_map[col].append(val)
        
        for col in sorted(col_map.keys()):
            result.append(col_map[col])
        
        return result
