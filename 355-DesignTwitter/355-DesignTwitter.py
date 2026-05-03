# Last updated: 5/3/2026, 11:26:10 AM
1class Twitter:
2
3    def __init__(self):
4        self.users = defaultdict(list) # [user1: [following]]
5        self.tweets = defaultdict(list)
6        self.time = 0
7
8    def postTweet(self, userId: int, tweetId: int) -> None:
9        self.tweets[userId].append((self.time, tweetId))
10        self.time -= 1
11
12    def getNewsFeed(self, userId: int) -> List[int]:
13        relevant = self.tweets[userId][-10:]
14        for followeeId in self.users[userId]:
15            relevant.extend(self.tweets[followeeId][-10:])
16
17        heapq.heapify(relevant)
18        feed = []
19        for _ in range(min(10, len(relevant))):
20            _, tweetId = heapq.heappop(relevant)            
21            feed.append(tweetId)
22
23        return feed
24
25    def follow(self, followerId: int, followeeId: int) -> None:
26        if followeeId in self.users[followerId]:
27            return
28            
29        self.users[followerId].append(followeeId)
30
31    def unfollow(self, followerId: int, followeeId: int) -> None:
32        if followeeId not in self.users[followerId]:
33            return 
34        
35        self.users[followerId].remove(followeeId)
36
37
38# Your Twitter object will be instantiated and called as such:
39# obj = Twitter()
40# obj.postTweet(userId,tweetId)
41# param_2 = obj.getNewsFeed(userId)
42# obj.follow(followerId,followeeId)
43# obj.unfollow(followerId,followeeId)