"""
kth smallest element in a binary search tree
LC 230 (medium)

Problem: 
Given the root of a binary search tree, and an integer k, return the kth 
smallest value (1-indexed) of all the values of the nodes in the tree.


Example 1:
          3
		 / \
		1   4
	     \ 
		  2   
Input: root = [3,1,4,null,2], k = 1
Output: 1


Example 2:
          5
		 / \
		3   6
	   / \
	  2   4 
	 /
	1  
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Category: 
Binary tree, depth first search, stack

Solution Explanation:
We need to traverse the binary search tree in acending order. Each time we reach 
the next ordered node, we will increment an integer value. Once that integer 
value equals k, we return the current node's value. We create a function to 
perform a depth first search for each node. For any node passed to this function, 
we prioritize getting to the leftmost leaf node. Once the current node's left 
is None, we increment the counter and return the current node's value if the 
counter equals k. Otherwise, we recurse on the right child node and the process 
repeats. One of the recursive operations will result in finding the value, while 
the other will not (ie, will return None). So, ultimately, we return whichever 
result is not None.

TC: O(n)
SC: O(1)
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def kth_smallest(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: int
		"""
		if not root:
			return root
		
		self.n = 0

		def dfs(root, k):
			if not root:
				return root

			left_result = dfs(root.left, k)
			
			self.n += 1
			if self.n == k:
				return root.val

			right_result = dfs(root.right, k)

			if left_result is not None:
				return left_result
			return right_result
			
		return dfs(root, k)


if __name__ == '__main__':
	# Set up for example 1 mentioned in the description. 
	node12 = TreeNode(2)
	node14 = TreeNode(4)
	node11 = TreeNode(1, None, node12)
	node13 = TreeNode(3, node11, node14)


	# Set up for example 2 mentioned in the description.
	node21 = TreeNode(1)
	node24 = TreeNode(4)
	node26 = TreeNode(6)
	node22 = TreeNode(2, node21)
	node23 = TreeNode(3, node22, node24)
	node25 = TreeNode(5, node23, node26)

	sol = Solution()
	result = sol.kth_smallest(node13, 1)
	print(result)
