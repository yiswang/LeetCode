#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        isomorphic-strings.py
# Create Date: 2017-02-21
# Usage:       isomorphic-strings.py
# Description:
#
# LeetCode problem 205. Isomorphic Strings Add to List
#
# Difficulty: Easy
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# For example, Given "egg", "add", return true.
# 
# Given "foo", "bar", return false.
# 
# Given "paper", "title", return true.
# 
# Note: You may assume both s and t have the same length.
#
###############################################################################

# Run time on LeetCode: 105ms, beat 23.33%
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        charsMap1 = {}
        charsMap2 = {}
        for c1, c2 in zip(s, t):
            if charsMap1.has_key(c1) and charsMap1[c1] != c2:
                return False
            if charsMap2.has_key(c2) and charsMap2[c2] != c1:
                return False
            charsMap1[c1] = c2
            charsMap2[c2] = c1
        return True
        

# More pythonic methods
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
#         return [s.find(ch) for ch in s] == [t.find(ch) for ch in t]
#         return map(s.find, s) == map(t.find, t)
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))

if __name__ == "__main__":
    test_cases = [
        ("", ""),
        ("a", "a"),
        ("a", "b"),
        ("ab", "ab"),
        ("egg", "add"),
        ("paper", "title"),
        ("foo", "bar"),
        ("ab", "aa"),
    ]
    solu = Solution()
    for s, t in test_cases:
        res = solu.isIsomorphic(s, t)
        print '"%s" "%s" %s' % (s, t, res)
