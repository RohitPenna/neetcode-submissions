class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(s, row, col, path):

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            
            if s == word:
                return True
            
            if len(s) > len(word):
                return False
            
            for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                    continue
                if (r, c) in path:
                    continue
                
                path.add((r,c))
                
                if dfs(s + board[r][c], r, c, path):
                    return True
                
                path.remove((r,c))

            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    s = word[0]
                    x = dfs(s, i, j, {(i, j)})
                    if x:
                        return True
        
        return False