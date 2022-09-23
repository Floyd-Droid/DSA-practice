"""
Coin change
LC 322 (medium)

Problem: 
You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If 
that amount of money cannot be made up by any combination of the coins, return 
-1. You may assume that you have an infinite number of each kind of coin.

Example 1
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2
Input: coins = [2], amount = 3
Output: -1

Example 3
Input: coins = [1], amount = 0
Output: 0


Category: 
Array, dynamic programming

Solution Explanation:
This satisfies the two cases required for dynamic programming:
(1) The optimal solution to the problem is the optimal solution of its 
subproblems.
(2) There are overlapping subproblems

Working from the bottom up, we create a solutions array whose length is equal 
to the target amount. We initialize each value of the array to be the target 
value plus 1 as a max value. For each intermediate value between 0 and the 
target, we want to find the smallest number of coins to reach that value. So 
for each value, we go through each coin and find the difference between the current 
value and coin. If the difference is positive, then we can potentially get to 
the target value by using the solution of the difference. We take the min between 
the current solution of the current value and the solution of the difference plus 
one (we add one to account for the coin currently being considered). We do this for 
each coin until the smallest value is found and increment to the next value towards 
the target.
At the end, we only return that target value's solution if it doesnt equal the 
initial solution. If it does, that means that there are no combination of coins 
that can reach the target value.

TC: O(n*k) [n=target, k=number of coins]
SC: O(n)
"""


class Solution:
	def coin_change(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""

		init = amount + 1
		sol = [init for _ in range(amount + 1)]
		sol[0] = 0

		for i in range(1, amount + 1):
			for coin in coins:
				diff = i - coin
				if diff >= 0:
					sol[i] = min(
						sol[i], 
						sol[diff] + 1
					)

		return sol[-1] if sol[-1] != init else -1


if __name__ == '__main__':
	# output: 3
	coins1 = [1,2,5]
	amount1 = 11

	# output: -1
	coins2 = [2]
	amount2 = 3

	# output: 0
	coins3 = [1]
	amount3 = 0


	sol = Solution()
	result = sol.coin_change(coins2, amount2)
	print(result)
