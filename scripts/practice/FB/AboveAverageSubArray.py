"""

Above-Average Subarrays

You are given an array A containing N integers. Your task is to find all subarrays 
whose average sum is greater than the average sum of the remaining array elements. 
You must return the start and end index of each subarray in sorted order.
A subarray that starts at position L1 and ends at position R1 comes before a subarray 
that starts at L2 and ends at R2 if L1 < L2, or if L1 = L2 and R1 ≤ R2.
Note that we'll define the average sum of an empty array to be 0, and we'll define 
the indicies of the array (for the purpose of output) to be 1 through N. A subarray 
that contains a single element will have L1 = R1.

Signature

Subarray[] aboveAverageSubarrays(int[] A)

Input

1 ≤ N ≤ 2,000
1 ≤ A[i] ≤ 1,000,000

Output

A Subarray is an object with two integer fields, left and right, defining the range that a given subarray covers. Return a list of all above-average subarrays sorted as explained above.

Example 1

A = [3, 4, 2]
output = [[1, 2], [1, 3], [2, 2]]
The above-average subarrays are [3, 4], [3, 4, 2], and [4].


"""


# Python3 implementation of the approach

# Function to return the count of sub-arrays
# such that the average of elements present
# in the sub-array is greater than the
# average of the elements not present
# in the sub-array
def countSubarrays(a, n):
	
	# Initialize the count variable
	count = 0

	# Initialize prefix sum array
	pre = [0 for i in range(n + 1)]

	# Preprocessing prefix sum
	for i in range(1, n + 1):
		pre[i] = pre[i - 1] + a[i - 1]

	for i in range(1, n + 1):
		for j in range(i, n + 1):

			# Calculating sum and count
			# to calculate averages
			sum1 = pre[j] - pre[i - 1]
			count1 = j - i + 1
			sum2 = pre[n] - sum1

			if n-count1 == 0:
				count2 = 1
			else:
				count2 = n - count1

			# Calculating averages
			includ = sum1 // count1
			exclud = sum2 // count2

			# Increment count if including avg
			# is greater than excluding avg
			if (includ > exclud):
				count += 1
		
	return count

# Driver code
arr = [6, 3, 5 ]
n = len(arr)
print(countSubarrays(arr, n))

# This code is contributed by mohit kumar


def aboveAverageSubarrays(A):
  total = sum(A)
  output = []
  for i in range(len(A)):
    for j in range(i,len(A)):
      sub_total = sum(A[i:j+1])
      n = (j-i+1)
      if (total-sub_total)/(len(A)-n if n < len(A) else 1) < sub_total/n:
        output.append([i+1,j+1])
  return output