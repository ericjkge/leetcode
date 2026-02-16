# Last updated: 2/16/2026, 1:07:14 PM
1class Twitter:
2
3    def __init__(self):
4        self.tweets = defaultdict(list) # userId: [(t1, tweet1), (t2, tweet2), ...]
5        self.following = defaultdict(list)
6        self.followers = defaultdict(list)
7        self.time = 0
8        
9    def postTweet(self, userId: int, tweetId: int) -> None:
10        self.time += 1
11        self.tweets[userId].append((self.time, tweetId))
12
13    def getNewsFeed(self, userId: int) -> List[int]:
14        relevant_tweets = []
15        for user, lst in self.tweets.items():
16            if user in self.following[userId] or user == userId:
17                relevant_tweets.extend(lst[-10:])
18
19        relevant_tweets.sort(reverse=True)
20        feed = []
21        for k, v in relevant_tweets:
22            feed.append(v)
23        return feed[:10]
24
25    def follow(self, followerId: int, followeeId: int) -> None:
26        if followerId == followeeId:
27            return
28
29        self.following[followerId].append(followeeId)
30        self.followers[followeeId].append(followerId)
31
32    def unfollow(self, followerId: int, followeeId: int) -> None:
33        if followeeId not in self.following[followerId]:
34            return
35
36        self.following[followerId].remove(followeeId)
37        self.followers[followeeId].remove(followerId)
38
39
40# Your Twitter object will be instantiated and called as such:
41# obj = Twitter()
42# obj.postTweet(userId,tweetId)
43# param_2 = obj.getNewsFeed(userId)
44# obj.follow(followerId,followeeId)
45# obj.unfollow(followerId,followeeId)