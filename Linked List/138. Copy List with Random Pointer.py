# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        # Step 1: Create new nodes and interweave with original nodes
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        
        # Step 2: Assign random pointers to the new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # Step 3: Unweave the lists to separate original and copied nodes
        current = head
        copy_head = head.next
        while current:
            copy = current.next
            current.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            current = current.next
        
        return copy_head

# Example usage:
# Creating a linked list with random pointers
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1.random = None
node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

solution = Solution()
copied_list = solution.copyRandomList(node1)

# Output the result linked list
output = []
copied_current = copied_list
while copied_current:
    random_index = -1
    if copied_current.random:
        random_index = copied_current.random.val
    output.append([copied_current.val, random_index])
    copied_current = copied_current.next
print(output)  # Output should show the deep copied list structure
