"""
Spiral matrix
LC 54 (medium)

Problem: 
Given an m x n matrix, return all elements of the matrix in spiral order.
Start at the top right of the matrix, move all the way left, down, right, 
up, etc., forming a spiral pattern

Example 1
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Category: 
Array, matrix, simulation

TC: O(n)
SC: O(n)
"""


class Solution:
	def spiral_order(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		max_i = len(matrix) - 1
		max_j = len(matrix[0]) - 1
		min_i = min_j = 0

		result = []
		visited = [[False for _ in range(max_j + 1)] for _ in range(max_i + 1)]

		while not visited[min_i][min_j]:
			for j in range(min_j, max_j + 1):
				if not visited[min_i][j]:
					result.append(matrix[min_i][j])
					visited[min_i][j] = True
			
			min_i += 1
			for i in range(min_i, max_i + 1):
				if not visited[i][max_j]:
					result.append(matrix[i][max_j])
					visited[i][max_j] = True
			
			max_j -= 1
			for j in range(max_j, min_j - 1, -1):
				if not visited[max_i][j]:
					result.append(matrix[max_i][j])
					visited[max_i][j] = True
			
			
			max_i -= 1
			for i in range(max_i, min_i - 1,  -1):
				if not visited[i][min_j]:
					result.append(matrix[i][min_j])
					visited[i][min_j] = True

			min_j += 1

			if min_j > max_j or min_i > max_i:
				break

		return result


if __name__ == '__main__':
	matrix1 = [[1,2,3],[4,5,6],[7,8,9]]  # output: [1,2,3,6,9,8,7,4,5]
	matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]  # output: [1,2,3,4,8,12,11,10,9,5,6,7]
	matrix3 = [[1]]  # output: [1]

	sol = Solution()
	result = sol.spiral_order(matrix3)
	print(result)