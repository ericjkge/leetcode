# Last updated: 7/7/2025, 2:56:47 PM
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(arr)

        # PLE (previous less element)
        ple = [0] * n
        stack = []
        for i in range(n):
            counter = 1
            while stack and stack[-1][0] > arr[i]:
                counter += stack.pop()[1]
            ple[i] = counter
            stack.append((arr[i], counter))
        
        # NLE (next less element)
        nle = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            counter = 1
            while stack and stack[-1][0] >= arr[i]:
                counter += stack.pop()[1]
            nle[i] = counter
            stack.append((arr[i], counter))
        
        ans = 0
        for i in range(n):
            ans = (ans + arr[i] * ple[i] * nle[i]) % MOD
        return ans
        
                