class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId : [count, tweetId]
        self.followMap = defaultdict(set) # userId : set(userIds)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush_max(maxHeap, [count, tweetId, followeeId, index - 1])

        while maxHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop_max(maxHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush_max(maxHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
