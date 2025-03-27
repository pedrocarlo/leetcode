# 981. Time Based Key-Value Store


class TimeMap:
    def __init__(self):
        self.map: dict[str, list[tuple[str, int]]] = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        # Here we are assuming timestamp is always greater when set
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # use bisect or write binary search by hand
        values = self.map.get(key, [])
        if not values:
            return ""
        left = 0
        right = len(values) - 1
        res = ""

        # print(values)
        while left <= right:
            mid = left + (right - left) // 2
            # print(left, mid, right)
            if values[mid][1] <= timestamp:
                left = mid + 1
                res = values[mid][0]
            else:
                right = mid - 1

        return res


timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
res = timeMap.get("foo", 1)
print(res)
res = timeMap.get("foo", 3)
print(res)
timeMap.set("foo", "bar2", 4)
res = timeMap.get("foo", 4)
print(res)
res = timeMap.get("foo", 5)
print(res)
