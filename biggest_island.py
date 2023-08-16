class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        biggestIsland = 0

        def dfs(r, c):
            if r >= ROW or c >= COL or r<0 or c<0:
                return 0
            if grid[r][c] != 1:
                return 0
            grid[r][c] = 0

            area = 1

            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)

            return area


        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    biggestIsland = max(biggestIsland, dfs(r, c))

        return biggestIsland