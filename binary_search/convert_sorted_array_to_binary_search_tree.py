"""
Convert sorted array to binary search tree
LC 108 (easy)

Problem: 
Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree. A height-balanced binary 
tree is a binary tree in which the depth of the two subtrees of every node 
never differs by more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Category: 
binary search, array, divide and conquer

Solution Explanation:
First attempt - Use the divide and conquer approach. We create a helper 
function that takes a left and right index value to deal with the left and 
right halves of each subarray as we divide. We take the current mid value 
and create a node from it. Its left child will be the middle value of the 
left array, and its right child will be the middle value of the right array, 
and so on.

The other solution is just a much cleaner version of the first. We use slices 
instead of explicitly passing in left and right indices, which means we don't 
need the helper function, instead recursively calling the main function on the 
left and right slices.

TC: O(n)
SC: O(1)
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def sorted_array_to_BST(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""
		if len(nums) == 0:
			return

		mid = len(nums) // 2

		new_node = TreeNode(nums[mid])
		new_node.left = self.sorted_array_to_BST(nums[:mid])
		new_node.right = self.sorted_array_to_BST(nums[mid+1:])

		return new_node

	def sorted_array_to_BST_first_attempt(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""

		def add_to_tree(nums, left, right):
			if left > right:
				return
			
			mid = (right + left) // 2

			new_node = TreeNode(nums[mid])
			
			new_node.left = add_to_tree(nums, left, mid-1)
			new_node.right = add_to_tree(nums, mid+1, right)

			return new_node
		
		mid = (len(nums)-1) // 2
		root = TreeNode(nums[mid])
		root.left = add_to_tree(nums, 0, mid - 1)
		root.right = add_to_tree(nums, mid+1, len(nums) - 1)

		return root


if __name__ == '__main__':

	# output: [0,-3,9,-10,null,5]
	nums1 = [-10,-3,0,5,9]

	# output: [3, 1]
	nums2 = [1,3]
	
	sol = Solution()
	result = sol.sorted_array_to_BST(nums1)
	print(result.val)
