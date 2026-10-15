class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = False
        down = False
        up = False
        right = True

        row = 0
        col = 0

        results = []

        for i in range(len(matrix) * len(matrix[0])):
            if right:
                results.append(matrix[row][col])
                matrix[row][col] = None
                if (col+1) < len(matrix[0]):
                    col += 1
                else:
                    right = False
                    down = True
                    row += 1
                    continue
                if matrix[row][col] is None:
                    col -= 1
                    right = False
                    down = True
                    row += 1
                continue
            
            if down:
                results.append(matrix[row][col])
                matrix[row][col] = None
                if (row+1) < len(matrix):
                    row += 1
                else:
                    down = False
                    left = True
                    col -= 1
                    continue
                
                if matrix[row][col] is None:
                    row -= 1
                    down = False
                    left = True
                    col -= 1
                continue

            if left:
                results.append(matrix[row][col])
                matrix[row][col] = None
                if col > 0:
                    col -= 1
                else:
                    left = False
                    up = True
                    row -= 1
                    continue

                if matrix[row][col] is None:
                    col += 1
                    left = False
                    up = True
                    row -=1
                continue
            
            if up:
                results.append(matrix[row][col])
                matrix[row][col] = None
                if row > 0:
                    row -= 1
                else:
                    up = False
                    right = True
                    col += 1
                if matrix[row][col] is None:
                    row += 1
                    up = False
                    right = True
                    col += 1
                continue

        return results