# Last updated: 5/30/2025, 12:07:34 PM
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        tracker = {}
        
        for char in text:
            tracker[char] = tracker.get(char, 0) + 1
        
        return min(tracker.get("b", 0), tracker.get("a", 0), tracker.get("l", 0) // 2, tracker.get("o", 0) // 2, tracker.get("n", 0))
    