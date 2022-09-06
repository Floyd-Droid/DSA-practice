"""
Task scheduler
LC 621 (medium)

Problem: 
Given a characters array tasks, representing the tasks a CPU needs to do, 
where each letter represents a different task. Tasks could be done in any 
order. Each task is done in one unit of time. For each unit of time, the 
CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown 
period between two same tasks (the same letter in the array), that is that 
there must be at least n units of time between any two same tasks.
Return the least number of units of times that the CPU will take to finish 
all the given tasks.

Example 1
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.


Category: 
array, hash table, greedy

Solution Explanation:
We know that the minimum number of units of time will be the number of tasks 
plus the number of idle times, so we just need to find out the number of idle 
times. The total number of idle times will start out at its maximum value, which 
is the frequency of the most frequent task minus 1, multiplied by n. For each 
other type of task, we update the total by subtracting the minimum between 
the maximum number of idle counts and the frequency of the current task.
If the total goes below 0, we just return the lenth of the input.

TC: O(n)
SC: O(n)
"""

import collections

class Solution:
	def least_interval(self, tasks, n):
		"""
		:type tasks: List[str]
		:type n: int
		:rtype: int
		"""
		task_counts = collections.Counter(tasks)
		counts = sorted(task_counts.values())

		max_idle = counts.pop()
		total = (max_idle - 1) * n

		while counts and max_idle > 0:
			total -= min(max_idle - 1, counts.pop())
		
		return max(0, total) + len(tasks)


if __name__ == '__main__':
	# output: 8
	tasks1 = ["A","A","A","B","B","B"]
	n1 = 2

	# output: 16
	tasks2 = ["A","A","A","A","A","A","B","C","D","E","F","G"]
	n2 = 2

	# output: 8 (no idle time)
	tasks3 = ["A","A","A","B","B","B","C","C"]
	n3 = 2

	sol = Solution()
	result = sol.least_interval(tasks1, n1)
	print(result)
