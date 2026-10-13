class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapping = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        ans = []
        if not digits:
            return []
        def dfs(cur, index):

            if index == len(digits):
                ans.append(cur)
                return
            
            if mapping[digits[index]]:
                for i in mapping[digits[index]]:
                    dfs(cur+i, index + 1)
        
        dfs("", 0)
        return ans
