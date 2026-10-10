from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        maps = defaultdict(set)
        ind = [0] * numCourses

        if len(prerequisites) == 0:
            return True

        for i in prerequisites:
            maps[i[1]].add(i[0])
            ind[i[0]] += 1
        
        queue = deque()
        for i in range(len(ind)):
            if ind[i] == 0:
                queue.append(i)
        
        if not queue:
            return False
        
        taken = 0

        while queue:
            x = queue.popleft()
            taken += 1

            for i in maps[x]:
                ind[i] -= 1
                if ind[i] == 0:
                    queue.append(i)
        
        return taken == numCourses



