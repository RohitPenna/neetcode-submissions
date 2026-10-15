class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        start = 0
        gl = 0
        total = 0

        for i in range(len(gas)):
            dif = gas[i] - cost[i]

            gl += dif
            total += dif

            if gl < 0:
                start = i + 1
                gl = 0

        if total < 0:
            return -1

        return start