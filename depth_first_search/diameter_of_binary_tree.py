"""
Diameter of binary tree
LC 543 (easy)

Problem: 
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root. The length of 
a path between two nodes is represented by the number of edges between them.


Example 1:
          1
		 / \
		2   3
	       / \
		  4   5
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].


Example 2:
    1
   / 
  2
Input: root = [1,2]
Output: 1

Category: 
Binary tree, depth first search, stack

Solution Explanation:
For any given node, the the diameter will be the maximum of:
(1) The diameter of the left subtree
(2) the diameter of the right subtree
(3) the diameter of the current tree

The diameter of any subtree will be the height of the left subtree, plus the 
height of the right subtree, plus 2 (for the two edges leading to either 
subtree).

TC: O(n)
SC: O(n)
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def diameter_of_binary_tree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""

		def solve(root):
			if not root:
				# (height, diameter)
				return (-1, 0)
			
			left_height, left_diameter = solve(root.left)
			right_height, right_diameter = solve(root.right)

			tree_height = max(left_height, right_height) + 1
			tree_diameter = left_height + right_height + 2
		
			return tree_height, max(left_diameter, right_diameter, tree_diameter)
		
		diameter = solve(root)[1]

		return diameter


if __name__ == '__main__':
	# Set up for example 1 mentioned in the description. Output: 3
	node15 = TreeNode(5)
	node14 = TreeNode(4)
	node12 = TreeNode(2, node14, node15)
	node13 = TreeNode(3)
	node11 = TreeNode(1, node12, node13)

	# Set up for example 2 mentioned in the description. output: 1
	node22 = TreeNode(2)
	node21 = TreeNode(1, node22)

	sol = Solution()
	result = sol.diameter_of_binary_tree(node11)
	print(result)
