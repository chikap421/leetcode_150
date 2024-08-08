from collections import deque

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        if endGene not in bank:
            return -1
        
        # Initialize BFS
        queue = deque([(startGene, 0)])
        visited = set()
        visited.add(startGene)
        gene_length = len(startGene)
        valid_genes = set(bank)
        
        while queue:
            current_gene, mutations = queue.popleft()
            
            # Generate all possible mutations
            for i in range(gene_length):
                for char in 'ACGT':
                    if current_gene[i] == char:
                        continue
                    mutated_gene = current_gene[:i] + char + current_gene[i + 1:]
                    
                    if mutated_gene == endGene:
                        return mutations + 1
                    
                    if mutated_gene in valid_genes and mutated_gene not in visited:
                        visited.add(mutated_gene)
                        queue.append((mutated_gene, mutations + 1))
        
        return -1

# Example usage:
startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]

solution = Solution()
print(solution.minMutation(startGene, endGene, bank))  # Output: 2
