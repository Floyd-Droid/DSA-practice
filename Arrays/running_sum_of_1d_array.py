"""
Running sum of 1d array
LC 1480 (easy)

Problem: 
Given an array nums. We define a running sum of an array as 
runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Category: 
Array, prefix sum

Solution Explanation:
Use an iterative approach to build an array of solutions from the bottom up.
Each value in the array will be the sum of all nums up to that point. So each 
solution will be the current num plus the previous result. To save space, we 
can perform this operation on the input array since we dont need all previous 
nums, just the previous running sum.

TC: O(n)
SC: O(1)
"""


class Solution:
	def running_sum(self, nums):
		for i in range(1, len(nums)):
			nums[i] = nums[i] + nums[i-1]
		
		return nums


if __name__ == '__main__':
	numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	sol = Solution()
	result = sol.running_sum(numbers1)
	print(result)