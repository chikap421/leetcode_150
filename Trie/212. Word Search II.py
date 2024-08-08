class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        self.word = None  # Storing the word at the end of the Trie path

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True
        node.word = word  # Store the complete word at the end node

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Step 1: Build the Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        self.result = set()
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

        # Step 2: Perform DFS from each cell
        for row in range(self.rows):
            for col in range(self.cols):
                self._dfs(row, col, trie.root)

        return list(self.result)

    def _dfs(self, row, col, node):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return

        char = self.board[row][col]
        if char == '#' or char not in node.children:
            return

        next_node = node.children[char]
        if next_node.isEndOfWord:
            self.result.add(next_node.word)

        # Mark the current cell as visited
        self.board[row][col] = '#'
        
        # Explore neighbors
        for d_row, d_col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            self._dfs(row + d_row, col + d_col, next_node)
        
        # Restore the current cell
        self.board[row][col] = char
