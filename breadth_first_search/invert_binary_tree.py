"""
Invert binary tree
LC 226 (easy)

Problem: 
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Category: 
Binary tree, breadth first search, depth first search

Solution Explanation:
Breadth first search approach - Using a queue, start at the root of the tree. 
For each node in the queue, swap its left and right children, and then add 
both of them to the queue.

Depth first search recursive - Start at the root node, and recurse on the child 
nodes until reaching leaf nodes. Swap the left and right children, working 
back up the tree to the root

TC: O(n) for BFS and DFS
SC: O(n) for BFS and DFS
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def invert_tree_BFS(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		if not root:
			return root
		
		queue = [root]

		while queue:
			node = queue.pop(0)
			node.left, node.right = node.right, node.left

			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		
		return root
	
	def invert_tree_DFS_recursive(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""

		def invert(root):
			if not root:
				return root
		
			invert_right = invert(root.right)
			invert_left = invert(root.left)

			root.left = invert_right
			root.right = invert_left

		return invert(root)


if __name__ == '__main__':
	# Set up for example 1 mentioned in the description
	node11 = TreeNode(1)
	node13 = TreeNode(3)
	node16 = TreeNode(6)
	node19 = TreeNode(9)
	node12 = TreeNode(2, node11, node13)
	node17 = TreeNode(7, node16, node19)
	node14 = TreeNode(4, node12, node17)

	sol = Solution()
	result = sol.invert_tree_BFS(node14)
