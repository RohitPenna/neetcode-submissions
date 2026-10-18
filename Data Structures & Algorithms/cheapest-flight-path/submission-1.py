class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        distance = {i: float('inf') for i in range(n)}
        distance[src] = 0

        for _ in range(k + 1):

            temp = distance.copy()

            for a, b, weight in flights:
                if distance[a] == float('inf'):
                    continue

                new_cost = distance[a] + weight

                if new_cost < temp[b]:
                    temp[b] = new_cost


            distance = temp


        return distance[dst] if distance[dst] != float('inf') else -1