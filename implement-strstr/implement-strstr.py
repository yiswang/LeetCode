#!/usr/bin/python

###############################################################################
#
# LeetCode question 28. Implement strStr()
#
# Difficulty: Easy
#
# Returns the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
###############################################################################

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        len_haystack = len(haystack)
        len_needle = len(needle)
        cur_begin_index = 0
        while cur_begin_index < len_haystack:
            i = cur_begin_index
            j = 0
            while i < len_haystack and j < len_needle:
                if haystack[i] != needle[j]:
                    break
                i += 1
                j += 1
            if j == len_needle:
                return i - len_needle
            elif cur_begin_index + len_needle >= len_haystack:
                return -1
            else:
                cur_begin_index += 1
        return -1


if __name__ == "__main__":
    test_cases = [
        ("", ""),
        ("", "P"),
        ("P", ""),
        ("P", "P"),
        ("PA", "PA"),
        ("AP", "PA"),
        ("APPALIPALISHIRINGNG", "PALI"),
        ("APPAYPALISHIRINGNG", "PALI"),
        ("APPAYPALOSHIRINGNG", "PALI"),
        ("aaaaaab", "aaaaab"),
        ("aaaaaa", "aaaaab"),
    ]
    solu = Solution()
    for s1, s2 in test_cases:
        res = solu.strStr(s1, s2)
        print res


