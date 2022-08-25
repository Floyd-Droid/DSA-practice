"""
Two sum
LC 1 (easy)

Problem: 
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target. You may assume that each input 
would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Category: 
Array, Hash table

Solution Explanation:
As we iterate through the array, we can insert the values into a hashmap. For 
each iteration, we can check the hashmap for a value which sums with the 
current value to get the target. If there is one, we can append both values' 
indices to the result array. Otherwise, just insert the value into the hashmap 
and move on. This allows a single pass through the array

TC: O(n)
SC: O(n)
"""


class Solution:
	def two_sum(self, nums, target):
		values = {}
		result = []
		
		for i, num in enumerate(nums):
			diff = target - num
			if diff in values:
				result.extend([i, values[diff]])
				del values[diff]
			else:
				values[num] = i

		return result


if __name__ == '__main__':
	numbers1 = [2, 7, 11, 15]
	target1 = 9  # answer is [0, 1]

	numbers2 = [3, 2, 4]
	target2 = 6  # answer is [1, 2]

	numbers3 = [3, 3]
	target3 = 6  # answer is [0, 1]

	sol = Solution()
	result = sol.two_sum(numbers1, target1)
	print(result)
