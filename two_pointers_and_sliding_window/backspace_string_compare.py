"""
Backspace string compare
LC 844 (easy)

Problem: 
Given two strings s and t, return true if they are equal when both are typed 
into empty text editors. '#' means a backspace character. Note that after 
backspacing an empty text, the text will continue empty.


Example 1
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".


Category: 
string, two pointers, stack

Solution Explanation:
With stack - individually go through each string. If the char is a letter, 
append it to a stack. If the char is a '#', pop the last char from the stack. 
If the two stacks are the same at the end of the process, then they will be 
the same in the text editor.

Two pointers approach - Use two pointers (i for string S, j for string T). 
Iterate backwards over both strings simultaneously. We need to find an i and j 
such that they both point to the last letter of their respective strings in 
the editor, then second last, and so on. This means we keep track of the amount 
of backspaces as we go, decrementing it when we pass over a valid letter. Once 
we get to a letter, but the number of backspaces available is 0, then we have 
found a letter that will appear in the final output. We do the same to the other 
pointer/string. We then compare them, and we have three cases:

(1) If i is -1, but j is not, that means we are finished with string S, but 
not string T. In this case, the pointer for T should point to a #, otherwise 
there will be an extra letter in T's final ouptut that won't be found in S's 
final output, so we return False
(2) The inverse case of (1), where j is -1, but i is not. We are finished with 
T but not S, so i should point to a # in S, otherwise return False
(3) If both i and j are not -1, then we simply compare the characters at those 
positions in their respective strings. If they are not equal, return False.

If none of the above cases are met, we continue looping until either the 
above conditions are met, or both pointers sit at -1 (return True).


TC: O(n) for stack, O(n) for two pointers
SC: O(n) for stack, O(1) for two pointers
"""


class Solution:
	def backspace_compare_with_stack(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		s_result = []
		t_result = []

		for s_char in s:
			if s_char == "#":
				s_result.pop()
			else:
				s_result.append(s_char)
		
		for t_char in t:
			if t_char == "#":
				t_result.pop()
			else:
				t_result.append(t_char)
		
		return s_result == t_result
	
	def backspace_compare_with_two_pointers(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		i = len(s) - 1
		j = len(t) - 1

		while i >= 0 or j >= 0:
			backspace_i = 0
			while i >= 0 and (backspace_i > 0 or s[i] == '#'):
				if s[i] == '#':
					backspace_i += 1
				else:
					backspace_i -= 1
				i -= 1
			
			backspace_j = 0
			while j >= 0 and (backspace_j > 0 or t[j] == '#'):
				if t[j] == '#':
					backspace_j += 1
				else:
					backspace_j -= 1
				j -= 1

			if (i < 0 and j >= 0 and t[j] != '#') or \
				(i >= 0 and j < 0 and s[i] != '#') or \
					(i >= 0 and j >= 0 and s[i] != t[j]):
				return False
			
			i -= 1
			j -= 1
		
		return True
			

if __name__ == '__main__':
	s1 = "ab#c"
	t1 = "ad#c"  # True

	s2 = "ab##g"
	t2 = "c#d#gd#"  # True

	s3 = "a#c"
	t3 = "b"  # False

	s4 = "nzp#o#g"
	t4 = "b#nzp#o#g"  # True


	sol = Solution()
	result = sol.backspace_compare_with_two_pointers(s3, t3)
	print(result)
