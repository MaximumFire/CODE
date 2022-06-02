# input was [3,2,2,3], val = 3
# output was [2, 3, 3]
# expected was [2, 2]
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)