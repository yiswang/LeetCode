#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        valid-anagram.py
# Create Date: 2017-02-24
# Usage:       valid-anagram.py
# Description:
#
# LeetCode problem 242. Valid Anagram Add to List
#
# Difficulty: Easy
#
# Given two strings s and t, write a function to determine if t is an anagram
# of s.
# 
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
#
###############################################################################

#
# Method 1.
# Run time on LeetCode: 125ms, beat 14.84%; 85ms, beat 68.33%
#
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = {}, {}
        for c in s:
            d1[c] = d1.get(c, 0) + 1
        for c in t:
            d2[c] = d2.get(c, 0) + 1
        return d1 == d2


#
# Method 2.
# Run time on LeetCode: 106ms, beat 33.02%; 136ms, beat 10.38%
#
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

#
# Method 3.
# Run time on LeetCode: 65ms, beat 89.85%; 86ms, beat 67.27%
#
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        for c in t:
            counts[ord(c) - ord('a')] -= 1
        for count in counts:
            if count != 0:
                return False
        return True
        
        

if __name__ == "__main__":
    test_cases = [
        ("naba", "naab"),
        ("naaba", "naab"),
    ]
    solu = Solution()
    for s, t in test_cases:
        print s, t
        res = solu.isAnagram(s, t)
        print res
        print ""    
