"""
Longest common prefix
LC 14 (easy)

Problem: 
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Category: 
array, string

Solution Explanation:
Begin with the first word in the list as the longest common prefix. For every 
other word in the list, compare each letter of the current longest prefix with 
the corresponding letter in the current word unsing index i, up until either 
the last character of the shorter word, or until the letters arent equal. 
Then slice the current word up to the index and set it as the longest prefix 
so far.

TC: O(n*m) [n = length of list, m = length of shortest word]
SC: O(1)
"""


class Solution:
	def longest_common_prefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if not strs:
			return ""
		
		longest = strs[0]

		for s in range(1, len(strs)):
			i = 0
			word = strs[s]

			while i < len(word) and i < len(longest) and longest[i] == word[i]:
				i += 1
			
			longest = word[:i]
		
		return longest


if __name__ == '__main__':
	strs1 = ["flower","flow","flight"]  # output: "fl"
	strs2 = ["dog","racecar","car"]  # output: ""

	sol = Solution()
	result = sol.longest_common_prefix(strs1)
	print(result)
