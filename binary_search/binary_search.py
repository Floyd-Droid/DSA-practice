"""
Binary search
LC 704 (easy)

Problem: 
Given an array of integers nums which is sorted in ascending order, and an 
integer target, write a function to search target in nums. If target exists, 
then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Category: 
binary search, array

Solution Explanation:
Both approaches are fairly similar. Find the middle index of the current 
section of the array. If the target is less than the middle value of the 
array, then we know that the value is potentially in the left half of the 
array. In the iterative approach, we simply update the left index (i) to equal 
the mid index value + 1. Otherwise, we update the right index value to be 
mid - 1. In either case, the loop continues until we either find the target 
or the subarray only has 1 item. In the recursive approach, we pass in the left 
and right values recursively, but is otherwise the pretty much the same

TC: O(log(n)) for both approaches
SC: O(1) for iterative, O(log(n)) for recursive (call stack)
"""


class Solution:
	def search_iterative(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		i = 0
		j = len(nums) - 1

		while i <= j:
			# No need to worry about integer overflow in python, but the 
			# below equation is written with that in mind nonetheless
			mid = i + ((j-i) // 2)

			if nums[mid] == target:
				return mid
			if target < nums[mid]:
				j = mid - 1
			else:
				i = mid + 1

		return -1

	def search_recursive(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		left = 0
		right = len(nums)-1

		def solve_recursive(nums, left, right):
			mid = left + ((right-left) // 2)

			if nums[mid] == target:
				return mid
			if len(nums) <= 1:
				return -1
			if target < nums[mid]:
				return solve_recursive(nums, left, mid+1)
			else:
				return solve_recursive(nums, mid+1, right)

		return solve_recursive(nums, left, right)


if __name__ == '__main__':

	nums1 = [-1,0,3,5,9,12]
	target1 = 9  # output: 4

	nums2 = [-1,0,3,5,9,12]
	target2 = 2  # output: -1
	
	sol = Solution()
	result = sol.search_iterative(nums1, target1)
	print(result)
