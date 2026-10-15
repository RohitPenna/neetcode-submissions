from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        x = dict(sorted(Counter(hand).items()))

        if len(hand) % groupSize != 0:
            return False
        
        while x:
            val = next(iter(x))

            x[val] -= 1

            if x[val] <= 0:
                del x[val]

            for i in range(val +1, val + groupSize):

                if i not in x:
                    return False
                    
                x[i] -= 1

                if x[i] <= 0:
                    del x[i]
            
        return True