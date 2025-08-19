# Last updated: 8/19/2025, 9:27:39 PM
# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         def countDigits(str):
#             zeros = str.count("0")
#             ones = len(str) - zeros
#             return (zeros, ones)

#         @cache
#         def dp(i, j, index):
#             if index == len(strs):
#                 return 0

#             zeros, ones = countDigits(strs[index])

#             skip = dp(i, j, index + 1)

#             take = 0
#             if i >= zeros and j >= ones:
#                 take = 1 + dp(i - zeros, j - ones, index + 1)
            
#             return max(skip, take)
            
#         return dp(m, n, 0)




class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count(str):
            zeros = str.count("0")
            ones = len(str) - zeros
            return zeros, ones

        @cache
        def dp(i, j, index):
            if i < 0 or j < 0:
                return -1
            if index == len(strs):
                return 0
            
            zeros, ones = count(strs[index])

            skip = dp(i, j, index + 1)
            take = 1 + dp(i - zeros, j - ones, index + 1)
            return max(skip, take)

        return dp(m, n, 0)