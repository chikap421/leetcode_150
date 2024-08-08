# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        # Dictionary to save the cloned nodes
        cloned_nodes = {}
        
        # Helper function to perform DFS and clone nodes
        def dfs(node):
            if node in cloned_nodes:
                return cloned_nodes[node]
            
            # Clone the node
            clone = Node(node.val)
            cloned_nodes[node] = clone
            
            # Recursively clone the neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        # Start DFS from the input node
        return dfs(node)

# Example usage:
# Constructing the graph as per example 1
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

solution = Solution()
cloned_node = solution.cloneGraph(node1)

# To verify, you can print the cloned graph structure
def print_graph(node):
    visited = set()
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        print("Node {}: {}".format(node.val, [neighbor.val for neighbor in node.neighbors]))
        for neighbor in node.neighbors:
            dfs(neighbor)
    
    dfs(node)

print_graph(cloned_node)
