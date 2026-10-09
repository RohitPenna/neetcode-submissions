import heapq

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
            
            for u in self.tweets[i]:

                heapq.heappush(heap, u)

                if len(heap) > 10:
                    heapq.heappop(heap)

        ans = []        
        while heap:
            x = heapq.heappop(heap)
            ans.append(x[1])

        return ans[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        print(followerId)
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId) 
        
