# Last updated: 7/17/2026, 12:51:24 AM
1class Solution:
2    def compress(self, chars: List[str]) -> int:
3        read = write = 0
4
5        while read < len(chars):
6            ch = chars[read]
7            start = read
8            while read < len(chars) and chars[read] == ch:
9                 read += 1
10
11            chars[write] = ch
12            write += 1
13            count = read - start
14            if count > 1:
15                for d in str(count):
16                    chars[write] = d
17                    write += 1
18        
19        return write
20