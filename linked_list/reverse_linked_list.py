"""
Reverse linked list
LC 206 (easy)

Problem: 
Given the head of a singly linked list, reverse the list, and return the 
reversed list.

Category: 
Linked list, recursion

Solution Explanation:
Perform an in-place reversal. For each node, temporarily store the next node 
in a variable. Update the current node's next to be the previous node. Update 
the prev node to be the current node for the next iteration, and update the 
current node to be the what used to be the current node's next (before it was 
updated). Once the current node is None, simply return the prev node, since it 
is the new head

TC: O(n)
SC: O(1)
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def reverse_linked_list(self, head):
		"""
        :type head: ListNode
        :rtype: ListNode
        """
		current_node = head
		prev_node = None

		while current_node:
			next_node = current_node.next
			current_node.next = prev_node
			prev_node = current_node
			current_node = next_node
		
		self.print_result(prev_node)

		return prev_node
	
	def print_result(self, head):
		current_node = head
		result = ''

		while current_node is not None:
			result += str(current_node.val) + ' -> '
			current_node = current_node.next
		
		print(result)


if __name__ == '__main__':
	node15 = ListNode(5)
	node14 = ListNode(4, node15)
	node13 = ListNode(3, node14)
	node12 = ListNode(2, node13)
	node11 = ListNode(1, node12)

	sol = Solution()
	result = sol.reverse_linked_list(node11)
