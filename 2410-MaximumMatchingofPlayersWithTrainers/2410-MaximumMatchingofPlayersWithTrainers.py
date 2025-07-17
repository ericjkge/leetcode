# Last updated: 7/17/2025, 4:59:27 PM
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        counter = 0
        players.sort()
        trainers.sort()
        while players and trainers:
            if players[0] <= trainers[0]:
                counter += 1
                players.pop(0)
                trainers.pop(0)
            else:
                trainers.pop(0)
        return counter