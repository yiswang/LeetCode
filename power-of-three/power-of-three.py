#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        power-of-three.py
# Create Date: 2017-03-15
# Usage:       power-of-three.py
# Description:
#
# LeetCode problem 326. Power of Three
#
# Difficulty: Easy
#
# Given an integer, write a function to determine if it is a power of three.
# 
# Follow up:
# Could you do it without using any loop / recursion?
# 
###############################################################################

#
# Method 1: Use loop.
# Run time on LeetCode: 185ms, beat 95.97%; 192ms, beat 89.73%
#
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n / 3
        return n == 1


#
# Method 2: Do not use loop.
# Run time on LeetCode: 308ms, beat 12.84%; 175ms, 96.63%
#
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        M = 1162261467 # 1162261467 is the biggest power of 3 that fits into 32 bits.
        return n > 0 and M % n == 0



if __name__ == "__main__":
    test_cases = [
            -27, -3, 0, 1, 2, 3, 4, 9, 10, 27
    ]
    solu = Solution()
    for n in test_cases:
        res = solu.isPowerOfThree(n)
        print res
        print ""    
