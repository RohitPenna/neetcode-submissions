class TimeMap:

    def __init__(self):
        self.maps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.maps[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        right = len(self.maps[key]) - 1
        left = 0

        if not self.maps[key] or self.maps[key][0][1] > timestamp:
            return ""

        while left < right:
            mid = (left+right + 1) // 2

            if self.maps[key][mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid
        
        return self.maps[key][right][0]