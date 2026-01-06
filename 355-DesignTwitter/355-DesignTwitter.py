# Last updated: 1/6/2026, 11:21:13 AM
1class Twitter:
2
3    def __init__(self):
4        self.following = defaultdict(set)
5        self.tweets = defaultdict(list)
6        self.time = 1
7
8    def postTweet(self, userId: int, tweetId: int) -> None:
9        self.tweets[userId].append((self.time, tweetId))
10        self.time += 1
11
12    def getNewsFeed(self, userId: int) -> List[int]:
13        following = self.following[userId]
14        following.add(userId)
15
16        posts = []
17        
18        for account in following:
19            posts.extend(self.tweets[account][-10:])
20        posts.sort(reverse=True)
21        posts = posts[:10]
22
23        return [post[1] for post in posts]
24
25    def follow(self, followerId: int, followeeId: int) -> None:
26        self.following[followerId].add(followeeId)
27
28    def unfollow(self, followerId: int, followeeId: int) -> None:
29        if followerId not in self.following or followeeId not in self.following[followerId]:
30            return
31
32        self.following[followerId].remove(followeeId)
33
34
35# Your Twitter object will be instantiated and called as such:
36# obj = Twitter()
37# obj.postTweet(userId,tweetId)
38# param_2 = obj.getNewsFeed(userId)
39# obj.follow(followerId,followeeId)
40# obj.unfollow(followerId,followeeId)