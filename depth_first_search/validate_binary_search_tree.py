"""
Validate binary search tree
LC 98 (medium)

Problem: 
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
  The left subtree of a node contains only nodes with keys less than the node's key.
  The right subtree of a node contains only nodes with keys greater than the node's key.
  Both the left and right subtrees must also be binary search trees.


Example 1:
Input: root = [2,1,3]

    2
   / \
  1   3

Output: true


Example 2:
Input: root = [5,1,4,null,null,3,6]

          5
		 / \
		1   4
	       / \
		  3   6

Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Category: 
Tree, depth first search, stack

Solution Explanation:
You could take a recursive or an iterative approach. The below solutions are 
iterative.

In the cleaner solution, we start with the root node along with a lower and 
upper values of -inf and +inf respectively. The goal is to track the lower and 
upper bounds that the current node must fall between as we add children to the 
stack. Using example 2 above, we first check that the root node (value of 5) 
falls between -inf and +inf. It does, so we append to the stack a tuple which 
includes the right child node followed by the lower and upper bounds.When the 
right child is added, the upper bound is inherited, while the lower bound is 
updated to be the value of the current node. The inverse is true when adding 
the left node to the stack. The process is repeated until a node's value falls 
outside of the lower and upper bounds, or the stack is exhausted.

In my first attempt, I kept an array to track the bounds. The idea was to 
traverse the tree left to right and bottom-up. For each node visited, I would 
record its value in the array. When visiting the next node, I would compare 
its value to the last value stored in the array, which should result in a sorted 
array (if its a valid BST). If the current node's value was less than the last 
array value, we know this isnt a valid BST.

TC: O(n) for both
SC: O(n) for first attempt, O(1) for improved solution
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def is_valid_BST_iterative(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if not root:
			return True

		stack = [(root, float('-inf'), float('inf'))]

		while stack:
			node, lower, upper = stack.pop()

			if not node:
				continue

			if node.val <= lower or node.val >= upper:
				return False
			
			stack.append((node.right, node.val, upper))
			stack.append((node.left, lower, node.val))
		
		return True
	
	def is_valid_BST_iterative_first_attempt(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		stack = [root]
		sequence = []
		current_node = root

		while stack:
			while current_node.left is not None:
				if not current_node.left.val in sequence:
					stack.append(current_node.left)
					current_node = current_node.left
			
			current_node = stack.pop()
			
			if sequence:
				if current_node.val <= sequence[-1]:
					return False
			sequence.append(current_node.val)
			
			if current_node.right is not None:
				stack.append(current_node.right)
				current_node = current_node.right

		return True


if __name__ == '__main__':
	# Set up for example 2 mentioned in the description
	node1 = TreeNode(1)
	node3 = TreeNode(3)
	node6 = TreeNode(6)
	node4 = TreeNode(4, node3, node6)
	node5 = TreeNode(5, node1, node4)

	sol = Solution()
	result = sol.is_valid_BST_iterative(node1)
	print(result)
