import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for i in times:
            a, b ,c = i
            graph[a].append((b, c))
        
        distance = {}

        distance = {i: float('inf') for i in range(1, n + 1)}
        
        heap = [(0, k)]
        distance[k] = 0

        while heap:
            cost, x = heapq.heappop(heap)

            if cost > distance[x]:
                continue
            
            for node, weight in graph[x]:
                new_cost = cost + weight

                if new_cost < distance[node]:
                    distance[node] = new_cost
                    heapq.heappush(heap, (new_cost, node))
        
        return max(distance.values()) if max(distance.values()) != float('inf') else -1
        