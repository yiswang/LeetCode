#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        power-of-four.py
# Create Date: 2017-03-16
# Usage:       power-of-four.py
# Description:
#
# LeetCode problem 326. Power of Four
#
# Difficulty: Easy
#
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
# 
# Example: Given num = 16, return true. Given num = 5, return false.
# 
# Follow up: Could you solve it without loops/recursion?
# 
###############################################################################

#
# Method 1. Do not use loop.
# Run time on LeetCode: 59ms, beat 27.82%; 72ms, beat 10.38%
#
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        return num > 0 and num & (num-1) == 0 and math.log(num, 2) % 2 == 0


#
# Method 2. Do not use loop.
# Run time on LeetCode: 52ms, beat 45.38%; 72ms, beat 10.38%
#
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num & (num-1) == 0 and (num - 1) % 3 == 0


#
# Method 3. Do not use loop.
# Run time on LeetCode: 46ms, beat 73.59%; 68ms, beat 15.26%
#
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num & (num-1) == 0 and (num & 0x55555555) == num


if __name__ == "__main__":
    test_cases = [
            -16, 0, 1, 2, 3, 4, 7, 8, 16
    ]
    solu = Solution()
    for n in test_cases:
        res = solu.isPowerOfFour(n)
        print res
        print ""    
