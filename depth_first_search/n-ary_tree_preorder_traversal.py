"""
N-ary tree preorder traversal
LC 589 (easy)

Problem: 
Given the root of an n-ary tree, return the preorder traversal of its nodes' 
values. Nary-Tree input serialization is represented in their level order 
traversal. Each group of children is separated by the null value (See examples)

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Category: 
Tree, depth first search, stack

Solution Explanation:
Iterative approach - Use a list as a stack. Preorder indicates we visit a node 
before dealing with its children. So pop a node in the stack and add its 
value to the return array. Then, iterate over its children in reverse order, 
adding each to the stack as you go. Repeat until the stack is empty

Recursive approach - Use the call stack to traverse the tree. Instead of 
adding each child to a list, recursively call the function, passing each child 
as the new 'root' each time.

TC: O(n) for both approaches
SC: O(n) for both approaches
"""

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
	def preorder_iterative(self, root):
		"""
		:type root: Node
		:rtype: List[int]
		"""
		stack = [root]
		order = []

		while stack:
			node = stack.pop()
			order.append(node.val)

			if node.children:
				for child in reversed(node.children):
					stack.append(child)

		return order
	
	def preorder_recursive(self, root):
		order = []

		def preorder_solve(root):
			if root:
				order.append(root.val)
				if root.children:
					for child in root.children:
						preorder_solve(child)

		preorder_solve(root)
		return order


if __name__ == '__main__':
	node1 = Node(1)
	node2 = Node(2)
	node3 = Node(3)
	node4 = Node(4)
	node5 = Node(5)
	node6 = Node(6)

	# Set up for example 1 mentioned in the description
	node1.children = [node3, node2, node4]
	node3.children = [node5, node6]

	sol = Solution()
	result = sol.preorder_iterative(node1)
	print(result)
