"""
Find all anagrams in a string
LC 438 (medium)

Problem: 
Given two strings s and p, return an array of all the start indices of p's 
anagrams in s. You may return the answer in any order. An Anagram is a word 
or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Category: 
string, two pointers, sliding window, hash table

Solution Explanation:
For my first attempt, I used two pointers. i tracks the start index, while j 
tracks the current letter being considered for the anagram. I convert the 
string p into a list so that each letter of s found to match a letter in the 
anagram can be removed from the list as we go. If the letter at j is not found 
in the anagram, we immediately break and move on to the next start index (i). 
If the letter at j is found in the anagram, we remove that letter from the list 
and increment j to consider the next letter in s. If j extends beyond i plus the 
length of the anagram, we check if there are any letters left in the list. If so, 
we know that this substring isnt an anagram. Otherwise, we add the start index 
to the return array

Another approach is to use two hash tables to track the counts of letters. One 
table keeps a consistent count of the anagram string (p), while the other tracks 
the counts of all substrings of s of length len(p). For each iteration, we 
first compare the counts of p to the results of the previous iteration, and 
add the current index if they are equal. Next, decrement the count for the 
current letter of s, deleting it if the decrement results in 0. Then increment 
the count for the letter which is len(p) steps from the current letter, sliding 
the window forward. Repeatedly slide the window forward and compare the counts 
until i reaches len(s)-len(p).


TC: O(ls*lp) for first attempt, O(ls-lp) for hash table
SC: O(1) for first attempt, O(lp) for hash table
"""

import collections


class Solution:
	def find_anagrams_first_attempt(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: List[int]
		"""
		indices = []
		i = 0

		while i < (len(s) - len(p)):
			j = i
			letters = list(p)
			while j < i + len(p):
				if s[j] in letters:
					letters.remove(s[j])
					j += 1
				else:
					break
			
			if not letters:
				indices.append(i)
			
			i += 1
		
		return indices
			
	def find_anagrams_with_hash_table(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: List[int]
		"""
		p_counts = collections.Counter(p)
		current_counts = collections.Counter(s[:len(p)])
		indices = []
		ls = len(s)
		lp = len(p)

		for i in range(ls - lp + 1):
			if current_counts == p_counts:
				indices.append(i)
			
			if i == ls - lp:
				break

			current_counts[s[i]] -= 1

			# If the decrement results in 0 (as in {'a': 0}), we just delete it.
			# Otherwise, a valid anagram in current_counts wont match p_counts
			if current_counts[s[i]] == 0:
				del current_counts[s[i]]

			current_counts[s[i+lp]] += 1

		return indices
				

if __name__ == '__main__':
	s1 = "cbaebabacd"
	p1 = "abc"  # output: [0, 6]

	s2 = "abab"
	p2 = "ab"  # output: [0, 1, 2]

	sol = Solution()
	result = sol.find_anagrams_with_hash_table(s2, p2)
	print(result)
