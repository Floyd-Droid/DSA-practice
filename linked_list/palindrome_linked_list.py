"""
Palindrome linked list
LC 234 (easy)

Problem: 
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1
Input: head = [1,2,2,1]
Output: true

Example 2
Input: head = [1,2]
Output: false

Category: 
Linked list, two pointers, stack

Solution Explanation:
Two pointers in O(n) space approach - Use a slow and fast pointer, where the 
slow pointer advances one step at a time, and the fast advances two steps at a 
time. As you go, add the node of the slow pointer's value to a list. When the 
fast pointer gets to the end of the list (either fast is None or its 
next is None), then the slow pointer will be in the middle of the list. If fast 
is not None, then the palindrome has an odd number of letters, so we need 
to advance the slow pointer by 1 for the next part to work. We then advance the 
slow pointer by one repeatedly, and compare the node values with the values we 
stored in the array, but do so in reverse order. If any of them arent equal, 
then we dont have a palindrome. This solution has a space complexity of O(n). 

The leetcode solution encourages you to do so in constant time, which would 
involve a similar approach to above, except you would need to reverse the 
second half of the list in place, determine if there is a palindrome, then 
restore the list afterwards. You could still do this in one pass, but you 
wouldnt need any auxiliary space. I'll try this in the future


TC: O(n)
SC: O(n)
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def is_palindrome_linear_space(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		slow = fast = head
		vals = []

		while fast is not None and fast.next is not None:
			vals.append(slow.val)
			slow = slow.next
			fast = fast.next.next
		
		if fast is not None:
			# If the palindrome is odd, the center value will be ignored
			slow = slow.next
		
		for i in range(len(vals) - 1, -1, -1):
			if slow.val == vals[i]:
				slow = slow.next
				continue
			else:
				return False
		
		return True


if __name__ == '__main__':
	# input: [1, 2, 2, 1], output: True
	node14 = ListNode(1)
	node13 = ListNode(2, node14)
	node12 = ListNode(2, node13)
	node11 = ListNode(1, node12)  

	# input: [1, 2, 3, 2, 1]. output: True
	node25 = ListNode(1)
	node24 = ListNode(2, node25)
	node23 = ListNode(3, node24)
	node22 = ListNode(2, node23)
	node21 = ListNode(1, node22)  

	# input: [1, 2], output: False
	node32 = ListNode(2)
	node31 = ListNode(1, node32) 

	sol = Solution()
	result = sol.is_palindrome(node21)
	print(result)
