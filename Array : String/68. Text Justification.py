class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def justify_line(line_words, line_length, maxWidth, is_last_line):
            if is_last_line or len(line_words) == 1:
                # Left justify the last line or a line with a single word
                return ' '.join(line_words).ljust(maxWidth)
            else:
                # Calculate space distribution
                total_spaces = maxWidth - line_length
                num_gaps = len(line_words) - 1
                even_spaces = total_spaces // num_gaps
                extra_spaces = total_spaces % num_gaps
                
                line = ''
                for i in range(len(line_words) - 1):
                    line += line_words[i]
                    line += ' ' * (even_spaces + (1 if i < extra_spaces else 0))
                line += line_words[-1]  # add the last word without extra space
                return line
        
        result = []
        line_words = []
        line_length = 0
        
        for word in words:
            if line_length + len(word) + len(line_words) > maxWidth:
                # Justify the current line
                result.append(justify_line(line_words, line_length, maxWidth, False))
                # Reset the line
                line_words = []
                line_length = 0
            
            # Add the word to the current line
            line_words.append(word)
            line_length += len(word)
        
        # Justify the last line
        result.append(justify_line(line_words, line_length, maxWidth, True))
        
        return result

# Example usage:
solution = Solution()
print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(solution.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(solution.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))
