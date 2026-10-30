# Last updated: 10/30/2026, 10:48:08 AM
1class Solution:
2    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
3        count = 0
4
5        for i in range(len(flowerbed)):
6            if flowerbed[i] == 0:
7                if (i - 1 >= 0 and flowerbed[i - 1] == 1) or (i + 1 < len(flowerbed) and flowerbed[i + 1] == 1):
8                    continue
9                count += 1
10                flowerbed[i] = 1
11        
12        return count >= n
13