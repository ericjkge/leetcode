# Last updated: 7/17/2025, 9:37:23 PM
class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = Counter(num)
        first_half = []
        center = ""

        for num in range(9, -1, -1):
            num_char = str(num)

            if num_char in counter:
                freq = counter[num_char]

                if freq // 2:
                    if not first_half and not num:
                        continue
                    else:
                        first_half.append(num_char * (freq // 2))

                if freq % 2 and not center:
                    center = num_char
        
        if not center and not first_half:
            return "0"

        return "".join(first_half + [center] + first_half[::-1])
                    
