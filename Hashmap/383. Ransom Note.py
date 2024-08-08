from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Count the frequency of each letter in ransomNote and magazine
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        # Check if magazine has enough of each letter to construct ransomNote
        for letter, count in ransom_count.items():
            if magazine_count[letter] < count:
                return False
        return True
