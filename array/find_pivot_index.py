"""
Find pivot index
LC 724 (easy)

Problem: 
Given an array of integers nums, calculate the pivot index of this array. The 
pivot index is the index where the sum of all the numbers strictly to the 
left of the index is equal to the sum of all the numbers strictly to the 
index's right.If the index is on the left edge of the array, then the left 
sum is 0 because there are no elements to the left. This also applies to the 
right edge of the array.Return the leftmost pivot index. If no such index 
exists, return -1.

Category: 
Array, prefix sum

Solution Explanation:
For any given position in the input array, we need to know the sum of all 
values to the left, and the sum of all values to the right. When finding 
pivot index, we can pass through the array once. Start with a left sum of 0, 
and a total sum of all numbers in the array. Then, for each value, check the 
left sum against the right sum, which will be the total minus the left sum 
minus the current value. If equal, then we have found the pivot index.

TC: O(n)
SC: O(1)
"""


class Solution:
	def find_pivot(self, nums):
		"""
        :type nums: List[int]
        :rtype: int
        """
		left_sum = 0
		total = sum(nums)

		for i, num in enumerate(nums):
			if left_sum == (total - left_sum - num):
				return i

			left_sum += num
		
		return -1


if __name__ == '__main__':
	numbers1 = [1,7,3,6,5,6]  # output: 3

	sol = Solution()
	result = sol.find_pivot(numbers1)
	print(result)