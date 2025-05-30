# Last updated: 5/30/2025, 12:07:33 PM
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}
        
        for winner, loser in matches:
            losses[winner] = losses.get(winner, 0)
            losses[loser] = losses.get(loser,  0) + 1
        
        zero_losses = []
        one_loss = []
        
        for player, losses in losses.items():
            if losses == 0:
                zero_losses.append(player)
            elif losses == 1:
                one_loss.append(player)
                
        return [sorted(zero_losses), sorted(one_loss)]
        