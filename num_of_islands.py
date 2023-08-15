class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        num_islands = 0

        def dfs(r, c):
            nonlocal num_islands
            if r >= ROW or c >= COL or r < 0 or c < 0 or grid[r][c] == 'x' or grid[r][c] == '0':
                return

            # mark r, c as visited
            grid[r][c] = 'x'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r, c)

        return num_islands
