# Last updated: 11/22/2025, 2:01:59 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        n = len(digits)

        if digits[n - 1] + 1 > 9:
            carry = 1
            digits[n - 1] = 0
        else:
            digits[n - 1] += 1

        if carry:
            for i in range(n - 2, -1, -1):
                if digits[i] + carry > 9:
                    carry = 1
                    digits[i] = 0
                else:
                    carry = 0
                    digits[i] += 1
                    break
        
        if carry:
            digits.insert(0, 1)
        
        return digits
            

            