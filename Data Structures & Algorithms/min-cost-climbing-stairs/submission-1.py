class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        prevTwo, prev = cost[0], cost[1]

        for i in range(2, len(cost)):
            curr = min(prev, prevTwo) + cost[i]
            prev, prevTwo = curr, prev

        return min(prev, prevTwo)