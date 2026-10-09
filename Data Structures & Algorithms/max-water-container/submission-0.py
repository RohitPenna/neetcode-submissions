class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeight = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            sums = min(heights[l], heights[r]) * (r - l)
            maxHeight = max(sums, maxHeight)

            if(heights[l] > heights[r]):
                r -= 1
            else:
                l += 1

        return maxHeight