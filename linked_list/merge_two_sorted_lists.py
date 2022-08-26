"""
Merge two sorted lists
LC 21 (easy)

Problem: 
You are given the heads of two sorted linked lists list1 and list2.Merge the 
two lists in a one sorted list. The list should be made by splicing together 
the nodes of the first two lists.
Return the head of the merged linked list.

Category: 
Linked list, recursion

Solution Explanation:
If either input list is None, return the other list. Next, determine which 
head will be the first item of the result list. From there, compare the next 
list1 node to the next list2 node to determine the next result list node, 
updating the appropriate values each time. Once either list1 or list2 is 
exhausted, finish out by adding the leftover nodes to the result.

TC: O(n)
SC: O(1)
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def merge_two_lists(self, list1, list2):
		"""
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
		if list1 is None:
			return list2
		if list2 is None:
			return list1
		
		# Determine the head
		if list1.val <= list2.val:
			result_node = head = list1
			list1 = list1.next
		else:
			result_node = head = list2
			list2 = list2.next
		
		# Compare and build the new list until either input list is exhausted
		while list1 is not None and list2 is not None:
			if list1.val <= list2.val:
				result_node.next = list1
				list1 = list1.next
			else:
				result_node.next = list2
				list2 = list2.next

			result_node = result_node.next
		
		# Finish out any remaining nodes from either list

		# Below is first attempt, but there is a better way
		'''
		while list1 is not None:
			result_node.next = list1
			list1 = list1.next
			result_node = result_node.next
		
		while list2 is not None:
			result_node.next = list2
			list2 = list2.next
			result_node = result_node.next
		'''

		# Instead of the above, just point to whichever list isnt None
		result_node.next = list1 or list2
		
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
	node14 = ListNode(4)
	node12 = ListNode(2, node14)
	node11 = ListNode(1, node12)

	node24 = ListNode(4)
	node23 = ListNode(3, node24)
	node21 = ListNode(1, node23)

	sol = Solution()
	result = sol.merge_two_lists(node11, node21)
