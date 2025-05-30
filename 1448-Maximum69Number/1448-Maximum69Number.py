# Last updated: 5/30/2025, 12:07:29 PM
class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = [int(digit) for digit in str(num)]
        for i in range(len(digits)):
            if digits[i] == 6:
                digits[i] = 9
                return int("".join(map(str, digits)))
        return num