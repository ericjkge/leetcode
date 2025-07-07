# Last updated: 7/6/2025, 10:17:35 PM
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        counter = 0

        for p in pushed:
            if p != popped[counter]:
                stack.append(p)
            else:
                counter += 1
                while stack and stack[-1] == popped[counter]:
                    stack.pop()
                    counter += 1

        return not stack