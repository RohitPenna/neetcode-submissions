class TimeMap:

    def __init__(self):
        self.maps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.maps[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.maps[key]) - 1
        ans = ""

        while left <= right:
            mid = (left + right) // 2

            if self.maps[key][mid][1] <= timestamp:
                ans = self.maps[key][mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return ans