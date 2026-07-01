class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = [(temperatures[0], 0)]

        for i in range(1, len(temperatures)):
            temp = temperatures[i]

            while s and s[-1][0] < temp:
                _, prev_idx = s.pop()
                res[prev_idx] = i - prev_idx
            
            s.append((temp, i))
        return res

        