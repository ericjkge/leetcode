# Last updated: 7/16/2026, 10:46:43 PM
1class Solution:
2    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
3        for i in range(len(flowerbed)):
4            if (i == 0 or flowerbed[i - 1] == 0) and flowerbed[i] == 0 and (i + 1 == len(flowerbed) or flowerbed[i + 1] == 0):
5                flowerbed[i] = 1
6                n -= 1
7            
8        return n <= 0