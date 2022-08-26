"""
Isomorphic strings
LC 205 (easy)

Problem: 
Given two strings s and t, determine if they are isomorphic.Two strings s and 
t are isomorphic if the characters in s can be replaced to get t. All 
occurrences of a character must be replaced with another character while 
preserving the order of characters. No two characters may map to the same 
character, but a character may map to itself.

Category: 
String, Hash table

Solution Explanation:
Keep two hash tables to map char1 (of s) and char2 (of t) to each other in 
both directions. Then, as we go through both strings, consider the 
following cases:
(1) A relation between char1 and char2 does not exist in either map. Add the 
relationships to both maps and move on.
(2) A relationship exists between char1 and char2 in one map, but not the other
(3) A relationship is found in both maps, but they do not match each other

TC: O(n)
SC: O(1)
"""


class Solution:
	def is_isomorphic(self, s, t):
		"""
        :type s: str
        :type t: str
        :rtype: bool
        """
		map_s_t = {}
		map_t_s = {}

		for char1, char2 in zip(s, t):
			# Case 1: Neither maps contain the association
			if (char1 not in map_s_t) and (char2 not in map_t_s):
				map_s_t[char1] = char2
				map_t_s[char2] = char1
			
			# Case 2: Mapping does not exist in one map but does the other
			# Case 3: The mappings exist in both, but they do not match
			elif (map_s_t.get(char1) != char2) or (map_t_s.get(char2) != char1):
				return False
		
		return True
	
	def is_isomorphic_first_attempt(self, s, t):
		"""
        :type s: str
        :type t: str
        :rtype: bool
        """
		map = {}

		# Strings are guaranteed equal length
		for i in range(len(s)):
			if not s[i] in map:
				if t[i] in map.values():
					return False
				map[s[i]] = t[i]
			else:
				if map[s[i]] != t[i]:
					return False

		return True


if __name__ == '__main__':
	s1 = 'egg'
	t1 = 'add'  # output: True

	s2 = 'paper'
	t2 = 'title'  # output: True

	sol = Solution()
	result = sol.is_isomorphic(s2, t2)
	print(result)
