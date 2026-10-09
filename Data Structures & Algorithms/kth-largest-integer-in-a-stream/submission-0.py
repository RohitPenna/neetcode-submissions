import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.x = nums
        heapq.heapify(self.x)
        
        # Keep only the k largest elements in the heap
        while len(self.x) > k:
            heapq.heappop(self.x)

    def add(self, val: int) -> int:
        heapq.heappush(self.x, val)
        
        # If we exceeded k elements, remove the smallest
        if len(self.x) > self.k:
            heapq.heappop(self.x)
            
        # The root of a min-heap of size k is the kth largest element
        return self.x[0]