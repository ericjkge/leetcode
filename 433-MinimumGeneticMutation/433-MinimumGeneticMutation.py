# Last updated: 5/30/2025, 12:07:52 PM
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        length = len(startGene)
        
        def neighbors(gene):
            neighbors = []
            for i in range(length):
                for change in ["A", "C", "G", "T"]:
                    if gene[i] != change:
                        mutation = gene[:i] + change + gene[i+1:]
                        neighbors.append(mutation)
            return neighbors

        queue = deque([(startGene, 0)])
        seen = {startGene}
        
        while queue:
            node, moves = queue.popleft()
            if node == endGene:
                return moves
            mutations = neighbors(node)
            for mutation in mutations:
                if mutation in bank and mutation not in seen:
                    seen.add(mutation)
                    queue.append((mutation, moves + 1))
        return -1
        
        
        
            
        