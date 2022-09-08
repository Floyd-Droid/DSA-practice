"""
Balanced binary tree
LC 110 (easy)

Problem: 
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the left and right subtrees of every node differ 
	in height by no more than 1.



Example 1:
          3
		 / \
		9  20
	       / \
		  15  7
Input: root = [3,9,20,null,null,15,7]
Output: true


Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Category: 
Binary tree, depth first search, stack

Solution Explanation:
For any given node, we need to answer three questions:
(1) Is the left subtree height balanced?
(2) is the right subtree height balanced?
(3) Is the difference in height between the left and right subtree less than 
	or equal to 1?

If yes to all three for every node, then the tree is height balanced

Recursive approach - The main function determines whether the left and right 
subtree are height balanced, while the helper function gets the height of the 
subtrees. If the three previously mentioned conditions are met, we return true

TC: O(n)
SC: O(n)
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def is_balanced_recursive(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""

		if not root:
			return True

		
		def get_height(root):
			if not root:
				return 0

			right_height = get_height(root.right)
			left_height = get_height(root.left)

			return max(right_height, left_height) + 1

		is_left_balanced = self.is_balanced_recursive(root.left)
		is_right_balanced = self.is_balanced_recursive(root.right)

		left_height = get_height(root.left)
		right_height = get_height(root.right)

		is_height_balanced = abs(left_height - right_height) <= 1
		
		return is_left_balanced and is_right_balanced and is_height_balanced




if __name__ == '__main__':
	# Set up for example 1 mentioned in the description. Output: True
	node115 = TreeNode(15)
	node17 = TreeNode(7)
	node19 = TreeNode(9)
	node120 = TreeNode(20, node115, node17)
	node13 = TreeNode(3, node19, node120)

	# Set up for example 2 mentioned in the description. Output: False
	node241 = TreeNode(4)
	node242 = TreeNode(4)
	node231 = TreeNode(3, node241, node242)
	node232 = TreeNode(3)
	node221 = TreeNode(2, node231, node232)
	node222 = TreeNode(2)
	node21 = TreeNode(1, node221, node222)

	sol = Solution()
	result = sol.is_balanced_recursive(node21)
	print(result)
