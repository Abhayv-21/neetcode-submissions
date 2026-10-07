import heapq
class Twitter:

    def __init__(self):
        self.tweets = {}
        self.time = 0
        self.follower = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        result = []

        people = set(self.follower.get(userId, set()))
        people.add(userId)

        for person in people:
            if person in self.tweets:
                time, tweetid = self.tweets[person][-1]
                index = len(self.tweets[person]) - 1 
                heapq.heappush(heap, (-time, tweetid, person, index))

        while heap and len(result) < 10:
            neg_time, tweetid, person, index = heapq.heappop(heap)
            result.append(tweetid)
            index = index - 1
            if index >= 0:
                time, tweet = self.tweets[person][index]
                heapq.heappush(heap, (-time, tweet, person, index))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follower:
            self.follower[followerId] = set()
        self.follower[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follower:
            return
        self.follower[followerId].discard(followeeId) 