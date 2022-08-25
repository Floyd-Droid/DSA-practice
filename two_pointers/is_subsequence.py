"""
Is subsequence
LC 392 (easy)

Problem: 
Given two strings s and t, return true if s is a subsequence of t, or false 
otherwise. A subsequence of a string is a new string that is formed from the 
original string by deleting some (can be none) of the characters without 
disturbing the relative positions of the remaining characters. (i.e., "ace" 
is a subsequence of "abcde" while "aec" is not).

Category: 
String, Two pointers

Solution Explanation:
Use two pointers; i for string s and j for string t. Increment j for each 
comparison, and whenever a matching letter is found, increment i. By the 
end of the process, if i is equal to the length of s, then we know that we 
found each letter of s within t in order of appearance, meaning that s is a 
subsequence of t.

TC: O(n)
SC: O(1)
"""


class Solution:
	def isSubsequence(self, s, t):
		i = j = 0

		while i < len(s) and j < len(t):
			if s[i] == t[j]:
				i += 1
			j += 1
		
		if i == len(s):
			return True
		
		return False


if __name__ == '__main__':
	s1 = 'abc'
	t1 = 'ahbgdc'

	sol = Solution()
	result = sol.isSubsequence(s1, t1)
	print(result)
