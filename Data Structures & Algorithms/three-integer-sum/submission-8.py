class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []

        num = sorted(nums)

        for i in range(len(num) - 2):

            if i > 0 and num[i] == num[i-1]:
                continue

            start = i + 1
            end = len(num) - 1

            while start < end:
                sums = num[start] + num[end] + num[i]
                if(sums == 0):
                    ret.append([ num[i], num[start], num[end]])
                    start += 1
                    end -= 1
                    while start < end and num[start] == num[start-1]: 
                        start += 1
                    while start < end and num[end] == num[end+1]: 
                        end -= 1
                elif (sums > 0):
                    end -= 1
                else:
                    start += 1
        
        return ret