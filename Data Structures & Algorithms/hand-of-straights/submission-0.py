class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand) % groupSize) != 0:
            return False

        minHeap, counts = [], {}
        for h in hand:
            counts[h] = counts.get(h, 0) + 1
            if counts[h] == 1:
                heapq.heappush(minHeap, h)

        for i in range(len(hand) // groupSize):
            num = minHeap[0]
            for j in range(groupSize):
                if num not in counts:
                    return False
                else:
                    cnt = counts[num] - 1
                    if cnt == 0:
                        del counts[num]
                        heapq.heappop(minHeap)
                    else:
                        counts[num] = cnt
                    num += 1
        return True
