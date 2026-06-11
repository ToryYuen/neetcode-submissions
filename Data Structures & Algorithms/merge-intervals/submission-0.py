class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval:interval[0])

        res = []
        tmp = intervals[0]
        for i in range(1, len(intervals)):
            if tmp[1] < intervals[i][0]:
                res.append(tmp)
                tmp = intervals[i]
            elif intervals[i][1] < tmp[0]:
                res.append(intervals[i])
            else:
                tmp = [min(tmp[0], intervals[i][0]), max(tmp[1], intervals[i][1])]

        res.append(tmp)
        return res