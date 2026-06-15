"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mp = {}

        for i in intervals:
            mp[i.start] = mp.get(i.start, 0) + 1
            mp[i.end] = mp.get(i.end, 0) - 1

        res, count = 0, 0 
        for time in sorted(mp.keys()):
            count += mp[time]
            res = max(res, count)
        return res

        