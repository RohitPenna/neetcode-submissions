class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        column = {}
        squares = {}

        for i in range(10):
            rows[i] = set()
            column[i] = set()
            squares[i] = set()

        x = len(board)
        for i in range (x):
            for j in range (x):
                y = board[i][j]
                if y.isdigit():
                    print(y)
                    num = (i // 3) * 3 + (j // 3)
                    if y in rows[i]:
                        return False
                    elif y in column[j]:
                        return False
                    elif y in squares[num]:
                        return False
                    rows[i].add(y)
                    column[j].add(y)
                    squares[num].add(y)

        return True