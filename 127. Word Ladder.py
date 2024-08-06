from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)  # To quickly check if a word is in wordList
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])  # Queue for BFS: (current word, transformation steps)
        visited = set([beginWord])  # Set to keep track of visited words
        
        while queue:
            current_word, steps = queue.popleft()
            
            if current_word == endWord:
                return steps
            
            # Try all possible one-letter transformations
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == current_word[i]:
                        continue
                    next_word = current_word[:i] + c + current_word[i+1:]
                    
                    if next_word in wordSet and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, steps + 1))
        
        return 0

# Example usage:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

solution = Solution()
print(solution.ladderLength(beginWord, endWord, wordList))  # Output: 5
