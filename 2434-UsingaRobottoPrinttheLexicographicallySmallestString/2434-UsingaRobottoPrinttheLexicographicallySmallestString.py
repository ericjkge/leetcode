# Last updated: 7/6/2025, 9:57:03 PM
class Solution:
    def robotWithString(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        result = []
        minChar = "a"

        for char in s:
            stack.append(char)
            counter[char] -= 1
            while minChar != "z" and counter[minChar] == 0:
                minChar = chr(ord(minChar) + 1)
            while stack and stack[-1] <= minChar:
                result.append(stack.pop())
            
        return "".join(result)


        while stack1:
            stack2.append(stack1.pop())

        return "".join(stack2)            
