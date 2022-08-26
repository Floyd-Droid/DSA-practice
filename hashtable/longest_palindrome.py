"""
Longest palindrome
LC 409 (easy)

Problem: 
Given a string s which consists of lowercase or uppercase letters, return the 
length of the longest palindrome that can be built with those letters. Letters 
are case sensitive, for example, "Aa" is not considered a palindrome here.

Category: 
string, hash table

Solution Explanation:
Get a count for each letter in the string. You can use the Counter() object 
to quickly get the counts. For each count, there are two cases:
(1) The count is even. All letters in this count can contribute to 
the palindrome, so add the count to the result
(2) If the count is odd, then all letters can contribute to the palindrome, 
but only one letter out of all letters can be at the center of an odd- 
length palindrome. So add count to the result, but make sure no future 
odd counts are considered for the center letter of the palindrome.

TC: O(n)
SC: O(n)
"""

import collections

class Solution:
	def longest_palindrome(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		counts = collections.Counter(s)
		length = 0
		single = 0

		for count in counts.values():
			if count % 2 == 0:
				length += count
			elif (count - 1) % 2 == 0:
				length += (count - 1)
				single = 1
			
		return length + single
	
	def longest_palindrome_first_attempt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		totals = {}
		for letter in s:
			if not letter in totals:
				totals[letter] = 1
			else:
				totals[letter] += 1

		length = 0
		single = 0
		for value in totals.values():
			if value % 2 == 0:
				length += value
			elif value % 2 == 1:
				length += (value - 1)
				single = 1

		length += single

		return length


if __name__ == '__main__':
	s1 = "abccccdd"  # output: 7
	s2 = "a"  # output: 1

	sol = Solution()
	result = sol.longest_palindrome(s1)
	print(result)
