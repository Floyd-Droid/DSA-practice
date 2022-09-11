"""
Rotting oranges
LC 994 (medium)

Problem: 
You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten 
orange becomes rotten. Return the minimum number of minutes that must elapse 
until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never 
rotten, because rotting only happens 4-directionally.

Example 3
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Category: 
Matrix, breadth first search

Solution Explanation:
We begin by going through the matrix and appending all rotten orange 
coordinates to a list and all fresh orange coordinates to a set. We 
then construct a queue (list) which will consist of lists of coordinates of 
rotten oranges to be considered. Each coordinate list in this queue corresponds 
to one minute in which the surrounding oranges are made rotten. We add the first 
set of rotten coordinates to the queue.

We go through the first set of rotten coordinates. For each coordinate, we 
use i and j direction vectors to consider each direction from the current 
coordinate (up, down, left, and right respectively). If each direction is within 
the bounds of the matrix and fresh, we remove that fresh coordinate from the 
fresh set and add the coordinates to a new list. Once all coordinates of the 
current set are dealt with, we check if there are any new coordinates to be 
considered. If so, we add a minute and append the new coordinates to the queue. 
Lastly, after the queue is empty, we check if there are any fresh orange 
coordinates left in the set. If so, then there is at least one orange which 
cant be made rotten (can't be reached), so return -1.


TC: O(mn)
SC: O(mn)
"""


class Solution:
	def oranges_rotting(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		
		fresh = set()

		i_dir = [-1, 1, 0, 0]
		j_dir = [0, 0, -1, 1]
		minutes = 0

		first_rotten = []
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == 2:
					first_rotten.append((i, j))
				if grid[i][j] == 1:
					fresh.add((i, j))
		
		rotten_queue = [first_rotten]
		
		while rotten_queue:
			coords = rotten_queue.pop(0)
			new_coords = []

			while coords:
				i, j = coords.pop(0)

				for d in range(len(i_dir)):
					x, y = i + i_dir[d], j + j_dir[d]

					if 0 <= x< len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
						grid[x][y] = 2
						fresh.remove((x, y))
						new_coords.append((x, y))
				
			if new_coords:
				minutes += 1
				rotten_queue.append(new_coords)

		return minutes if not fresh else -1


if __name__ == '__main__':
	grid1 = [[2,1,1],[1,1,0],[0,1,1]]  # output: 4

	grid2 = [[2,1,1],[0,1,1],[1,0,1]]  # output: -1

	grid = [[0,2]]  # output: 0

	sol = Solution()
	result = sol.oranges_rotting(grid1)
	print(result)