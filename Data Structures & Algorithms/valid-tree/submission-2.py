from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        maps = defaultdict(set)

        if len(edges) == 0:
            return True

        for i in edges:
            maps[i[0]].add(i[1])
            maps[i[1]].add(i[0])

        queue = deque()
        queue.append(0)
        
        visited = {0:-1}
        while queue:
            x = queue.popleft()

            for i in maps[x]:
                if i not in visited:
                    visited[i] = x
                    queue.append(i)
                elif visited[x] != i:
                    return False
        
        return len(visited) == n


