# O(n) time complexity solution
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        count = [0] * (n + 1)
        
        # Populate the count array
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
        
        total = 0
        # Traverse the count array from end to start
        for i in range(n, -1, -1):
            total += count[i]
            if total >= i:
                return i
        
        return 0


# O(nlogn) time complexity solution 
# class Solution(object):
#     def hIndex(self, citations):
#         """
#         :type citations: List[int]
#         :rtype: int
#         """
        
#         # Sort the citations in the descending order
#         citations.sort(reverse=True)

#         h_index = 0

#         # Iterate through the sorted list and find the h-index
#         for i in range (len(citations)):
#             if citations[i] >= i + 1:
#                 h_index = i + 1
#             else:
#                 break
#         return h_index
#


