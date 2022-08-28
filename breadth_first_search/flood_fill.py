"""
Flood fill
LC 733 (easy)

Problem: 
An image is represented by an m x n integer grid image where image[i][j] 
represents the pixel value of the image. You are also given three integers 
sr, sc, and color. You should perform a flood fill on the image starting from 
the pixel image[sr][sc]. To perform a flood fill, consider the starting pixel, 
plus any pixels connected 4-directionally to the starting pixel of the same 
color as the starting pixel, plus any pixels connected 4-directionally to 
those pixels (also with the same color), and so on. Replace the color of all 
of the aforementioned pixels with color.
Return the modified image after performing the flood fill.


Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation: From the center of the image with position (sr, sc) = (1, 1) 
(i.e., the red pixel), all pixels connected by a path of the same color as 
the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally 
connected to the starting pixel.


Category: 
Tree, breadth first search

Solution Explanation:
Leetcode lists this as a depth-first-search problem, but to me it seems more 
suited to breadth-first-search. I have both solutions below.

For the BFS approach, it is unnecessary to keep track of which coordinates you 
have already visited, since we only perform the color transformation for 
coordinates which are the same as the start color, which we change as we visit. 
But, this opens up an edge case for when the starting color matches the new 
color. If thats the case, we would repeatedly visit already visited coordinates 
infinitely. So if the start color equals the new color, we just immediately 
return the input image

For the BFS approach, I used direction vectors with a for loop to add each 
node with the start color surrounding the current node to the queue.

For the DFS approach, I recursively call the function for each coordinate set 
surrounding the current node. This approach, unlike the BFS, will require an 
array that tracks which coordinates have been visited. Otherwise, we would 
visit some coordinates multiple times, which may cause the stack to overflow 
for large matrices.

TC: O(n) for both approaches
SC: O(n) for both approaches
"""


class Solution:
	def flood_fill_BFS(self, image, sr, sc, color):
		"""
		:type image: List[List[int]]
		:type sr: int
		:type sc: int
		:type color: int
		:rtype: List[List[int]]
		"""
		start_color = image[sr][sc]

		if start_color == color:
			return image

		queue = [(sr, sc)]

		max_i = len(image) - 1
		max_j= len(image[0]) - 1

		i_dir = [-1, 1, 0, 0]
		j_dir = [0, 0, -1, 1]

		while queue:
			i, j = queue.pop(0)
			image[i][j] = color

			for n in range(len(i_dir)):
				x, y = i + i_dir[n], j + j_dir[n]

				if (0 <= x <= max_i) and (0 <= y <= max_j):
					if image[x][y] == start_color:
						queue.append((x, y))
		
		return image
	
	def flood_fill_DFS_recursive(self, image, sr, sc, newColor):
		"""
		:type image: List[List[int]]
		:type sr: int
		:type sc: int
		:type color: int
		:rtype: List[List[int]]
		"""
		max_i = len(image) - 1
		max_j = len(image[0]) - 1
		color = image[sr][sc]

		visited = [[False for _ in range(max_j + 1)] for _ in range(max_i + 1)]

		if color == newColor: 
			return image
		
		def dfs(i, j):
			visited[i][j] = True

			if image[i][j] == color:
				image[i][j] = newColor
				if i >= 1 and not visited[i-1][j]: 
					dfs(i-1, j)
				if i+1 <= max_i and not visited[i+1][j]: 
					dfs(i+1, j)
				if j >= 1 and not visited[i][j-1]: 
					dfs(i, j-1)
				if j+1 <= max_j and not visited[i][j+1]: 
					dfs(i, j+1)

		dfs(sr, sc)

		return image


if __name__ == '__main__':
	# output: [[2,2,2],[2,2,0],[2,0,1]]
	image1 = [[1,1,1],[1,1,0],[1,0,1]]
	sr1 = 1
	sc1 = 1
	color1 = 2

	# output: [[0,0,0],[0,0,0]], same as input
	image2 = [[0,0,0],[0,0,0]]
	sr2 = 0
	sc2 = 0
	color2 = 0

	sol = Solution()
	result = sol.flood_fill_BFS(image1, sr1, sc1, color1)
	print(result)
