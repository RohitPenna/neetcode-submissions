class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            # Calculate the middle index of the current range
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                # Target is in the right half, move low pointer
                low = mid + 1
            else:
                # Target is in the left half, move high pointer
                high = mid - 1
                
        return -1