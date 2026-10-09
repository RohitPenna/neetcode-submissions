import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-x for x in nums]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        
        heapq.heappush(self.nums, -val)

        temp = []
        for i in range(self.k):
            temp.append(heapq.heappop(self.nums))
        
        print(temp)
        x = -temp[-1]

        for i in temp:
            heapq.heappush(self.nums, i)
        
        return x
