from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)

        heap = []

        for i in freq:
            heapq.heappush(heap, -freq[i])

        counter = 0

        while heap:
            temp = []
            completed = 0

            for i in range(n + 1):
                if heap:
                    x = -heapq.heappop(heap)
                    x -= 1

                    completed += 1

                    if x > 0:
                        temp.append(-x)

            for x in temp:
                heapq.heappush(heap, x)

            if heap:
                counter += n + 1
            else:
                counter += completed

        return counter