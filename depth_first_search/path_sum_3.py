"""
Path sum III
LC 437 (medium)

Problem: 
Given the root of a binary tree and an integer targetSum, return the number of 
paths where the sum of the values along the path equals targetSum. The path 
does not need to start or end at the root or a leaf, but it must go downwards 
(i.e., traveling only from parent nodes to child nodes).


Example 1:
          10
		 /  \
		5    -3
	   / \     \
	  3	  2     11
     / \   \
    3  -2   1
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: There are 3 distinct paths in the tree that sum to 8


Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Category: 
Binary tree, depth first search, stack, hash table

Solution Explanation:
Approach 1 (without hashtable) - We need to consider every combination of nodes to 
see if their values sum to the target. So we start with the root node in an 
iterative stack. We pop the root node add its children to the stack. We then 
call a recursive function on the current node whose goal is to take the current 
sum of the nodes so far and compare with the target, incrementing the counter 
if they match. This occurs all the way down the tree.
Then, the entire process repeats for the next node in the iterative stack, 
which is the root's right child, then for the left child node, and so on. This 
process result in a quadratic time complexity.

Approach 2 (with hashtable) - We can reduce the time complexity from quadratic to 
linear by utilizing a hash table to track the running sum for any given node, 
and check if the difference between the target and the current running sum 
exists in the hash table. If so, we increment the number of paths. Before returning 
to the caller, we decrement the value associated with the current sum in the 
hash table, effectively removing it as a path under consideration.
This concept is also used in problems like two sum (LC 1)

TC: O(n^2) approach1, O(n) approach2
SC: O(n) approach1 (stack), O(n) approach2 (hash table)
"""
from collections import defaultdict


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def path_sum_approach1(self, root, targetSum):
		"""
		:type root: TreeNode
		:type targetSum: int
		:rtype: int
		"""
		if not root:
			return root
		
		stack = [root]
		self.num_paths = 0

		while stack:
			node = stack.pop()
			if node.left:
				stack.append(node.left)
			if node.right:
				stack.append(node.right)
			
			
			self.dfs(node, 0, targetSum)
		
		return self.num_paths
	
	def dfs1(self, root, current_sum, target_sum):
		if not root:
			return root
		
		current_sum += root.val
		if current_sum == target_sum:
			self.num_paths += 1
		
		self.dfs(root.left, current_sum, target_sum)
		self.dfs(root.right, current_sum, target_sum)
	
	def path_sum_approach2(self, root, targetSum):
		"""
		:type root: TreeNode
		:type targetSum: int
		:rtype: int
		"""
		self.count = 0
		running_sum = 0
		sums = defaultdict(int)

		def dfs2(node, running_sum):
			if not node:
				return node
			
			running_sum += node.val

			if running_sum == targetSum:
				self.count += 1

			if sums.get(running_sum - targetSum):
				self.count += sums[running_sum - targetSum]
			
			sums[running_sum] += 1
			
			dfs2(node.left, running_sum)
			dfs2(node.right, running_sum)

			if sums[running_sum]:
				sums[running_sum] -= 1
			
		dfs2(root, running_sum)
		return self.count


if __name__ == '__main__':
	# Set up for example 1 mentioned in the description. Output: 3
	node131 = TreeNode(3)
	node1n2 = TreeNode(-2)
	node11 = TreeNode(1)

	node111 = TreeNode(11)
	node1n3 = TreeNode(-3, None, node111)

	node132 = TreeNode(3, node131, node1n2)
	node12 = TreeNode(2, None, node11)
	node15 = TreeNode(5, node132, node12)
	node10 = TreeNode(10, node15, node1n3)


	# Set up for example 2 mentioned in the description. output: 1
	node22 = TreeNode(2)
	node21 = TreeNode(1, node22)

	sol = Solution()
	result = sol.path_sum_approach2(node10, 8)
	print(result)
