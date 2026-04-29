class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid),len(grid[0])
        q = deque()
        fresh, time = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        directions = [
            [1,0],
            [-1,0],
            [0,1],
            [0,-1]
        ]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dir_r, dir_c in directions:
                    row, col = r + dir_r, c + dir_c
                    if ( row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    fresh -= 1
                    q.append([row,col])
            time += 1
        return time if fresh == 0 else -1






