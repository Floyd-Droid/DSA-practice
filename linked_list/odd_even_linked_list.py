"""
Odd even linked list
LC 328 (medium)

Problem: 
Given the head of a singly linked list, group all the nodes with odd indices 
together followed by the nodes with even indices, and return the reordered 
list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain 
as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Category: 
Linked list

Solution Explanation:
Create two new lists; one for odd indices, and one for even. Start by assigning 
the first item of the list as the head of the odd list, and the second item as 
the head of the even list. The current_node represents the node to be placed in 
either list. We also have a boolean which determines whether the current node 
is to be placed in the even or odd list. Repeatedly advance in the main list 
and use the boolean to append the current node to the appropriate list. Once 
the current node is None, we firstly take the tail of the odd list and point 
it to the head of the even list, and then make sure the tail of the even list 
points to None (otherwise we may get a cycle).

TC: O(n)
SC: O(1)
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def odd_even_list(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head or not head.next:
			return head
		
		current_odd = head
		even_head = current_even = head.next

		if current_even.next is None:
			current_odd.next = current_even
			return head

		current_node = current_even.next
		is_even = False

		while current_node:
			if is_even:
				current_even.next = current_node
				current_even = current_even.next
			else:
				current_odd.next = current_node
				current_odd = current_odd.next
			
			is_even = not is_even
			current_node = current_node.next
		
		current_odd.next = even_head
		current_even.next = None

		return head

	def print_result(self, head):
		current_node = head
		result = ''

		while current_node is not None:
			
			result += str(current_node.val) + ' -> '
			current_node = current_node.next

		print(result)

if __name__ == '__main__':
	# input: [1, 2, 3, 4, 5]. output: [1,3,5,2,4]
	node15 = ListNode(5)
	node14 = ListNode(4, node15)
	node13 = ListNode(3, node14)
	node12 = ListNode(2, node13)
	node11 = ListNode(1, node12)  

	# input: [2,1,3,5,6,4,7], output: [2,3,6,7,1,5,4]
	node27 = ListNode(7)
	node24 = ListNode(4, node27) 
	node26 = ListNode(6, node24)
	node25 = ListNode(5, node26) 
	node23 = ListNode(3, node25) 
	node21 = ListNode(1, node23) 
	node22 = ListNode(2, node21)

	sol = Solution()
	result = sol.odd_even_list(node22)
	sol.print_result(result)
