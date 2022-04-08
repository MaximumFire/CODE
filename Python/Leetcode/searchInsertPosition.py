class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            if target == nums[0]:
                return 0
            elif target < nums[0]:
                return 0
            else:
                return 1
        elif len(nums) == 2:
            if (target < nums[1]) and (nums[0] < target):
                return 1
        j = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if i == 0:
                if target < nums[i]:
                    j = i
            elif i == len(nums) - 1:
                if nums[len(nums)-1] < target:
                    j = len(nums)
                else:
                    if nums[i-1] < target < nums[i]:
                        j = i
            else:
                if nums[i-1] < target < nums[i]:
                    j = i
        return j

s = Solution()

print(s.searchInsert([1,3,5], 4))