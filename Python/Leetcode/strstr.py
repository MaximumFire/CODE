class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if needle in haystack:
            for i in range(len(haystack)):
                try:
                    if haystack[i] == needle[0]:
                        valid = False
                        for j in range(len(needle)):
                            if haystack[i+j] == needle[j]:
                                valid = True
                            else:
                                valid = False
                                break
                        if valid:
                            return i
                except IndexError:
                    return -1
        else:
            return -1


s = Solution()

print(s.strStr("mississippi", "sipp"))