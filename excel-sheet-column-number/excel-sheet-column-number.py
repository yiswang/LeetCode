#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        excel-sheet-column-number.py
# Create Date: 2017-02-10
# Usage:       excel-sheet-column-number.py
# Description:
#
# LeetCode problem 171. Excel Sheet Column Number
#
# Difficulty: Easy
#
# Related to question Excel Sheet Column Title
# 
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
# 
# For example:
# 
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#
###############################################################################

#
# Method 1. It's like a base 26 number system.
# Run time on LeetCode: 55ms, beat 48.48%
#
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        d = {}
        for i in xrange(26):
            d[letters[i]] = i + 1
        colNum = 0
        n = 0
        for letter in s[::-1]:
            colNum += (26**n) * d[letter.upper()]
            n += 1
        return colNum


#
# Method 2: A pythonic method by using the reduce function.
#
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x, y: x * 26 + y, [ord(c) - ord('A') + 1 for c in s.upper()])

if __name__ == "__main__":
    test_cases = [
        "A",
        "b",
        "Z",
        "AA",
        "AC",
        "AZ",
        "BA",
        "BZ",
        "ZA",
        "ZZ",
        "AAA",
        "AAZ",
        "ADA",
        "ADZ",
        "AZA",
        "AZZ",
        "BAA",
        "BAZ",
        "BBA",
        "ZZY",
        "ZZZ",
        "AAAA",
    ]
    solu = Solution()
    for s in test_cases:
        res = solu.titleToNumber(s)
        print "%s -> %d" % (s, res)
