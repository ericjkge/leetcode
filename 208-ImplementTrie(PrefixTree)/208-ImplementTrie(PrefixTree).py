# Last updated: 2/6/2026, 10:06:19 AM
1class TrieNode:
2    def __init__(self):
3        self.children = {}
4        self.is_end = False
5
6class Trie:
7
8    def __init__(self):
9        self.root = TrieNode()
10
11    def insert(self, word: str) -> None:
12        node = self.root
13        for c in word:
14            if c not in node.children:
15                node.children[c] = TrieNode()
16            node = node.children[c]
17        node.is_end = True
18
19    def search(self, word: str) -> bool:
20        node = self.root
21        for c in word:
22            if c not in node.children:
23                return False
24            node = node.children[c]
25        return node.is_end
26
27    def startsWith(self, prefix: str) -> bool:
28        node = self.root
29        for c in prefix:
30            if c not in node.children:
31                return False
32            node = node.children[c]
33        return True
34
35# Your Trie object will be instantiated and called as such:
36# obj = Trie()
37# obj.insert(word)
38# param_2 = obj.search(word)
39# param_3 = obj.startsWith(prefix)