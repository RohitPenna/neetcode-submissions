class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = 0
        lr = len(matrix[0]) - 1

        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][lr] >= target:
                row = i
        
        left = 0
        right = lr
        print(matrix[row])

        while left <= right:

            mid = (left+right)//2

            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return False