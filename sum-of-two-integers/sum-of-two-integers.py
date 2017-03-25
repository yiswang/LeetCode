#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        sum-of-two-integers.py
# Create Date: 2017-03-21
# Usage:       sum-of-two-integers.py
# Description:
#
# LeetCode problem 371. Sum of Two Integers Add to List
#
# Difficulty: Easy
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
# 
# Example:
# Given a = 1 and b = 2, return 3.
# 
###############################################################################

#
# Method 1.
# Run time on LeetCode: 36ms, beat 85.51%
#
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff # For 32-bit integer
        res, carry = a, b
        while carry:
            res, carry = (res ^ carry) & mask, ((res & carry) << 1) & mask
        return res if res <= 0x7fffffff else ~(res ^ mask)



if __name__ == "__main__":
    test_cases = [
            (4, -2),
            (2, 3),
            (3, 4),
            (5, 9),
    ]
    solu = Solution()
    for a, b in test_cases:
        res = solu.getSum(a, b)
        print res
        print ""    
