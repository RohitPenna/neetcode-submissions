from collections import defaultdict, deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        con = defaultdict(set)

        def bfs(start, target):

            queue = deque([start])
            visited = {start}

            while queue:
                x = queue.popleft()

                if x == target:
                    return True

                for i in con[x]:
                    if i not in visited:
                        visited.add(i)
                        queue.append(i)

            return False

        for a, b in edges:

            if bfs(a, b):
                return [a, b]

            con[a].add(b)
            con[b].add(a)