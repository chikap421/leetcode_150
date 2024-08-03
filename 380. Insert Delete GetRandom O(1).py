class RandomizedSet(object):

    def __init__(self):
        # List to store elements
        self.data = []
        # Hash map to store elements to index mapping
        self.indices = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.indices:
            return False
        self.data.append(val)
        self.indices[val] = len(self.data) - 1
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.indices:
            return False
        
        # Get index of the element to remove
        idx_to_remove = self.indices[val]
        last_element = self.data[-1]

        # Move the last element to the place of the element to remove
        self.data[idx_to_remove] = last_element
        self.indices[last_element] = idx_to_remove

        # Remove the last element
        self.data.pop()
        del self.indices[val]

        return True

        

    def getRandom(self):
        """
        :rtype: int
        """

        return random.choice(self.data)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()