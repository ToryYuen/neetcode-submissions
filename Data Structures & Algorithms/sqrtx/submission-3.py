class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x - 1
        while l <= r:
            m = (l + r) // 2
            square = m * m
            if square == x:
                return m
            elif square > x:
                r = m - 1
            else:
                l = m + 1
        return l - 1 if l > 1 else l