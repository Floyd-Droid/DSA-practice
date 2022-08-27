"""
Lowest Common Ancestor of a Binary Search Tree
LC 235 (easy)

Problem: 
Given a binary search tree (BST), find the lowest common ancestor (LCA) node 
of two given nodes in the BST. According to the definition of LCA on 
Wikipedia: “The lowest common ancestor is defined between two nodes p and q 
as the lowest node in T that has both p and q as descendants (where we allow 
a node to be a descendant of itself).”


Example 1:
          6
	   /     \
	  2       8
	 / \     / \
	0	4   7   9
       / \
      3   5

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


Example 2:
Same as example 1, except p = 0, q = 5
output: 2


Category: 
Tree, depth first search

Solution Explanation:
I begin by determing which input node is smaller so the comparisons are more 
straightforward. The goal is to find a node such that its value lies between 
the two input node values. If the current node's value is greater than the 
larger input node, we know that the common ancestor node must be in the left 
half of the tree, so we continue down that path. If the current node's value 
is less than the smaller input node, we go down the right path. Repeat until 
you've found the node that's within the specified range.

TC: O(log(n))
SC: O(1)
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def lowest_common_ancestor(self, root, p, q):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""

		if p.val <= q.val:
			smaller_node = p
			larger_node = q
		else:
			smaller_node = q
			larger_node = p
		
		current_node = root

		while not (smaller_node.val <= current_node.val <= larger_node.val):
			if current_node.val >= larger_node.val:
				current_node = current_node.left
			else:
				current_node = current_node.right
		
		return current_node


if __name__ == '__main__':
	# Set up for example 2 mentioned in the description
	node5 = TreeNode(5)
	node3 = TreeNode(3)
	node0 = TreeNode(0)
	node7 = TreeNode(7)
	node9 = TreeNode(9)

	node4 = TreeNode(4, node3, node5)
	node2 = TreeNode(2, node0, node4)
	node8 = TreeNode(8, node7, node9)
	node6 = TreeNode(6, node2, node8)  # output for p=node0 and q=node5 : node2

	sol = Solution()
	result = sol.lowest_common_ancestor(node6, node0, node5)
	print(result.val)
