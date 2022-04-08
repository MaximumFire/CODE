class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        highest = 0
        for i in range(len(nums)):
            temp = 0
            for j in range(len(nums)-i):
                temp = 0
                for k in range(len(nums)-j):
                    pos = j + k
                    temp += nums[pos]
                if temp >= highest:
                    highest = temp
        return highest

s = Solution()

print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))