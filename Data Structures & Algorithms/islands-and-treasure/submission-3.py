class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [ [1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add( (r,c) )


        def addCell(row, col) :
            if ( min(row, col) < 0 or row >= ROWS or col >= COLS or (row, col) in visited or grid[row][col] == -1 ):
                return
            visited.add((row, col))
            q.append((row, col))

        
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                for dr, dc in directions:
                    addCell(r + dr, c + dc)
            distance += 1