# Last updated: 7/17/2025, 5:01:50 PM
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        counter = 0
        p1 = p2 = 0
        players.sort()
        trainers.sort()
        while p1 < len(players) and p2 < len(trainers):
            if players[p1] <= trainers[p2]:
                counter += 1
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return counter