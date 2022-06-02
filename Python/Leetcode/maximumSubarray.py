# input was [-2,1,-3,4,-1,2,1,-5,4]
# output was 4
# expected was 6

"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array."""

class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum

s = Solution()

print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))