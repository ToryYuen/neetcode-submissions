class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            n = digits[i] + carry
            if n >= 10:
                res.append(n - 10)
                carry = 1 
            else:
                res.append(n)
                carry = 0
        
        if carry == 1:
            res.append(1)
        return res[::-1]