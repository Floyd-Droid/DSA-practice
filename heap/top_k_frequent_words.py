"""
Top k frequent words
LC 692 (medium)

Problem: 
Given an array of strings words and an integer k, return the k most frequent 
strings. Return the answer sorted by the frequency from highest to lowest. 
Sort the words with the same frequency by their lexicographical order.

Example 1
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, 
with the number of occurrence being 4, 3, 2 and 1 respectively.


Category: 
heap, hash table, string, trie

Solution Explanation:
To find the k most frequent words, we can organize the input list into a heap, 
then take k elements from the top. We begin by constructing a dictionary of the 
input strings associated with the number of times they appear in the list. Then, 
for each pair, we add the frequency and word as a tuple to a heap, where the 
heap will sort by the frequency, then by the string. Python's heapq is a min 
heap, so we pass in the negative of the frequency so that the largest value is 
on top. We want the words to be sorted lexicographically, so we don't need to 
do anything more in that regard. Once the heap is constructed, we append the top 
k words to the result list and return it.

TC: O(n*log(n))
SC: O(n)
"""

import heapq
import collections

class Solution:
	def top_k_frequent(self, words, k):
		"""
		:type words: List[str]
		:type k: int
		:rtype: List[str]
		"""
		result = []
		heap = []

		counts = collections.Counter(words)

		for word, count in counts.items():
			heapq.heappush(heap, (-count, word))
		
		i = k
		while i > 0:
			result.append(heapq.heappop(heap)[1])
			i -= 1
		
		return result


if __name__ == '__main__':
	words1 = ["i","love","leetcode","i","love","coding"]
	k1 = 2  # output: ["i","love"]
	
	words2 = ["the","day","is","sunny","the","the","the","sunny","is","is"]
	k2 = 4  # output: ["the","is","sunny","day"]
	
	sol = Solution()
	result = sol.top_k_frequent(words2, k2)
	print(result)
