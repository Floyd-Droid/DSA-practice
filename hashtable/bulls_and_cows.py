"""
Bulls and cows
LC 299 (medium)

Problem: 
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number 
is. When your friend makes a guess, you provide a hint with the following 
info:
    The number of "bulls", which are digits in the guess that are in the correct 
		position.
    The number of "cows", which are digits in the guess that are in your secret 
		number but are located in the wrong position. Specifically, the non-bull 
		digits in the guess that could be rearranged such that they become bulls.

Given the secret number secret and your friend's guess guess, return the hint for 
your friend's guess. The hint should be formatted as "xAyB", where x is the number 
of bulls and y is the number of cows. Note that both secret and guess may contain 
duplicate digits.


Example 1:
Input: secret = "1807", guess = "7810"
Output: "1A3B"


Example 2:
Input: secret = "1122", guess = "1222"
Output: "3A0B"


Example 3:
Input: secret = "1123", guess = "0111"
Output: "1A1B"


Category: 
Array, Hash table

Solution Explanation:

First attempt - I use a list of the numbers in the secret to track which 
numbers can be considered cows or bulls. For each number of the guess, if it 
equals the corresponding number of the secret, we increment bulls. If that 
number is not currently found in the list of secret numbers, then there was 
a point in a previous iteration where we misattributed a cow, so decrement 
cows. Otherwise, we remove the number from the list. If the numbers of secret 
and guess are not equal, yet the number of guess can be found in the list, 
then it is a potential cow, so we increment cows and remove the number.

Solution with hash table - Create a hash table to track the counts for the 
numbers in the secret. Iterate over the guess. If the current number isnt found 
within the count, skip to the next iteration. If the current number matches the 
secret, increment bulls. Otherwise, increment cows. Decrement the count for the 
current number of the guess. If the new count is negative, that means there was 
a previous iteration in which we attributed a number to be a cow, but now we 
know that it isnt, so we decrement cow. Example 2 best illustrates how a 
number can be misattributed as a cow, requiring correction later on.

TC: O(n) for both
SC: O(n) for both
"""

import collections


class Solution:
	def bulls_and_cows_first_attempt(self, secret, guess):
		"""
		:type secret: str
		:type guess: str
		:rtype: str
		"""
		bulls = 0
		cows = 0
		secret_nums = list(secret)

		for ind, num in enumerate(guess):
			
			if num == secret[ind]:
				bulls += 1
				if num not in secret_nums:
					cows -= 1
				else:
					secret_nums.remove(num)
				
			elif num in secret_nums:
				cows += 1
				secret_nums.remove(num)

		result = "{0}A{1}B".format(bulls, cows)
		return result

	def bulls_and_cows_hash_table(self, secret, guess):
		"""
		:type secret: str
		:type guess: str
		:rtype: str
		"""
		bulls = 0
		cows = 0
		secret_count = collections.Counter(secret)

		for i in range(len(guess)):
			if guess[i] not in secret_count:
				continue
			if guess[i] == secret[i]:
				bulls += 1
			elif guess[i] in secret_count:
				cows += 1

			secret_count[guess[i]] -= 1

			if secret_count[guess[i]] < 0:
				cows -= 1
		
		return f"{bulls}A{cows}B"


if __name__ == '__main__':
	secret1 = "1807"
	guess1 = "7810"  # output: "1A3B"

	secret2 = "1122"
	guess2 = "1222"  # output: "3A0B"

	secret3 = "1123"
	guess3 = "0111"  # output: "1A1B"

	secret4 = "1234"
	guess4 = "0111"  # output: "0A1B"

	sol = Solution()
	result = sol.bulls_and_cows_hash_table(secret2, guess2)
	print(result)
