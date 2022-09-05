"""
Remove nth node from the end of a list
LC 19 (medium)

Problem: 
Given the head of a linked list, remove the nth node from the end of the list 
and return its head.

Category: 
Linked list, two pointers

Solution Explanation:
Two pointers approach - To establish the nth node from the end of the list, 
start at the head and move forward n times or until the current_node's next 
is None. If we reach a next of None before repeating the above process n-1 
times, then n must be the length of the list, so we set the head to be the 
current head's next and return it. Otherwise, we then repeatedly advance the 
current_node and the lag_node by one each time until the current_node's next 
is None and we've reached the end of the list. At this point, the lag node's 
next is the node which needs to be removed. So we store the node after it in 
memory, set the removal node's next to be None, then set the lag node's next 
to be the node in memory.

TC: O(n)
SC: O(1)
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def remove_nth_from_end(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		if head is None or head.next is None:
			return None

		current_node = lag_node = head

		k = 0
		while k < n and current_node.next is not None:
			current_node = current_node.next
			k += 1
		
		if k < n:
			head = head.next
			lag_node.next = None
			self.print_result(head)
			return head

		while current_node.next is not None:
			current_node = current_node.next
			lag_node = lag_node.next
		
		if lag_node.next is current_node:
			lag_node.next = None
		else:
			tmp_node = lag_node.next.next
			lag_node.next.next = None
			lag_node.next = tmp_node

		self.print_result(head)

		return head
	
	def print_result(self, head):
		current_node = head
		result = ''

		while current_node is not None:
			result += str(current_node.val) + ' -> '
			current_node = current_node.next
		
		print(result)


if __name__ == '__main__':
	 # input: [1, 2, 3, 4, 5], n=2   output: [1, 2, 3, 5]
	node15 = ListNode(5)
	node14 = ListNode(4, node15)
	node13 = ListNode(3, node14)
	node12 = ListNode(2, node13)
	node11 = ListNode(1, node12)

	# input: [1, 2]. For n=1, output is [1], For n=2, output is [2]
	node22 = ListNode(2)
	node21 = ListNode(1, node22)  

	# input: [1, 2, 3]. For n=1, output is [1, 2]. For n=3, output is [2, 3]
	node33 = ListNode(3)
	node32 = ListNode(2, node33)
	node31 = ListNode(1, node32)

	sol = Solution()
	result = sol.remove_nth_from_end(node31, 3)
