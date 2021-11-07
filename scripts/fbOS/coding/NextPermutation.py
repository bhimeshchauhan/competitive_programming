"""

Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:

Input: nums = [1]
Output: [1]

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # To find next permutations, we'll start from the end
        i = j = len(nums)-1
        # First we'll find the first non-increasing element starting from the end
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # After completion of the first loop, there will be two cases
        # 1. Our i becomes zero (This will happen if the given array is sorted decreasingly). In this case, we'll simply reverse the sequence and will return
        if i == 0:
            nums.reverse()
            return
        # 2. If it's not zero then we'll find the first number grater then nums[i-1] starting from end
        while nums[j] <= nums[i-1]:
            j -= 1
        # Now out pointer is pointing at two different positions
        # i. first non-assending number from end
        # j. first number greater than nums[i-1]

        # We'll swap these two numbers
        nums[i-1], nums[j] = nums[j], nums[i-1]

        # We'll reverse a sequence strating from i to end
        nums[i:] = nums[len(nums)-1:i-1:-1]
        # We don't need to return anything as we've modified nums in-place


if __name__ == "__main__":
    s = Solution
    print(s.nextPermutation([1, 5, 8, 4, 7, 6, 5, 3, 1]))
