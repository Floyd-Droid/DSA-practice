"""
First bad version
LC 278 (easy)

Problem: 
You are a product manager and currently leading a team to develop a new 
product. Unfortunately, the latest version of your product fails the quality 
check. Since each version is developed based on the previous version, all the 
versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first 
bad one, which causes all the following ones to be bad. You are given an API 
bool isBadVersion(version) which returns whether version is bad. Implement a 
function to find the first bad version. You should minimize the number of 
calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Category: 
binary search

Solution Explanation:
The brute force approach would be to start at the most recent version, and 
keep checking if its bad, decrementing each time until you find a good version. 
However, that would give a linear time complexity, and we can do better.

We can implement a binary search. Take the current version, and cut it in half. 
Check if its bad. If it is, then we know that the first bad version is either 
the current version, or a version that comes before it. If its not bad, the 
first bad version must come after it. Either way, we get new parameters to 
focus the search. 

TC: O(log(n))
SC: O(1)
"""

# Leetcode defines the isBadVersion API, which returns a bool determining if 
# the passed in version is bad or not

def is_bad_version(version):
	bad_version = 20
	return version >= bad_version


class Solution:
	def first_bad_version(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		i = 1
		j = n

		while i < j:
			mid = i + ((j-i) // 2)
			is_bad = is_bad_version(mid)

			if is_bad:
				j = mid
			else:
				i = mid + 1
		
		return i


if __name__ == '__main__':

	version = 45

	sol = Solution()
	result = sol.first_bad_version(version)
	print(result)
