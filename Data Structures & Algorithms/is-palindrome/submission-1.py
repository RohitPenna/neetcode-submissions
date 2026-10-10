class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1

        while left < right:
            l = s[left]
            r = s[right]
            if not l.isdigit() and not l.isalpha():
                left += 1
                continue
            if not r.isdigit() and not r.isalpha():
                right -= 1
                continue
            
            if l.lower() != r.lower():
                return False

            left += 1
            right -= 1
        
        return True
