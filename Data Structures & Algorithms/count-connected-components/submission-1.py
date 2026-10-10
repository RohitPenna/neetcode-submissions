from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        con = defaultdict(list)
        
        def bfs (val):

            queue = deque()

            queue.append(val)

            count = 0

            while queue:
                while queue:
                    x = queue.popleft()

                    for i in con[x]:
                        if i in con:
                            queue.append(i)
                    
                    del con[x]
                
                count += 1

                if con:
                    queue.append(next(iter(con)))
            return count

        for i in range(n):
            con[i] = []
        
        for i in edges:
            con[i[0]].append(i[1])
            con[i[1]].append(i[0])
        
        return bfs(0) + len(con)



