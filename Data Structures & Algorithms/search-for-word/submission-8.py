class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(index, row, col, path):

            if index == len(word) - 1:
                return True

            for r, c in [(row + 1, col), (row - 1, col),
                         (row, col + 1), (row, col - 1)]:

                if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                    continue

                if (r, c) in path:
                    continue

                if board[r][c] != word[index + 1]:
                    continue

                path.add((r, c))

                if dfs(index + 1, r, c, path):
                    return True

                path.remove((r, c))

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(0, i, j, {(i, j)}):
                        return True

        return False