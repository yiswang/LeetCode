#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        excel-sheet-column-title.py
# Create Date: 2017-02-09
# Usage:       excel-sheet-column-title.py
# Description:
#
# LeetCode problem 168. Excel Sheet Column Title
#
# Difficulty: Easy
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
#
###############################################################################

#
# Run time on LeetCode: 35ms, beat 86.31%
#
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        baseAlphabet = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
        title = ""
        while n > 0:
            x = n % 26
            n = n / 26 if x != 0 else n / 26 - 1
            title = baseAlphabet[x] + title
        return title

        
if __name__ == "__main__":
    test_cases = range(26*28)
    solu = Solution()
    for n in test_cases:
        res = solu.convertToTitle(n)
        print "%d -> %s" % (n, res)
