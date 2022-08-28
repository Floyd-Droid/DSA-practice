"""
Fibonacci number
LC 509 (easy)

Problem: 
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the 
Fibonacci sequence, such that each number is the sum of the two preceding 
ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).


Category: 
Math, dynamic programming

Solution Explanation:
This satisfies the two cases required for dynamic programming:
(1) The optimal solution to the problem is the optimal solution of its 
subproblems.
(2) There are overlapping subproblems

In the recursive approach, we first cover the base cases: The first 2 numbers 
in the sequence (n=1 and n=2) are 0 and 1 respectively. Otherwise, we return 
the sum two recursive calls, where one is pass n-1 and the other n-2, as in 
the above equation

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
	def fib_iterative(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n == 0:
			return 0
		
		if n <= 2:
			return n - 1
		
		n2 = 0  # n-2 value
		n1 = 1  # n-1 value
		val = 1  # n value

		for i in range(3, n):
			n2 = n1
			n1 = val
			val = n2 + n1

		return val

	def fib_recursive(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n < 2:
			return 0
		if n == 2:
			return 1
		
		return self.fib_recursive(n-1) + self.fib_recursive(n-2)
	
	def fib_recursive_with_memoization(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		solutions = [-1] * (n + 1)
		solutions[0] = solutions[1] = 0
		solutions[2] = 1

		def solve(n):
			if solutions[n] != -1:
				return solutions[n]
		
			solutions[n] = solve(n-1) + solve(n-2)
			return solutions[n]
		
		result = solve(n)

		return result


if __name__ == '__main__':

	sol = Solution()
	result = sol.fib_recursive_with_memoization(10)
	print(result)
