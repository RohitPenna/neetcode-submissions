
import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        users = self.following[userId].copy()
        users.add(userId)

        for i in users:
            if self.tweets[i]:
                index = len(self.tweets[i]) - 1
                count, tweetId = self.tweets[i][index]

                heapq.heappush(heap, (-count, tweetId, i, index))

        ans = []

        while heap and len(ans) < 10:
            count, tweetId, user, index = heapq.heappop(heap)
            ans.append(tweetId)

            if index > 0:
                index -= 1
                count, tweetId = self.tweets[user][index]

                heapq.heappush(heap, (-count, tweetId, user, index))

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
