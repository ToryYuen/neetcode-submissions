class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                res = max(res, (i - idx) * height)
                start = idx
            stack.append((start , h))

        length = len(heights)
        for i, h in stack:
            res = max(res, (length - i) * h)

        return res