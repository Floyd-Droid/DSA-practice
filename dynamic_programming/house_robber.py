"""
House Robber
LC 198 (medium)

Problem: 
You are a professional robber planning to rob houses along a street. Each 
has a certain amount of money stashed, the only constraint stopping you 
from robbing each of them is that adjacent houses have security systems 
connected and it will automatically contact the police if two adjacent 
houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the 
police.

Example 1
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


Category: 
Array, dynamic programming

Solution Explanation:
This satisfies the two cases required for dynamic programming:
(1) The optimal solution to the problem is the optimal solution of its 
subproblems.
(2) There are overlapping subproblems

In either recursive or iterative approach, we keep an array to track the 
maximum amount of money that can be robbed from the current set of houses 
being considered. 

In the iterative approach, we work our way up the neighborhood. For any given 
house, we will choose to either rob it, or skip to the next house. If we rob 
the current house, we add the money from the current house to the maximum 
amount of money associated with the house 2 doors back, since we cant rob the 
previous house. If we skip the current house, then the solution will be the 
same as the maximum profit associated with the previous house. We take the 
maximum of these two solutions.

The recursive solution is a similar concept as the iterative, just top-down.


TC: O(n) for both iterative and recursive with memoization
SC: O(n) for both
"""


class Solution:
	def rob_iterative(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return nums

		if len(nums) == 1:
			return nums[0]

		sol = [0 for _ in range(len(nums))]
		sol[0] = nums[0]
		sol[1] = max(nums[0], nums[1])

		for i in range(2, len(nums)):
			sol[i] = max(
				sol[i-2] + nums[i],
				sol[i-1]
			)
		
		return sol[-1]

	def rob_recursive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		sol = [-1 for _ in range(len(nums))]

		def solve(nums, i):
			if i >= len(nums):
				return 0
			
			if sol[i] != -1:
				return sol[i]

			sol[i] = max(
				nums[i] + solve(nums, i+2),
				solve(nums, i+1)
			)

			return sol[i]
		
		return solve(nums, 0)


if __name__ == '__main__':
	# output: 4
	nums1 = [1,2,3,1]

	# output: 12
	nums2 = [2,7,9,3,1]


	sol = Solution()
	result = sol.rob_iterative(nums2)
	print(result)
