class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        maps = defaultdict(set)
        ind = [0] * numCourses

        if len(prerequisites) == 0:
            res = []
            for i in range(numCourses):
                res.append(i)
            return res

        for i in prerequisites:
            maps[i[1]].add(i[0])
            ind[i[0]] += 1
        
        queue = deque()
        for i in range(len(ind)):
            if ind[i] == 0:
                queue.append(i)
        
        if not queue:
            return []
        
        taken = 0
        ans = []

        while queue:
            x = queue.popleft()
            taken += 1
            ans.append(x)

            if taken == numCourses:
                return ans

            for i in maps[x]:
                ind[i] -= 1
                if ind[i] == 0:
                    queue.append(i)
        
        if taken == numCourses:
            return ans
        else:
            return []