class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Convert binary strings to integers
        int_a = int(a, 2)
        int_b = int(b, 2)
        
        # Add the integers
        sum_int = int_a + int_b
        
        # Convert the sum back to a binary string and remove the '0b' prefix
        binary_sum = bin(sum_int)[2:]
        
        return binary_sum
