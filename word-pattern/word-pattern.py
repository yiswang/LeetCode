#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        word-pattern.py
# Create Date: 2017-02-28
# Usage:       word-pattern.py
# Description:
#
# LeetCode problem 290. Word Pattern Add to List
#
# Difficulty: Easy
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
#
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.
#
###############################################################################

#
# Run time on LeetCode: 49ms, beat 27.98%; 45ms, beat 42.62%
#
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strList = str.split()
        if len(pattern) != len(strList):
            return False
        d = {}
        for i, ch in enumerate(pattern):
            if d.has_key(ch) and d[ch] != strList[i]:
                return False
            else:
                d[ch] = strList[i]
        d = {}
        for i, st in enumerate(strList):
            if d.has_key(st) and d[st] != pattern[i]:
                return False
            else:
                d[st] = pattern[i]
        return True


#
# Run time on LeetCode: 42ms, beat 50.95%; 52ms, beat 20.55%
#
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strList = str.split()
        return len(pattern) == len(strList) and \
            len(set(pattern)) == len(set(strList)) == len(set(zip(pattern, strList)))


#
# Run time on LeetCode: 42ms, beat 50.95%; 52ms, beat 20.55%
#
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strList = str.split()
        return map(pattern.find, pattern) == map(strList.index, strList)


if __name__ == "__main__":
    test_cases = [
        ("abba", "cat dog dog cat"),
        ("abba", "cat dog dog mouse"),
        ("abba", "cat cat cat cat"),
        ("aaaa", "cat cat cat cat"),
    ]
    solu = Solution()
    for pattern, st in test_cases:
        print pattern + "\t" + st
        res = solu.wordPattern(pattern, st)
        print res
        print ""    
