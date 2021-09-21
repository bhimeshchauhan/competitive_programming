"""

Count pairs with given sum


Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal to ‘sum’.

Examples:  

Input  :  arr[] = {1, 5, 7, -1}, 
          sum = 6
Output :  2
Pairs with sum 6 are (1, 5) and (7, -1)

Input  :  arr[] = {1, 5, 7, -1, 5}, 
          sum = 6
Output :  3
Pairs with sum 6 are (1, 5), (7, -1) &
                     (1, 5)         

Input  :  arr[] = {1, 1, 1, 1}, 
          sum = 2
Output :  6
There are 3! pairs with sum 2.

Input  :  arr[] = {10, 12, 10, 15, -1, 7, 6, 
                   5, 4, 2, 1, 1, 1}, 
          sum = 11
Output :  9
Expected time complexity O(n)

"""

# Python3 implementation of simple method
# to find count of pairs with given sum.

# Returns number of pairs in arr[0..n-1]
# with sum equal to 'sum'


def getPairsCount(arr, n, sum):

	count = 0 # Initialize result

	# Consider all possible pairs
	# and check their sums
	for i in range(0, n):
		for j in range(i + 1, n):
			if arr[i] + arr[j] == sum:
				count += 1

	return count


# Driver function
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is",
	getPairsCount(arr, n, sum))

# This code is contributed by Smitha Dinesh Semwal



# Effecient Solution

# Python implementation of simple method to find count of
# pairs with given sum.

# Returns number of pairs in arr[0..n-1] with sum equal to 'sum'
def getPairsCount(arr, n, sum):
    unordered_map = {}
    count = 0
    for i in range(n):
        if sum - arr[i] in unordered_map:
            count += unordered_map[sum - arr[i]]

        if arr[i] in unordered_map:
            unordered_map[arr[i]] += 1
        else:
            unordered_map[arr[i]] = 1

    return count

# Driver code
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print('Count of pairs is', getPairsCount(arr, n, sum))

# This code is contributed by Manish Thapa
