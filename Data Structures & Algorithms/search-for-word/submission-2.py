class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # to keep track of recent path to avoid overlapping recursions

        def dfs(r, c, i):
            if i == len(word):  # if the length of the word has been reached
                return True
            if ( r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path):  
                return False
            path.add((r,c))   # add the current coordinate to the path
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)) # run the recursion in all directions
            path.remove((r,c)) # remove the coordinate as all neighbours have been visited
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

