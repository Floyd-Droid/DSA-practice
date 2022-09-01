"""
Decode string
LC 394 (medium)

Problem: 
Given an encoded string, return its decoded string. The encoding rule is: 
k[encoded_string], where the encoded_string inside the square brackets is 
being repeated exactly k times. Note that k is guaranteed to be a positive 
integer.
You may assume that the input string is always valid; there are no extra 
white spaces, square brackets are well-formed, etc. Furthermore, you may 
assume that the original data does not contain any digits and that digits are 
only for those repeat numbers, k. For example, there will not be input like 3a 
or 2[4].
The test cases are generated so that the length of the output will never exceed 
105.

Example 1
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Category: 
string, stack, recursion

Solution Explanation:
You can use an array as an auxiliary stack or use recursion and the call stack. 
Regardless, for any given char in the input string, there are 4 cases:

(1) char is a number. From here there are 2 subcases. Update the current number 
accordingly. We need to write it such that multi-digit numbers are accounted for, 
in case the current char and prev char are both digits

(2) The char is "[". This is the beginning of the string to be multiplied by 
the preceding number. In the aux stack approach, append the current string 
and current num to the stack, and then reset both values for the next substring. 
In the recursive approach, call the function, passing in the starting position 
of the string. Once you have the resulting substring, multiply the substring 
by the current num and append to the result string

(3) The char is a letter. Include it in the substring to be multiplied.

(4) The char is "]". This marks the end of the current substring. In the aux 
stack approach, pop from the stack, and use the resulting values along with the 
current substring to construct the result string. In the recursive approach, 
return the current current string and the position for the previous caller to 
use to construct the result string.


TC: O(n) for iterative, O(n) for recursive
SC: O(n) for iterative, O(n) for recursive
"""


class Solution:
	def decode_string_recursive(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if not s:
			return ""

		def solve(s, pos):
			current_str = ""
			current_num = 0

			while pos < len(s):
				char = s[pos]
				if char.isdigit():
					current_num = int(current_num)*10 + int(char)
				elif char == "[":
					substr, pos = solve(s, pos + 1)
					current_str += current_num * substr
					current_num = 0
				elif char == "]":
					return current_str, pos
				else:
					current_str += char
				
				pos += 1
			
			return current_str
		
		result = solve(s, 0)

		return result

		
	def decode_string_aux_stack(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		stack = []
		current_str = ""
		current_num = 0

		for char in s:
			if char.isdigit():
				current_num = int(current_num)*10 + int(char)
			elif char == "[":
				stack.append((current_str, current_num))
				current_str = ""
				current_num = 0
			elif char == "]":
				prev_str, prev_num = stack.pop()
				current_str = prev_str + (prev_num * current_str)
			else:
				current_str += char
		
		return current_str


if __name__ == '__main__':
	s1 = "3[a]2[bc]"  # output: "aaabcbc"

	s2 = "3[a2[c]]"  # output: "accaccacc"

	s3 = "2[abc]3[cd]ef"  # output: "abcabccdcdcdef"

	sol = Solution()
	result = sol.decode_string_recursive(s1)
	print(result)
