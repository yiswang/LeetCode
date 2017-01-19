#!/usr/bin/python

###############################################################################
#
# LeetCode 14. Longest Common Prefix
#
# Difficulty: Easy
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
###############################################################################

import pdb

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        longest_common_prefix = ""
        for i in xrange(len(strs[0])):
            j = 0
            flag = True
            for j in xrange(len(strs)-1):
                if not (i < len(strs[j]) and i < len(strs[j+1]) and strs[j][i] == strs[j+1][i]):
                    flag = False
                    break
            if flag == True:
                longest_common_prefix += strs[0][i]
            else:
                break
                
        return longest_common_prefix


if __name__ == "__main__":
    pdb.set_trace()
    strs = [
        "abc",
        "abcd",
        "abcef",
        "abcdef"
    ]
    solu = Solution()
    print solu.longestCommonPrefix(strs)
