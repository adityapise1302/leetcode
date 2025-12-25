class TimeMap:

    def __init__(self):
        self.key_store = dict() # Dictionary: key: list of (value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_store.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        list_val_ts = self.key_store.get(key, [])
        l, r = 0, len(list_val_ts) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if list_val_ts[mid][1] <= timestamp:
                res = list_val_ts[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)