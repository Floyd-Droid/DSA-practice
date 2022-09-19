"""
Pacific Atlantic water flow
LC 417 (medium)

Problem: 
There is an m x n rectangular island that borders both the Pacific Ocean and 
Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, 
and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an m x n 
integer matrix heights where heights[r][c] represents the height above sea 
level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring 
cells directly north, south, east, and west if the neighboring cell's height 
is less than or equal to the current cell's height. Water can flow from any 
cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes 
that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic 
oceans.


Example 1:
Input: heights = [
	[1,2,2,3,5],
	[3,2,3,4,4],
	[2,4,5,3,1],
	[6,7,1,4,5],
	[5,1,1,2,4]
]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, 
as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the 
Pacific and Atlantic oceans.


Example 2:
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.


Category: 
array, depth first search

Solution Explanation:
We keep two separate sets; one for coordinates in which water flows to the 
atlantic, and one for the pacific. We create a function to perform a 
depth-first-search in all directions from any given coordinate.

When invoking the dfs function, we use two for loops. In the first loop, the 
first call is passed the visited array corresponding to pacific coordinates, 
and the initial coordinates are those of the left border. So we 
start at the left border and make our way rightward until we reach a "wall" 
in the sense that the next coordinate is less than the current value, meaning 
we can't get to the pacific from that coordinate. The next call does the same 
thing, except for the atlantic visited set and the right border as starting 
coordinates. As before, when we reach a coordinate whose value is less then the 
current coordinate, then we can't reach the atlantic from that new coordinate

The next for loop does the same as the previous loop, except the starting 
coordinates are the top and bottom border of the grid

Lastly, we find the intersection of the two sets, which gives us the coordinates 
in which water can flow to both the pacific and atlantic oceans.

TC: O(m*n), for an m x n array
SC: O(m*n)
"""


class Solution:
	def pacific_atlantic(self, heights):
		"""
		:type heights: List[List[int]]
		:rtype: List[List[int]]
		"""
		if not heights[0]:
			return heights

		pacific_visited = set()
		atlantic_visited = set()

		dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

		def dfs(visited, x, y):
			visited.add((x, y))
			for x_dir, y_dir in dir:
				x2, y2 = x + x_dir, y + y_dir

				if 0 <= x2 < len(heights) and 0 <= y2 < len(heights[0]) and (x2, y2) not in visited \
					and heights[x2][y2] >= heights[x][y]:
					dfs(visited, x2, y2)
			
		for i in range(len(heights)):
			dfs(pacific_visited, i, 0)
			dfs(atlantic_visited, i, len(heights[0]) - 1)
		
		for j in range(len(heights[0])):
			dfs(pacific_visited, 0, j)
			dfs(atlantic_visited, len(heights)-1, j)
		
		return list(pacific_visited.intersection(atlantic_visited))


if __name__ == '__main__':
	# output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
	heights1 = [
		[1,2,2,3,5],
		[3,2,3,4,4],
		[2,4,5,3,1],
		[6,7,1,4,5],
		[5,1,1,2,4]
	]

	# output: [[0,0]]
	heights = [[1]]

	sol = Solution()
	result = sol.pacific_atlantic(heights1)
	print(result)
