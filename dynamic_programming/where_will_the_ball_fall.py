"""
Where will the ball fall
LC 1706 (medium)

Problem: 
You have a 2-D grid of size m x n representing a box, and you have n balls. 
The box is open on the top and bottom sides. Each cell in the box has a 
diagonal board spanning two corners of the cell that can redirect a ball to 
the right or to the left.
    A board that redirects the ball to the right spans the top-left corner 
		to the bottom-right corner and is represented in the grid as 1.
    A board that redirects the ball to the left spans the top-right corner 
		to the bottom-left corner and is represented in the grid as -1.

We drop one ball at the top of each column of the box. Each ball can get stuck 
in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped 
pattern between two boards or if a board redirects the ball into either wall 
of the box.
Return an array answer of size n where answer[i] is the column that the ball 
falls out of at the bottom after dropping the ball from the ith column at the 
top, or -1 if the ball gets stuck in the box.

Example 1
Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]

Example 2
Input: grid = [[-1]]
Output: [-1]


Category: 
array, dynamic programming

Solution Explanation:
This satisfies the two cases required for dynamic programming:
(1) The optimal solution to the problem is the optimal solution of its 
subproblems.
(2) There are overlapping subproblems


Depth first search approach - Write a function that takes the current position 
in the matrix and determines which direction the ball will go. There are four 
conditions to consider:
(1) If i reaches the max value of i, then the ball will fall through the bottom, 
so we return the current column value. 

(2) Excluding the leftmost column, we consider the current space and the space 
immediately to the left. If both are -1, then there is a path that leads the 
ball down-left of the current space, so we recursively call the function with 
the coordinates (i+1, j-1)

(3) Excluding the rightmost column, we consider the current space and the space 
immediately to the right. If both are 1, then there is a path that leads the 
ball down-right of the current space, so we recursively call the function with 
the coordinates (i+1, j-1)

(4) If the other conditions don't hold, return -1, indicating the ball will 
get stuck at this point.

TC: O(m*n) for DFS
SC: O(m) for DFS
"""


class Solution:
	def find_ball_DFS(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: List[int]
		"""
		if not grid[0]:
			return []

		m, n = len(grid), len(grid[0])

		result = [-1] * n

		def solve(grid, i, j):
			if i >= m:
				return j
			
			if j - 1 >= 0 and grid[i][j] == grid[i][j-1] == -1:
				return solve(grid, i+1, j-1)
			
			if j + 1 <= n - 1 and grid[i][j] == grid[i][j+1] == 1:
				return solve(grid, i+1, j+1)
			
			return -1

		for j in range(n):
			result[j] = solve(grid, 0, j)

		return result
				

if __name__ == '__main__':
	# ouput: [1,-1,-1,-1,-1]
	grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]

	sol = Solution()
	result = sol.find_ball_DFS(grid)
	print(result)
