class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        unvisited = {}

        for p in points:
            unvisited[tuple(p)] = float('inf')

        x = tuple(points[0])
        unvisited[x] = 0

        tot = 0

        while unvisited:

            # Find the cheapest unvisited point
            point = min(unvisited, key=lambda x: unvisited[x])

            tot += unvisited[point]
            del unvisited[point]

            # Update costs of remaining points
            for p in unvisited:
                dist = abs(point[0] - p[0]) + abs(point[1] - p[1])

                if dist < unvisited[p]:
                    unvisited[p] = dist

        return tot