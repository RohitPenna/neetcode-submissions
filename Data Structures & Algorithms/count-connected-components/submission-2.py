from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        con = defaultdict(list)

        for a, b in edges:
            con[a].append(b)
            con[b].append(a)

        visited = set()
        count = 0

        for i in range(n):

            if i in visited:
                continue

            count += 1
            queue = deque([i])
            visited.add(i)

            while queue:
                x = queue.popleft()

                for j in con[x]:
                    if j not in visited:
                        visited.add(j)
                        queue.append(j)

        return count