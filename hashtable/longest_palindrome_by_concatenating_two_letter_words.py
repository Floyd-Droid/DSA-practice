"""
Longest palindrome by concatenating two letter words
LC 2131 (medium)

Problem: 
You are given an array of strings words. Each element of words consists of 
two lowercase English letters. Create the longest possible palindrome by 
selecting some elements from words and concatenating them in any order. Each 
element can be selected at most once. Return the length of the longest 
palindrome that you can create. If it is impossible to create any palindrome, 
return 0. A palindrome is a string that reads the same forward and backward.

Example 1
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Category: 
string, array, hash table

Solution Explanation:
This is very similar to the longest palindrome problem. We create a dictionary 
of words and their frequency in the list. For each key-value pair, word can 
either have two repeating characters, or two non-repeating characters. If the 
characters are repeating, an even numbered count will contribute 2*count 
letters in the palindrome. An odd numbered count can contribute 2*(count-1) 
letters, plus the 2 left over letters, which can take the center of the 
palindrome, so add 2 to the count. This case is represented by the "single" 
variable in the solution. It starts as 0, but when we find an odd numbered 
count, we set it to 2, then add it to the final count once the entire process 
is complete, since only one pair can take the center of the palindrome.

For non-repeating characters, we can reverse the current string and check if 
its in the dictionary. If so, only the smaller count between the two can 
contribute to the longest palindrome. Since we will come across this 
mirrored word later in the iteration, we only multiply the lower count by 
2 instead of 4 (the repetition will make up for it). My first thought 
was to delete the word and its mirror as we go, but you can't change the 
size of the dictionary while iterating, so we'll multiply the lower count 
by 2 instead of 4 to make up for it.

TC: O(n)
SC: O(n)
"""

import collections

class Solution:
	def longest_palindrome(self, words):
		"""
		:type words: List[str]
		:rtype: int
		"""
		counts = collections.Counter(words)
		longest = 0
		single = 0

		for word, count in counts.items():
			if word[0] == word[1]:
				if count % 2 == 0:
					longest += (2 * count)
				if count % 2 == 1:
					longest += (2 * (count - 1))
					single = 2
			else:
				rev_list = list(word)
				rev_list.reverse()
				mirror = "".join(rev_list)

				if mirror in counts:
					smaller_count = min(counts[word], counts[mirror])
					longest += (2 * smaller_count)
		
		return longest + single


if __name__ == '__main__':
	words1 = ["lc","cl","gg"]  # output: 6
	words2 = ["ab","ty","yt","lc","cl","ab"]  # output: 8

	sol = Solution()
	result = sol.longest_palindrome(words2)
	print(result)
