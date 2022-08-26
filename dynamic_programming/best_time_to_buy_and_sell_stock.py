"""
Best time to buy and sell stock
LC 121 (easy)

Problem: 


Category: 
Array, dynamic programming

Solution Explanation:
This satisfies the two cases required for dynamic programming:
(1) The optimal solution to the problem is the optimal solution of its 
subproblems.
(2) There are overlapping subproblems

The below solutions take the bottom-up approach to DP.
Starting at the first day, and moving up. For each day, we record the minimum 
price so far as well as the maximum profit so far. The minimum price is just 
the smallest value in the input array so far. The maximum profit for any 
given day will be the greater value between the current maximum profit, and 
the potential profit of buying on the minimum price day and selling on the 
current day. Repeat the process until you exhaust the input array and return 
the max profit


TC: O(n)
SC: O(1)
"""


class Solution:
	def max_profit_bottom_up_first_attempt(self, prices):
		"""
        :type prices: List[int]
        :rtype: int
        """
		if not prices:
			return 0

		max_profit = [0] * len(prices)
		min_price = prices[0]

		for i in range(1, len(prices)):
			if prices[i] < min_price:
				min_price = prices[i]

			max_profit[i] = max(max_profit[i-1], prices[i] - min_price)

		return max_profit[-1]
	
	def max_profit_bottom_up(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		max_profit = 0
		min_price = float("inf")

		for i in range(1, len(prices)):
			min_price = min(min_price, prices[i])

			max_profit = max(max_profit, prices[i] - min_price)

		return max_profit


if __name__ == '__main__':
	prices1 = [7,1,5,3,6,4]  # output: 5

	sol = Solution()
	result = sol.max_profit_bottom_up(prices1)
	print(result)
