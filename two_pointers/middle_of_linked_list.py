"""
Middle of a linked list
LC 876 (easy)

Problem: 
Given the head of a singly linked list, return the middle node of the linked 
list. If there are two middle nodes, return the second middle node.

Category: 
Linked list, two pointers

Solution Explanation:
Use two pointers: one slow (advances by 1 each time) and one fast (advances 
by two each time). Once the fast pointer corresponds to None or a node whose 
next is None, we know that the slow pointer will be at the middle of the list. 
Further, if there are two middle nodes, the second will be returned.

TC: O(n)
SC: O(1)
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def middle_node(self, head):
		"""
        :type head: ListNode
        :rtype: ListNode
        """
		slow_node = fast_node = head

		while fast_node and fast_node.next:
			slow_node = slow_node.next
			fast_node = fast_node.next.next
		
		return slow_node


if __name__ == '__main__':
	node16 = ListNode(6)
	node15 = ListNode(5, node16)
	node14 = ListNode(4, node15)
	node13 = ListNode(3, node14)
	node12 = ListNode(2, node13)
	node11 = ListNode(1, node12)

	sol = Solution()
	result = sol.middle_node(node11)
	print(result.val)
