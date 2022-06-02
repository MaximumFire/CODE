class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        if xStr == xStr[::-1]:
            return True
        else:
            return False
