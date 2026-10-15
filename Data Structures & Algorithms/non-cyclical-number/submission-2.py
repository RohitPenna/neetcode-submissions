class Solution:
    def isHappy(self, n: int) -> bool:
        

        def loop(num, contains):

            if num == 1:
                return True
            
            s = 0
            
            while num != 0:
                i = num % 10

                i = i * i
                s += i

                num = num // 10
            
            if s in contains:
                return False
            else:
                contains.add(s)
                return loop(s, contains)
            
        return loop(n, set())