#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        reverse-string.py
# Create Date: 2017-03-17
# Usage:       reverse-string.py
# Description:
#
# LeetCode problem 344. Reverse String Add to List
#
# Difficulty: Easy
#
# Write a function that takes a string as input and returns the string
# reversed.
# 
# Example:
# Given s = "hello", return "olleh".
# 
###############################################################################

#
# Method 1.
# Run time on LeetCode: Time Limit Exceeded.
#
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in xrange(len(s)-1, -1, -1):
            res += s[i]
        return res


#
# Method 2.
# Run time on LeetCode: 48ms, beat 81.55%
#
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


#
# Method 3.
# Run time on LeetCode: 86ms, beat 12.37%
#
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        l.reverse()
        return ''.join(l)


if __name__ == "__main__":
    test_cases = [
            "",
            "hello",
            "hello world",
            "hello   world",
    ]
    solu = Solution()
    for n in test_cases:
        res = solu.reverseStrings(n)
        print res
        print ""    
