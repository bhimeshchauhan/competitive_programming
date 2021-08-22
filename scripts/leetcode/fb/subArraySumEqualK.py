"""

Given an array of integers nums and an integer k, 
return the total number of continuous subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

"""
class Solution:
    def subarraySum(self, nums, k):
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
        
        return(count)
    
if __name__ == "__main__":
    nums = [1,2,1,3]
    k = 3
    print(Solution().subarraySum(nums, k))    

