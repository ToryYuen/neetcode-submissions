class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        minHeap, counts = [], {}
        for h in hand:
            counts[h] = counts.get(h, 0) + 1
            if counts[h] == 1:
                minHeap.append(h)
        heapq.heapify(minHeap)

        while minHeap:
            num = minHeap[0]

            for i in range(num, num + groupSize):
                if i not in counts:
                    return False
                counts[i] -= 1
                if counts[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
