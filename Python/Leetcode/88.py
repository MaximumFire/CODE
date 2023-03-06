# merge sort
class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while 0 in nums1:
            nums1.remove(0)
        while 0 in nums2:
            nums2.remove(0)
        if m == 0 and n >= 1:
            nums1 = nums2
        elif m >= 1 and n == 0:
            pass
        else:
            lists = []
            for i in range(m):
                lists.append([nums1[i]])
            for i in range(n):
                lists.append([nums2[i]])
            while len(lists) != 1:
                
                x = lists[0]
                y = lists[1]

                xpos = 0
                ypos = 0
                result = []
                while len(x) > 0 and len(y) > 0:
                    if x[xpos] < y[ypos]:
                        result.append(x[xpos])
                        x.pop(xpos)
                    elif x[xpos] > y[ypos]:
                        result.append(y[ypos])
                        y.pop(ypos)
                    else:
                        result.append(x[xpos])
                        result.append(y[ypos])
                        x.pop(xpos)
                        y.pop(ypos)
                if len(x) == 0:
                    for val in y:
                        result.append(val)
                elif len(y) == 0:
                    for val in x:
                        result.append(val)

                lists[0] = result
                lists.remove(lists[1])
            nums1 = lists[0]
        return nums1

    def merge_alg(self, x, y):
        xpos = 0
        ypos = 0
        result = []
        while len(x) > 0 and len(y) > 0:
            if x[xpos] < y[ypos]:
                result.append(x[xpos])
                x.pop(xpos)
            elif x[xpos] > y[ypos]:
                result.append(y[ypos])
                y.pop(ypos)
            else:
                result.append(x[xpos])
                result.append(y[ypos])
                x.pop(xpos)
                y.pop(ypos)
        if len(x) == 0:
            for val in y:
                result.append(val)
        elif len(y) == 0:
            for val in x:
                result.append(val)
        return result

c = Solution()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

print(c.merge(nums1=nums1, m=m, nums2=nums2, n=n))
