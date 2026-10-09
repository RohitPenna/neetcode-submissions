class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = len(s) - 1
        y = 0
        while x > y:
            while x > y and not (s[x].isalpha() or s[x].isdigit()):
                x -= 1
            while x > y and not (s[y].isalpha() or s[y].isdigit()):
                y += 1

            if(s[y].lower() != s[x].lower()):
                return False
            x -=1
            y += 1

        return True