# Last updated: 7/21/2025, 3:15:04 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]
        for _ in range(numRows - 1):
            prev = dp[-1]
            nextRow = [1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1]
            dp.append(nextRow)
        
        return dp
