# Last updated: 12/27/2025, 10:50:51 PM
1class TrieNode:
2    def __init__(self, character, is_end):
3        self.character = character
4        self.is_end = is_end
5        self.children = {}
6
7class Trie:
8
9    def __init__(self):
10        self.root = TrieNode("", False)
11
12    def insert(self, word: str) -> None:
13        curr = self.root
14        for c in word:
15            if c not in curr.children:
16                node = TrieNode(c, False)
17                curr.children[c] = node
18            curr = curr.children[c]
19        curr.is_end = True
20
21    def search(self, word: str) -> bool:
22        curr = self.root
23        for c in word:
24            if c not in curr.children:
25                return False
26            curr = curr.children[c]
27        return curr.is_end
28
29    def startsWith(self, prefix: str) -> bool:
30        curr = self.root
31        for c in prefix:
32            if c not in curr.children:
33                return False
34            curr = curr.children[c]
35        return True
36
37
38# Your Trie object will be instantiated and called as such:
39# obj = Trie()
40# obj.insert(word)
41# param_2 = obj.search(word)
42# param_3 = obj.startsWith(prefix)