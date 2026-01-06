# Last updated: 1/6/2026, 11:15:06 AM
1class Twitter:
2
3    def __init__(self):
4        self.users = defaultdict(lambda: defaultdict(list)) # user_id: {"following":[], "posts":[(time, tweet_id)]}
5        self.time = 1
6
7    def postTweet(self, userId: int, tweetId: int) -> None:
8        self.users[userId]["posts"].append((self.time, tweetId))
9        self.time += 1
10
11    def getNewsFeed(self, userId: int) -> List[int]:
12        following = self.users[userId]["following"]
13        posts = self.users[userId]["posts"][-10:]
14        
15        for account in following:
16            posts.extend(self.users[account]["posts"][-10:])
17        posts.sort(reverse=True)
18        posts = posts[:10]
19
20        return [post[1] for post in posts]
21
22    def follow(self, followerId: int, followeeId: int) -> None:
23        if followeeId in self.users[followerId]["following"]:
24            return
25            
26        self.users[followerId]["following"].append(followeeId)
27
28    def unfollow(self, followerId: int, followeeId: int) -> None:
29        if followerId not in self.users or followeeId not in self.users[followerId]["following"]:
30            return
31
32        self.users[followerId]["following"].remove(followeeId)
33
34
35# Your Twitter object will be instantiated and called as such:
36# obj = Twitter()
37# obj.postTweet(userId,tweetId)
38# param_2 = obj.getNewsFeed(userId)
39# obj.follow(followerId,followeeId)
40# obj.unfollow(followerId,followeeId)