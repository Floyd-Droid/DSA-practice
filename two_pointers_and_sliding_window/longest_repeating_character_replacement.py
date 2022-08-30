"""
Longest repeating character replacement
LC 424 (medium)

Problem: 
You are given a string s and an integer k. You can choose any character of the 
string and change it to any other uppercase English character. You can perform 
this operation at most k times.
Return the length of the longest substring containing the same letter you can 
get after performing the above operations.

Example 1
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
Vice versa: Replace the first 'B' with 'A', and you get 'AAAA'


Category: 
string, two pointers, sliding window, hash table

Solution Explanation:
Sliding window approach - Create a counter for the current letters of the 
sliding window. The max_count represents the current maximum count in the 
counter, while the result is the length of the longest substring after k 
transformations.
Begin by building a window starting with the first letter of s. 
Add the letter to the counter, and update the max count if that letter's 
count exceeds the current max count. If the difference between the current 
length of the longest substring and the current highest count in the counter 
exceeds or equals k, then we cannot make any more transformations given the 
current starting position in the string, so we decrement that starting letter's 
count to shift the left of the window forward one letter. Otherwise, we can 
make a transformation, and therefore increment the result. For the next 
iteration, we expand the window rightward one letter and repeat the process.


TC: O(n)
SC: O(1)
"""

import collections


class Solution:
	def character_replacement_sliding_window(self, s, k):
		"""
		:type s: str
		:type k: int
		:rtype: int
		"""
		max_count = 0
		result = 0
		counts = collections.Counter()

		for i in range(len(s)):
			counts[s[i]] += 1
			max_count = max(
				max_count,
				counts[s[i]]
			)

			if result - max_count >= k:
				counts[s[i-result]] -= 1
			else:
				result += 1
		
		return result


if __name__ == '__main__':
	s1 = "ABAB"
	k1 = 2  # output: 4

	s2 = "AABABBA"  
	k2 = 1  # output: 4

	sol = Solution()
	result = sol.character_replacement_sliding_window(s1, k1)
	print(result)
