class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Start from the end of the array
        for i in reversed(range(len(digits))):
            # If the current digit is less than 9, just increment and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the current digit is 9, set it to 0 and continue to the next digit
            digits[i] = 0
        
        # If all digits were 9, the result will be an array with a leading 1 followed by zeros
        return [1] + digits
