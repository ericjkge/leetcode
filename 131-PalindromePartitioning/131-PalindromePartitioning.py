# Last updated: 12/17/2025, 8:48:16 PM
1class Solution:
2    def partition(self, s: str) -> List[List[str]]:
3        n = len(s)
4        ans = []
5
6        def backtrack(index, path):
7            if index == n:
8                ans.append(path[:])
9                return
10
11            for i in range(index, n):
12                if s[index:i + 1] == s[index:i + 1][::-1]:
13                    path.append(s[index:i + 1])
14                    backtrack(i + 1, path)
15                    path.pop()
16        
17        backtrack(0, [])
18        return ans
19
20
21
22
23
24
25
26
27
28        # ans = []
29        # n = len(s)
30
31        # def isPalindrome(string):
32        #     return string == string[::-1]
33
34        # def backtrack(start, path):
35        #     if start == n:
36        #         ans.append(path[:])
37        #         return
38            
39        #     for i in range(start, n):
40        #         if isPalindrome(s[start:i + 1]):
41        #             path.append(s[start:i + 1])
42        #             backtrack(i + 1, path)
43        #             path.pop()
44            
45        # backtrack(0, [])
46        # return ans