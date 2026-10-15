class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        

        left = 0
        mid = 0
        right = 0
        
        for i in range(len(triplets)):

            x, y, z = triplets[i]

            if x > target[0] or y > target[1] or z > target[2]:
                continue
            
            left = max(left, x)
            mid = max(mid, y)
            right = max(right, z)
        
        return left == target[0] and mid == target[1] and right == target[2]