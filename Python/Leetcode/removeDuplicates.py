class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            i = 0
            while i < len(nums) - 1:
                if nums[i] == nums[i + 1]:
                    nums.pop(i)
                else:
                    i += 1
            return len(nums)