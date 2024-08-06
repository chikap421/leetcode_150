import heapq

class MedianFinder(object):

    def __init__(self):
        # Initialize two heaps
        self.max_heap = []  # max heap (inverted to use min heap in Python)
        self.min_heap = []  # min heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Add number to max_heap (inverted to use min heap)
        heapq.heappush(self.max_heap, -num)

        # Ensure max_heap's root is less than min_heap's root
        if (self.min_heap and -self.max_heap[0] > self.min_heap[0]):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Balance the heaps such that max_heap has at most one more element than min_heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
