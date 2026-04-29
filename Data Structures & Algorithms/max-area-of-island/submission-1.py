class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [
            [1,0],
            [0,1],
            [-1,0],
            [0,-1]
        ]
        ROWS, COLS = len(grid), len(grid[0])
        maxSize = 0

        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]==0:
                return 0
            grid[r][c]=0
            size = 1
            for [dir_r, dir_c] in dirs:
                size += dfs(r + dir_r, c + dir_c)
            return size

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    cur_size = dfs(r,c)
                    maxSize = max(cur_size, maxSize)
        return maxSize