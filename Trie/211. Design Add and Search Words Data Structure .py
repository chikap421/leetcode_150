class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self._search(word, 0, self.root)
    
    def _search(self, word, index, node):
        if index == len(word):
            return node.isEndOfWord
        
        char = word[index]
        if char == '.':
            for child in node.children.values():
                if self._search(word, index + 1, child):
                    return True
        else:
            if char in node.children:
                return self._search(word, index + 1, node.children[char])
        
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
