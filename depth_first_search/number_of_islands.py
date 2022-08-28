"""
Number of islands
LC 200 (medium)

Problem: 
Given an m x n 2D binary grid grid which represents a map of '1's (land) and 
'0's (water), return the number of islands. An island is surrounded by water 
and is formed by connecting adjacent lands horizontally or vertically. You may 
assume all four edges of the grid are all surrounded by water.


Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1


Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Category: 
array, depth first search

Solution Explanation:
Use a nested for loop to iterate over each set of coordinates. For each set, 
skip over it if it is water or if we have already visited it. Otherwise, 
perform a DFS on the coordinate until there is no more island (ie, the stack 
is empty). Increment the number of islands, then move on to the next coordinate 
set in the for loop, once again skipping if it is water or we have already 
visited. Repeat until you have visited all coordinates and return the resulting 
number of islands

TC: O(m*n), for an m x n array
SC: O(m*n)
"""


class Solution:
	def num_islands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		max_i = len(grid) - 1
		max_j = len(grid[0]) - 1
		visited = [[False for _ in range(max_j + 1)] for _ in range(max_i + 1)]

		stack = []

		i_dir = [-1, 1, 0, 0]
		j_dir = [0, 0, -1, 1]

		num_islands = 0

		for i in range(max_i + 1):
			for j in range(max_j + 1):
				if grid[i][j] == '0' or visited[i][j]:
					continue
				
				stack.append((i, j))
				visited[i][j] = True

				while stack:
					x, y = stack.pop()
					
					for n in range(len(i_dir)):
						x2, y2 = x + i_dir[n], y + j_dir[n]
						if 0 <= x2 <= max_i and 0 <= y2 <= max_j:
							if not visited[x2][y2] and grid[x2][y2] == '1':
								stack.append((x2, y2))
								visited[x2][y2] = True
					
				num_islands += 1
		
		return num_islands


if __name__ == '__main__':
	# output: 1
	grid1 = [
		["1","1","1","1","0"],
		["1","1","0","1","0"],
		["1","1","0","0","0"],
		["0","0","0","0","0"]
	]

	# output: 3
	grid2 = [
		["1","1","0","0","0"],
		["1","1","0","0","0"],
		["0","0","1","0","0"],
		["0","0","0","1","1"]
	]

	sol = Solution()
	result = sol.num_islands(grid2)
	print(result)