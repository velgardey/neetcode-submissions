class TimeMap:

    def __init__(self):
        self.keyStore = {} # keyStore : "key" : [[val1, timestamp1], [val2, timestamp2], ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key, []) # Returns the list of value, timestamp and defaults to []

        # Binary Search to find the timestamp
        l, r = 0, len(values) - 1

        while l <= r :
            mid = l + (r - l) // 2

            if timestamp >= values[mid][1] :
                res = values[mid][0] # Store the value or the closest value by timestamp which is less than the req timestamp
                l = mid + 1
            else :
                r = mid - 1
        return res

