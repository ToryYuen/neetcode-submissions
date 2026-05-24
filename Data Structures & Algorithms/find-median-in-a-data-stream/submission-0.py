import heapq
class MedianFinder:

    def __init__(self):
        #max heap, min heap
        #small: same size as or one smaller than large
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush_max(self.small, heapq.heappushpop(self.large, num))
        else:
            heapq.heappush(self.large, heapq.heappushpop_max(self.small, num))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (self.small[0] + self.large[0]) / 2.0
        
        