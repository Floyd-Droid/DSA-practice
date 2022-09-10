"""
Search a 2d matrix
LC 74 (medium)

Problem: 
Write an efficient algorithm that searches for a value target in an m x n 
integer matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the 
		previous row.


Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Category: 
binary search, array, matrix

Solution Explanation:
Recursive approach - I wrote two functions, one for finding the list that the 
target value would be contained within, and then another for finding the target 
within that list. We find the middle index of the 2D list and compare the 
target to the first and last items. If the target is less than the first item, 
then the value could be between the current left list and the list right before 
the middle list. If the target is greater than the last item, then the target 
could be anywhere from the list after the current middle array and the right 
array. If the target is between the prviously mentioned values, then it can 
only be found in the current middle array, and we pass that array to the other 
function to search for the target, using a 1D binary search approach similar 
to the 2D approach. If the left value ever exceeds the right value, the target 
is not within the matrix.
This approach has a time complexity of O(log(n) + log(m)) where n is the length of 
the matrix, and m is the length of any array within the matrix.

Iterative approach - This is the same process as the recursive approach, except 
we use while loops to update the left and right values until we find the target


TC: O(log(n) + log(m)) for recursive and iterative
SC: O(log(n) + log(m)) for recursive (if including the call stack), 
		and O(1) for iterative
"""


class Solution:
	def search_matrix_recursive(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""

		def binary_search_2d(matrix, target, left, right):
			if left > right:
				return False

			mid = ((right - left - 1) // 2) + left + 1

			if target < matrix[mid][0]:
				return binary_search_2d(matrix, target, left, mid-1)
			elif target > matrix[mid][-1]:
				return binary_search_2d(matrix, target, mid + 1, right)
			elif matrix[mid][0] <= target <= matrix[mid][-1]:
				return self.binary_search_1d(matrix[mid], target, 0, len(matrix[mid]) - 1)
		
		return binary_search_2d(matrix, target, 0, len(matrix)-1)

	def binary_search_1d_recursive(self, nums, target, left, right):
		if left > right:
			return False

		mid = ((right - left - 1) // 2) + left + 1

		if target < nums[mid]:
			return self.binary_search_1d(nums, target, left, mid - 1)
		elif target > nums[mid]:
			return self.binary_search_1d(nums, target, mid + 1, right)
		elif target == nums[mid]:
			return True
	

	def search_matrix_iterative(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		left = 0
		right = len(matrix) - 1

		while left <= right:
			mid = ((right - left - 1) // 2) + left + 1

			if target < matrix[mid][0]:
				right = mid - 1
			elif target > matrix[mid][-1]:
				left = mid + 1
			elif matrix[mid][0] <= target <= matrix[mid][-1]:
				return self.binary_search_iterative(matrix[mid], target, 0, len(matrix[mid]) - 1)

		return False
	
	def binary_search_1d_iterative(self, nums, target, left, right):
		
		while left <= right:
			mid = ((right - left - 1) // 2) + left + 1

			if target < nums[mid]:
				right = mid - 1
			elif target > nums[mid]:
				left = mid + 1
			elif target == nums[mid]:
				return True
		
		return False


if __name__ == '__main__':

	# Output: true
	matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
	target1 = 3

	# output: False
	matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
	target2 = 13

	# output: False
	matrix3 = [[1]]
	target3 = 0

	sol = Solution()
	result = sol.search_matrix_iterative(matrix1, target1)
	print(result)
