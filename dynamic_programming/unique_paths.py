"""
Unique paths
LC 62 (medium)

Problem: 
There is a robot on an m x n grid. The robot is initially located at the 
top-left corner (i.e., grid[0][0]). The robot tries to move to the 
bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move 
either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths 
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal 
to 2 * 109.


Category: 
dynamic programming, depth-first-search

Solution Explanation:
This satisfies the two cases required for dynamic programming:
(1) The optimal solution to the problem is the optimal solution of its 
subproblems.
(2) There are overlapping subproblems

Recursive approach (DFS): we know that we can only move right or down, so for each 
m and n, we return the sum of recursive calls for (m=m-1 x n) and (m x n=n-1). 
If either m or n is 1, we know there is only one possible path, so we return 1.

Recursive with memoization approach: Same idea, but this time keep a 2D array 
to track previously calculated solutions. This way, if we visit a 'square' 
whose solution has already been calculated, we just return that instead of 
repeatedly traversing the same paths.

Iterative approach: Construct an m x n array and build from the base cases to 
the solution. We know if i or j is 0 (ie, m or n is 1), there is only one path. 
From there, for any given square, sum the results from the previous squares; 
(i-1, j) and (i, j-1).


TC: O(m*n) for iterative, O(2^(n*m)) for recursive, O(n*m) for recursive w/memo
SC: O(m*n) for iterative, O(2^(n*m)) for recursive, O(n*m) for recursive w/memo
"""


class Solution:
	def unique_paths_iterative(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		solutions = [[0]*n for _ in range(m)]

		for i in range(m):
			for j in range(n):
				if i == 0 or j == 0:
					solutions[i][j] = 1
				else:
					solutions[i][j] = solutions[i-1][j] + solutions[i][j-1]

		return solutions[m-1][n-1]

	def unique_paths_recursive(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		if m == 1 or n == 1:
			return 1
		return  self.unique_paths_recursive(m-1, n) + self.unique_paths_recursive(m, n-1)
		
		
	def unique_paths_recursive_with_memoization(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		solutions = [[-1 for _ in range(n+1)] for _ in range(m+1)]

		def solve(m, n):
			if solutions[m][n] != -1:
				return solutions[m][n]
			
			if m == 1 or n == 1:
				solutions[m][n] = 1
				return solutions[m][n]
			
			solutions[m][n] = solve(m-1, n) + solve(m, n-1)

			return solutions[m][n]
		
		return solve(m, n)
				

if __name__ == '__main__':
	m1 = 3
	n1 = 7  # output: 28

	m2 = 3
	n2 = 2  # output: 3

	sol = Solution()
	result = sol.unique_paths_iterative(m1, n1)
	print(result)
