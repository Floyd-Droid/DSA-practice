"""
Climbing stairs
LC 70 (easy)

Problem: 
You are climbing a staircase. It takes n steps to reach the top. Each time you 
can either climb 1 or 2 steps. In how many distinct ways can you climb to the 
top?


Category: 
Math, dynamic programming

Solution Explanation:
This satisfies the two cases required for dynamic programming:
(1) The optimal solution to the problem is the optimal solution of its 
subproblems.
(2) There are overlapping subproblems

This problem is basically the same as the fibonacci sequence, except the 
sequence is offset:
fib: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...   (if taking n=1 to be 0)
stairs: 1, 2, 3, 5, 8, 13, 21, ...

In the recursive approach, we first cover the base cases: The first 2 numbers 
in the sequence (n=1 and n=2) are 1 and 2 respectively. Otherwise, we return 
the sum two recursive calls, where one is pass n-1 and the other n-2, since 
we can only climb one or two steps at a time

The recursive approach with memoization is similar, except we keep track of 
previously solved inputs in an array and pull from that before attmepting to 
recurse

In the iterative approach, we can work from the base case upward. You could 
use an array to track the values, but its better to do so in constant space, 
so I instead use 3 variables to track any given n, n-1, and n-2. A for loop 
continuously cycles the variables and updates their values up to n.


TC: O(n) for iterative, O(2^n) for recursive, O(n) for recursive with memoization
SC: O(1) for iterative, O(2^n) for recursive, O(n) for recursive with memoization
"""


class Solution:
	def climb_stairs_iterative(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n <= 2:
			return n
		
		n2 = 0  # n=0 initially
		n1 = 1  # n=1 initially
		val = 2  # n=2 initially

		for i in range(2, n):
			n2 = n1
			n1 = val
			val = n2 + n1

		return val

	def climb_stairs_recursive(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n <= 2:
			return n
		
		return self.climb_stairs_recursive(n-1) + self.climb_stairs_recursive(n-2)
	
	def climb_stairs_recursive_with_memoization(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		solutions = [-1] * (n + 1)
		solutions[0] = 0
		solutions[1] = 1
		solutions[2] = 2

		def solve(n):
			if solutions[n] != -1:
				return solutions[n]
		
			solutions[n] = solve(n-1) + solve(n-2)
			return solutions[n]
		
		result = solve(n)

		return result


if __name__ == '__main__':

	sol = Solution()
	result = sol.climb_stairs_recursive_with_memoization(5)
	print(result)
