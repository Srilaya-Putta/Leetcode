class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == '1'
        def dfs(row, col):
            for dx, dy in directions:
                nextRow, nextCol = row + dx, col + dy
                key = (nextRow, nextCol)

                if isValid(nextRow, nextCol):
                    grid[nextRow][nextCol] = '0'
                    dfs(nextRow, nextCol)
        
        m, n = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        ans = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '0':
                    continue

                ans += 1
                grid[row][col] = '0'
                dfs(row, col)

        return ans
