class TimeMap:

    def __init__(self):
        self.d: dict[str:list[tuple[int:str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        val:list[tuple[int:str]] = self.d.get(key, [])
        val.append((timestamp, value))
        self.d[key] = val

    def get(self, key: str, timestamp: int) -> str:
        val:list[tuple[int:str]] = self.d.get(key, [])

        res = ""
        l, r = 0, len(val) - 1
        while l <= r:
            m = (l + r) // 2
            if val[m][0] == timestamp:
                return val[m][1]
            elif val[m][0] > timestamp:
                r = m - 1
            else:
                res = val[m][1]
                l = m + 1
        return res
        
