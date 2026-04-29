class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])  # initiate the ROWS and COLS 
        pacific, atlantic = set(), set()  # these sets store the cell coordinates from which the oceans can be reached

        def dfs(r, c, visited, previousHeight):
            if ( (r,c) in visited or r < 0 or r == ROWS or c < 0 or c == COLS or heights[r][c] < previousHeight ):  # bounds check, duplicate check and water flowing conditon check
                return
            visited.add((r,c)) # add current coordinate to the sets of the respective oceans
            dfs( r + 1, c, visited, heights[r][c])  # expand the recursion to all neighbouring cells
            dfs( r - 1, c, visited, heights[r][c])
            dfs( r, c + 1, visited, heights[r][c])
            dfs( r, c - 1, visited, heights[r][c])

        for c in range(COLS):  # for constant c cases for both atlantic and pacific neighbouring cells
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS): # for constant r cases for both atlantic and pacific neighbouring cells
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        res = [] # result list
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:  # we check if the coordinates are present in both pacific and atlantic
                    res.append((r,c))
        return res