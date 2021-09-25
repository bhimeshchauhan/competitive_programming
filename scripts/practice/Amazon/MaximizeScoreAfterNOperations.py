"""

Maximize Score After N Operations

You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.

Example 1:

Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1

Example 2:

Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11

Example 3:

Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14

Constraints:

1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 106

"""

def maxScore(self, nums: List[int]) -> int:
	gcd = math.gcd
	n = len(nums)
	if n == 2:
		return gcd(nums[0], nums[1])

	# Store pairs of (GCD(i,j) and mask of 2**i + 2**j)
	gcd_and_mask = []
	for i in range(n):
		first = 1 << i
		for j in range(i + 1, n):
			gcd_and_mask.append([gcd(nums[i], nums[j]), first + (1 << j)])

	# Sort GCD and mask by decreasing GCD size
	gcd_and_mask.sort(key=lambda x: x[0], reverse=True)
	best = 0

	def dfs(pair_array, free_pairs_left, pair_array_index, curr_sum, mask):
		nonlocal best
		if free_pairs_left == 1:
			# If we have used all but 2 elements, find which 2 we need
			need = mask ^ ((1 << n) - 1)
			for x in pair_array[pair_array_index:]:
				if x[1] == need:
					best = max(curr_sum + x[0], best)
					return
			return

		# In the best case scenario, if all GCD values we have left to add are the size of the
		# current largest GCD value we are allowed to take (that value = pair_array[pair_array_index]), our
		# curr_sum can improve by at most value * (1 + 2 + ... + free_pairs_left) = value * max_multiplier
		max_multiplier = (free_pairs_left * (free_pairs_left + 1)) // 2

		for next_index in range(pair_array_index, len(pair_array) - free_pairs_left):
			my_gcd_pair = pair_array[next_index]

			if max_multiplier * my_gcd_pair[0] + curr_sum <= best:  # If we can never beat current best
				return
			if mask & my_gcd_pair[1]:  # If we have already used an element of the pair
				continue
			dfs(pair_array, free_pairs_left - 1, next_index + 1,
				curr_sum + free_pairs_left * my_gcd_pair[0], mask + my_gcd_pair[1])

	# Call DFS starting with n/2 pairs left, going down
	dfs(pair_array=gcd_and_mask, free_pairs_left= n >> 1,
		pair_array_index=0, curr_sum=0, mask=0)

	return best