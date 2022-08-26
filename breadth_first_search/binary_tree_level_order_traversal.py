"""
Binary tree level order traversal
LC 102 (medium)

Problem: 
Given the root of a binary tree, return the level order traversal of its 
nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Category: 
Tree, breadth first search, queue

Solution Explanation:
There are two solutions below. The first one is written to satisfy the output 
conditions of the LeetCode problem. They want each level of nodes to be 
presented as a nested array within the output array. The other solution was 
written without that nonsense restriction, and is less headache-inducing as 
a result.

For the first solution, each item in the queue will be an array of nodes which 
comprise an entire level of the tree. So for each set/level of nodes, we visit 
each one and gather their values and children in separate arrays as we do so. 
Then, when done with that level of nodes, we append gathered values array to 
the output array, and append the level children array to the queue. Repeat 
until the queue is empty

If the output array simply needs to have the nodes in order of appearance 
with no nesting, the second solution suffices, and is just a simpler version 
of the first solution

TC: O(n)
SC: O(n)
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def levelorder_leetcode(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if root == None:
			return []
		
		queue = [[root]]
		traversal = []

		while queue:
			node_set = queue.pop(0)
			next_traversal = []
			next_queue = []

			while node_set:
				node = node_set.pop(0)
				next_traversal.append(node.val)
				
				if node.left is not None:
					next_queue.append(node.left)
				if node.right is not None:
					next_queue.append(node.right)
				
			traversal.append(next_traversal)
			if next_queue:
				queue.append(next_queue)

		return traversal

	def levelorder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		queue = [root]
		order = []

		while queue:
			node = queue.pop(0)
			order.append(node.val)

			if node.left:
				queue.append(node.left)
			
			if node.right:
				queue.append(node.right)
		
		return order


if __name__ == '__main__':
	# Set up for example 1 mentioned in the description
	node15 = TreeNode(15)
	node7 = TreeNode(7)
	node20 = TreeNode(20, node15, node7)
	node9 = TreeNode(9)
	node3 = TreeNode(3, node9, node20)

	sol = Solution()
	result = sol.levelorder(node3)
	print(result)
