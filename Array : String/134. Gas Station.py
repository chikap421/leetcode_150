class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        
        total_surplus = 0
        current_surplus = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_surplus += gas[i] - cost[i]
            current_surplus += gas[i] - cost[i]
            
            if current_surplus < 0:
                start_index = i + 1
                current_surplus = 0
        
        return start_index if total_surplus >= 0 else -1
