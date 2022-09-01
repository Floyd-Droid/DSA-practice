"""
Last stone weight
LC 1046 (easy)

Problem: 
You are given an array of integers stones where stones[i] is the weight of the 
ith stone. We are playing a game with the stones. On each turn, we choose the 
heaviest two stones and smash them together. Suppose the heaviest two stones 
have weights x and y with x <= y. The result of this smash is:

    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y 
		has new weight y - x.

At the end of the game, there is at most one stone left. Return the weight of 
the last remaining stone. If there are no stones left, return 0.

Example 1
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2
Input: stones = [1]
Output: 1


Category: 
array, heap

Solution Explanation:
First attempt - We used the max() function on the input list to grab the two 
largest values while removing them from the list. If they are not equal, we 
take the difference and then append to the list. Repeat until there is 1 or 0 
items in the list.

Heap approach - Construct a heap from the input list. Since heapq is a min heap, 
add the negative of each stone weight as you go. Then use a loop to repeatedly 
take the "top" 2 values from the heap and compare just as in the other approach, 
taking care to consider the negative values. If not equal, add the difference 
to the heap and move on. It takes O(log(n)) time to insert a value into the heap 
and we do so for each item in the list, for a time complexity of
O(n*log(n))
It takes O(1) time to grab the max/min value

TC: O(n*log(n)) for list approach, O(n*log(n)) for heap
SC: O(1) for list approach, O(n) for heap
"""

import heapq


class Solution:
	def last_stone_weight_list(self, stones):
		"""
		:type stones: List[int]
		:rtype: int
		"""
		while len(stones) > 1:
			y = stones.pop(stones.index(max(stones)))
			x = stones.pop(stones.index(max(stones)))
			
			if x != y:
				y -= x
				stones.append(y)
        
		return stones[0] if stones else 0
	
	def last_stone_weight_heap(self, stones):
		"""
		:type stones: List[int]
		:rtype: int
		"""
		heap = []
		for stone in stones:
			heapq.heappush(heap, -stone)
		
		while len(heap) >= 2:
			y = heapq.heappop(heap)
			x = heapq.heappop(heap)

			if x != y:
				heapq.heappush(heap, (y-x))
		
		return -heap[-1] if heap else 0



if __name__ == '__main__':
	stones1 = [2,7,4,1,8,1]  # output: 1
	stones2 = [1]  #output: 1
	
	sol = Solution()
	result = sol.last_stone_weight_heap(stones1)
	print(result)
