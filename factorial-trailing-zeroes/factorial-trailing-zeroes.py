#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        factorial-trailing-zeroes.py
# Create Date: 2017-02-15
# Usage:       factorial-trailing-zeroes.py
# Description:
#
# LeetCode problem 172. Factorial Trailing Zeroes
#
# Difficulty: Easy
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Note: Your solution should be in logarithmic time complexity.
#
###############################################################################

#
# Run time on LeetCode: 35ms. Beats 99.19%
#
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n = n / 5
            count += n
        return count

if __name__ == "__main__":
    test_cases = [1, 4, 5, 6, 9, 10, 16, 25, 26, 49, 50, 51, 74, 75]

    solu = Solution()
    for n in test_cases:
        print solu.trailingZeroes(n)
    print ""
