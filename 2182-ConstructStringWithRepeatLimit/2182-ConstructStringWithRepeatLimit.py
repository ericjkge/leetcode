# Last updated: 7/10/2025, 12:11:04 AM
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)
        heap = [(-ord(letter), letter) for letter in counter]
        heapq.heapify(heap)
        ans = []

        while heap:
            _, letter1 = heapq.heappop(heap)
            use = min(repeatLimit, counter[letter1])

            ans.extend([letter1] * use)
            counter[letter1] -= use

            if counter[letter1] > 0:
                if not heap:
                    break

                _, letter2 = heapq.heappop(heap)
                ans.append(letter2)
                counter[letter2] -= 1

                if counter[letter2] > 0:
                    heapq.heappush(heap, (-ord(letter2), letter2))
                heapq.heappush(heap, (-ord(letter1), letter1))

        return "".join(ans)