"""
Search in a rotated sorted array
LC 33 (medium)

Problem: 
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown 
pivot index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become 
[4,5,6,7,0,1,2]. Given the array nums after the possible rotation and an integer 
target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Category: 
binary search, array

Solution Explanation:
Perform a binary search. Even if rotated, one of the halves of the array will 
be sorted. We can check which half is sorted and see if the target lies between 
first and last value in the subarray. If so, we focus our search on that subarray. 
Otherwise, we focus on the other half. Repeat the process until the target is 
found or the left value equals or exceeds the right value.


TC: O(log(n))
SC: O(1)
"""


class Solution:
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		left = 0
		right = len(nums) - 1

		while left <= right:
			
			mid = ((left + right - 1) // 2) + 1

			if target == nums[mid]:
				return mid
			
			if nums[left] < nums[mid]:
				if nums[left] <= target < nums[mid]:
					right = mid - 1
				else:
					left = mid + 1
			
			else:
				if nums[mid] < target <= nums[right]:
					left = mid + 1
				else:
					right = mid - 1
		
		return -1


if __name__ == '__main__':

	# Output: 4
	nums1 = [4,5,6,7,0,1,2]
	target1 = 0

	# output: -1
	nums2 = [4,5,6,7,0,1,2]
	target2 = 3

	# output: -1
	nums3 = [1]
	target3 = 0

	# output: 1
	nums4 = [3, 1]
	target4 = 3

	sol = Solution()
	result = sol.search(nums4, target4)
	print(result)
