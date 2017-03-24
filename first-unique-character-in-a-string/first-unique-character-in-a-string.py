#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        first-unique-character-in-a-string.py
# Create Date: 2017-03-24
# Usage:       first-unique-character-in-a-string.py
# Description:
#
# LeetCode problem 387. First Unique Character in a String
#
# Difficulty: Easy
#
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
#
# Note: You may assume the string contain only lowercase letters.
# 
###############################################################################

#
# Method 1. Use hashtable. O(n) - Time, O(n) - Space
# Run time on LeetCode: 338ms, beat 29.42%; 318ms, beat 32.74%
#
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        return min([s.find(c) for c, v in collections.Counter(s).iteritems() if v == 1] or [-1])


#
# Method 2. Use set data type and count method of string. O(n) - Time, O(n) - Space
# Run time on LeetCode: 89ms, beat 91.35%; 93ms, beat 93.76%
#
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        return min([s.find(c) for c in set(s) if s.count(c) == 1] or [-1])


#
# Method 3. Use string.ascii_lowercase and count method of string. O(n) - Time, O(n) - Space
# Run time on LeetCode: 125ms, beat 87.61%
#
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import string
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c) == 1] or [-1])


if __name__ == "__main__":
    test_cases = [
            "abab",
            "leetcode",
            "loveleetcode",
    ]
    solu = Solution()
    for s in test_cases:
        print s
        res = solu.firstUniqChar(s)
        print res
        print ""
        
