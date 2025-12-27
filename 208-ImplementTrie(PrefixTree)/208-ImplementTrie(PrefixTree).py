# Last updated: 12/27/2025, 10:52:01 PM
1class TrieNode:
2    def __init__(self):
3        self.is_end = False
4        self.children = {}
5
6class Trie:
7
8    def __init__(self):
9        self.root = TrieNode()
10
11    def insert(self, word: str) -> None:
12        curr = self.root
13        for c in word:
14            if c not in curr.children:
15                curr.children[c] = TrieNode()
16            curr = curr.children[c]
17        curr.is_end = True
18
19    def search(self, word: str) -> bool:
20        curr = self.root
21        for c in word:
22            if c not in curr.children:
23                return False
24            curr = curr.children[c]
25        return curr.is_end
26
27    def startsWith(self, prefix: str) -> bool:
28        curr = self.root
29        for c in prefix:
30            if c not in curr.children:
31                return False
32            curr = curr.children[c]
33        return True
34
35
36# Your Trie object will be instantiated and called as such:
37# obj = Trie()
38# obj.insert(word)
39# param_2 = obj.search(word)
40# param_3 = obj.startsWith(prefix)