# Last updated: 7/9/2025, 10:18:31 PM
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        frequencies = Counter(words)
        for word, frequency in frequencies.items():
            heapq.heappush(heap, (-frequency, word))
        
        ans = []
        for _ in range(k):
            _, word = heapq.heappop(heap)
            ans.append(word)
        
        return ans