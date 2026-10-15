from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.matrix = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.matrix[tuple(point)] += 1

    def count(self, point: List[int]) -> int:

        count = 0
        x, y = point

        for (px, py) in self.matrix:

            # Must share x-coordinate, but have different y
            if px == x and py != y:

                # Side length
                side = abs(py - y)

                # Check square to the right
                count += (
                    self.matrix[(px, py)]
                    * self.matrix.get((x + side, y), 0)
                    * self.matrix.get((x + side, py), 0)
                )

                # Check square to the left
                count += (
                    self.matrix[(px, py)]
                    * self.matrix.get((x - side, y), 0)
                    * self.matrix.get((x - side, py), 0)
                )

        return count