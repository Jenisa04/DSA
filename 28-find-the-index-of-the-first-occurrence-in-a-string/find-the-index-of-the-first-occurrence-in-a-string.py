class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            ptr1 = 0
            ptr2 = 0
            while ptr1 <= len(haystack)-1:
                if haystack[ptr1] == needle[ptr2]:
                    if ptr2 == len(needle)-1:
                        return ptr1 - (len(needle) - 1)
                    ptr1 += 1
                    ptr2 += 1
                else:
                    ptr1 = (ptr1 - ptr2) + 1
                    ptr2 = 0