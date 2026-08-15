class Twitter:

    def __init__(self):
        self.tweet=[]
        self.followerId=defaultdict(set)
        self.t=0

    def postTweet(self, userId: int, tweetId: int) -> None:
            self.t+=1
            heapq.heappush(self.tweet,[self.t,userId,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        for time,user,tweet in reversed(self.tweet):
            if userId==user or user in self.followerId[userId]:
                res.append(tweet)
                if len(res)==10:
                    break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerId[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followerId[followerId].discard(followeeId)
