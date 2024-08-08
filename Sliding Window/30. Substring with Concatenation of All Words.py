from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        word_count = Counter(words)
        result = []
        
        for i in range(word_len):
            left = i
            right = i
            seen_words = Counter()
            count = 0
            
            while right + word_len <= s_len:
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    seen_words[word] += 1
                    count += 1
                    
                    while seen_words[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen_words[left_word] -= 1
                        left += word_len
                        count -= 1
                        
                    if count == num_words:
                        result.append(left)
                else:
                    seen_words.clear()
                    count = 0
                    left = right
        
        return result

# Example usage
solution = Solution()
print(solution.findSubstring("barfoothefoobarman", ["foo", "bar"]))  # Output: [0, 9]
print(solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))  # Output: []
print(solution.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))  # Output: [6, 9, 12]
