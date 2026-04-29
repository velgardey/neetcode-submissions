class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):
            if ( row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0 or (row, col) in visited ):
                return 0
            
            visited.add( (row, col) )
            current_area = 1

            for dr, dc in directions:
                current_area += dfs(row + dr, col + dc)
            
            return current_area

        area = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, dfs(r, c) )
        
        return area

            