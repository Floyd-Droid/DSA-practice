"""
Min cost climbing stairs
LC 746 (easy)

Problem: 
You are given an integer array cost where cost[i] is the cost of ith step on a 
staircase. Once you pay the cost, you can either climb one or two steps. You 
can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.


Category: 
Array, dynamic programming

Solution Explanation:
This satisfies the two cases required for dynamic programming:
(1) The optimal solution to the problem is the optimal solution of its 
subproblems.
(2) There are overlapping subproblems

This is similar to the climbing stairs problem, but now we need to consider 
the cost of each step as well.

In the first iterative approach, I keep an array to track the minimum cost 
for each step. The minimum cost for step i is the mimimum between the min cost 
of step i and step i-1. Similarly, the return value is the minimum between the 
last two values of the min_cost array. So for each step of the for loop, we 
always incur the cost of the current step. From there, we know that we either 
took one or two steps to get there. So we add the cost of the current step to 
the mimimum between the minimum cost of the two previous steps.

Another approach is to modify the input array to track the minimum cost in 
order to have constant space complexity. Otherwise, the idea is the same.


TC: O(n) for iterative, O(n) for iterative with modified input
SC: O(n) for iterative, O(1) for iterative with modified input
"""


class Solution:
	def min_cost_iterative(self, cost):
		"""
		:type cost: List[int]
		:rtype: int
		"""
		min_cost = [cost[0], cost[1]]

		for i in range(2, len(cost)):
			min_cost.append(cost[i] + min(min_cost[i-2], min_cost[i-1]))
		
		return min(min_cost[-1], min_cost[-2])
	
	def min_cost_iterative_modify_input(self, cost):
		for i in range(2, len(cost)):
			cost[i] += min(cost[i-1], cost[i-2])
		
		return min(cost[-1], cost[-2])


if __name__ == '__main__':
	cost1 = [10,15,20]  # output: 15
	cost2 = [1,100,1,1,1,100,1,1,100,1]  # output: 6

	sol = Solution()
	result = sol.min_cost_iterative(cost1)
	print(result)
