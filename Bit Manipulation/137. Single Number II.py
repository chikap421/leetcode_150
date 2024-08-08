class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize counters for bits that appear once and twice
        ones, twos = 0, 0
        
        for num in nums:
            # Update twos with the bits that are already in ones and appear again
            twos |= ones & num
            
            # Update ones with the new bits from num
            ones ^= num
            
            # Get the bits that have appeared three times
            threes = ones & twos
            
            # Remove the bits that have appeared three times from ones and twos
            ones &= ~threes
            twos &= ~threes
        
        return ones
