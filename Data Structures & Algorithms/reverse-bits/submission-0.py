class Solution:
    def reverseBits(self, n: int) -> int:
        i, num = 31, 0
        while n:
            if n & 1:
                num += (2 ** i)
            n >>= 1
            i -= 1
        return num
            

        