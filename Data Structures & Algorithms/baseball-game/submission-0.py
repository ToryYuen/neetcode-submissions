class Solution:
    def calPoints(self, operations: List[str]) -> int:
        h = []
        for ope in operations:
            if ope == '+':
                h.append(h[-1] + h[-2])
            elif ope == 'C':
                if h:
                    h.pop()
            elif ope == 'D':
                h.append(int(h[-1] * 2))
            else:
                h.append(int(ope))

        return sum(h)