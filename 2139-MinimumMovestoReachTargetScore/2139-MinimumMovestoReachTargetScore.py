# Last updated: 7/17/2025, 10:29:26 PM
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        counter = 0

        while target > 1:
            if not target % 2 and maxDoubles:
                target /= 2
                maxDoubles -= 1
                counter += 1
            elif maxDoubles:
                target -= 1
                counter += 1
            else:
                target -= 1
                counter += int(target)
                break

        return counter