"""
Happy number
LC 202 (easy)

Problem: 
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the 
	squares of its digits. Repeat the process until the number equals 1 (where 
	it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Example 1
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2
Input: n = 2
Output: false

Category: 
hash table, two pointers

Solution Explanation:
We know that the input is a happy number if, for any given sum of squares that 
follows, the result is 1.

Hash table approach - We can continuously sum the squares of each digit in the 
number. For each result, we check if the sum is 1. If so, return True. Otherwise, 
add the sum to the hash table. If we come across a sum that is already within 
the hash table, we know there is a cycle which means we'll never get a sum of 1, 
so return False.
We process each digit in the number, and the number of digits is given by the 
logarithm of the number, so the time complexity is O(log(n))

Two pointer approach - We aren't directly dealing with a linked list, but we can 
treat this problem as if we are, since each number will have a "next" value in 
the sequence. We can use Floyd's cycle detection algorithm to find any cycles. 
This involves using two pointers, one "slow", which advances by 1 step ata time, 
and a "fast" which advances by 2 steps at a time. One step will be finding the 
"next" number in the sequence, which is just the sum of the squares of the 
digits of the current number. So we create a function to find the next number. 
Then create a loop that will find the next for the current value for the slow 
pointer, and the next next value for the fast pointer. If there is a cycle, 
these two pointers will eventually meet (ie, their value will be equal). If 
there is no cycle, then the fast pointer will eventually be 1, and we will 
have cut the time to find it in half.


TC: O(log(n)) for hash table, O(log(n)) for two pointers
SC: O(log(n)) for hash table, O(1) for two pointers
"""


class Solution:
	def is_happy_hash_table(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		current_num = str(n)
		results = {}

		while current_num not in results:
			sum = 0
			for num in current_num:
				sum += int(num) * int(num)

			if sum == 1:
				return True
			
			results[current_num] = sum
			current_num = str(sum)
		
		return False
	

	def is_happy_two_pointers(self, n):
		"""
		:type n: int
		:rtype: bool
		"""

		def get_next(n):
			num = str(n)
			sum = 0
			for digit in num:
				sum += int(digit) * int(digit)
			
			return sum
		
		slow_n = n
		fast_n = get_next(n)

		while slow_n != fast_n and fast_n != 1:
			slow_n = get_next(slow_n)
			fast_n = get_next(get_next(fast_n))
		
		return fast_n == 1


if __name__ == '__main__':
	n1 = 19  # True
	n2 = 2  # False

	sol = Solution()
	result = sol.is_happy_two_pointers(n2)
	print(result)
