"""
Linked list cycle II
LC 142 (medium)

Problem: 
Given the head of a linked list, return the node where the cycle begins. If 
there is no cycle, return null. There is a cycle in a linked list if there is 
some node in the list that can be reached again by continuously following the 
next pointer. Internally, pos is used to denote the index of the node that 
tail's next pointer is connected to (0-indexed). It is -1 if there is no 
cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.

Category: 
Linked list, hash table, two pointers

Solution Explanation:
Starting at the head, continue down the linked list, adding each node to a 
dictionary as you go. For each node, check if it exists within the dictionary. 
If so, we have found the first node of the cycle.

TC: O(n)
SC: O(1)
"""

class ListNode(object):
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class Solution:
	def detect_cycle(self, head):
		"""
        :type head: ListNode
        :rtype: ListNode
        """
		visited_nodes = {}

		current_node = head

		while current_node:
			if current_node in visited_nodes:
				return current_node
			visited_nodes[current_node] = current_node.val
			current_node = current_node.next
		
		return None


if __name__ == '__main__':
	node4 = ListNode(-4)
	node3 = ListNode(0, node4)
	node2 = ListNode(2, node3)
	node1 = ListNode(1, node2)
	node4.next = node2
	# ^ output: node 2
	
	sol = Solution()
	result = sol.detect_cycle(node1)
	print(result.val)
