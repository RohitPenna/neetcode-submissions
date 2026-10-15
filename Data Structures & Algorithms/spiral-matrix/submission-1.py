class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows = len(matrix)
        cols = len(matrix[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited = set()
        res = []

        row = 0
        col = 0
        d = 0

        for _ in range(rows * cols):
            res.append(matrix[row][col])
            visited.add((row, col))

            dr, dc = directions[d]
            new_row = row + dr
            new_col = col + dc

            if (new_row < 0 or new_row >= rows or
                new_col < 0 or new_col >= cols or
                (new_row, new_col) in visited):

                d = (d + 1) % 4
                dr, dc = directions[d]

            row += dr
            col += dc

        return res