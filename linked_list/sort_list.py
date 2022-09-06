"""
Sort list
LC 148 (medium)

Problem: 
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and 
O(1) memory (i.e. constant space)?

Example 1
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Category: 
Linked list, two pointers

Solution Explanation:
Top-down merge sort - Merge sort is a divide and conquer algorithm, so the first 
step is to divide the linked list in half until we are dealing with segments of 
one item. Use the slow and fast pointer technique to find the middle point, 
separate the two segments of the list, and pass each segment back into the same 
function.
The second step is to merge the resulting list segments. Once we get down to 
single item lists, we begin building a sorted list by merging adjacent lists 
in the tree. Since the lists are always sorted, we work incrementally left to 
right, comparing values in both lists and adjusting pointers accordingly, then 
returning the head of the sorted/merged list


TC: O(n*log(n))
SC: O(1)
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def sort_list_merge_sort(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head or not head.next:
			return head
		
		pre_slow = None
		slow = fast = head

		while fast and fast.next:
			pre_slow = slow
			slow = slow.next
			fast = fast.next.next
		
		pre_slow.next = None
		
		def merge(left_node, right_node):
			tmp = tail = ListNode()

			while left_node and right_node:
				if left_node.val < right_node.val:
					tail.next = left_node
					tail = tail.next
					left_node = left_node.next
				else:
					tail.next = right_node
					tail = tail.next
					right_node = right_node.next
			
			tail.next = left_node or right_node
			
			return tmp.next

		left_head = self.sort_list_merge_sort2(head)
		right_head = self.sort_list_merge_sort2(slow)
		
		return merge(left_head, right_head)

	def print_result(self, head):
		current_node = head
		result = ''

		while current_node is not None:
			result += str(current_node.val) + ' -> '
			current_node = current_node.next
		
		print(result)


if __name__ == '__main__':
	# head = [4,2,1,3], output: [1, 2, 3, 4]
	node13 = ListNode(3)
	node11 = ListNode(1, node13)
	node12 = ListNode(2, node11)
	node14 = ListNode(4, node12)

	# head = [-1,5,3,4,0], output: [-1, 0, 3, 4, 5]
	node20 = ListNode(0)
	node24 = ListNode(4, node20)
	node23 = ListNode(3, node24)
	node25 = ListNode(5, node23)
	node21 = ListNode(-1, node25)

	sol = Solution()
	result = sol.sort_list_merge_sort2(node14)
	sol.print_result(result)
