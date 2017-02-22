#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        power-of-two.py
# Create Date: 2017-02-22
# Usage:       power-of-two.py
# Description:
#
# LeetCode problem 231. Power of Two Add to List
#
# Difficulty: Easy
#
# Given an integer, write a function to determine if it is a power of two.
# 
###############################################################################

#
# Run time on LeetCode: 58ms, beat 31.79%
#
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n > 1:
            if not n % 2 == 0:
                return False
            n = n / 2
        return True

#
# Using the "n & (n-1)" trick.
# Run time on LeetCode: 46ms, beat 74.61%
#
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n-1)


if __name__ == "__main__":
    test_cases = [
        0,1,2,3,4,5,6,7,8,9,10
    ]

    solu = Solution()
    for num in test_cases:
        print num
        res = solu.isPowerOfTwo(num)
        print res
        print ""


