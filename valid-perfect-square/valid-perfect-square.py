#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        valid-perfect-square.py
# Create Date: 2017-03-21
# Usage:       valid-perfect-square.py
# Description:
#
# LeetCode problem 367. Valid Perfect Square Add to List
#
# Difficulty: Easy
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# Example 1:
# 
# Input: 16
# Returns: True
#
# Example 2:
# 
# Input: 14
# Returns: False
# 
###############################################################################

#
# Method 1. Sequential search. O(sqrt(n)) - Time
# Run time on LeetCode: 46ms, beat 53.10%; 49ms, beat 43.20%
#
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = 1
        while x * x < num:
            x += 1
        return x * x == num


#
# Method 2. Binary search. O(log-2(n)) - Time
# Run time on LeetCode: 32ms, beat 99.20%
#
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low, high = 1, num
        while low <= high:
            mid = (low + high) / 2
            if mid * mid == num:
                return True
            if mid ** mid < num:
                low = mid + 1
            else:
                high = mid - 1
        return False


#
# Method 3. A square number is equal to 1 + 3 + 5 + 7 + ..., O(sqrt(n)) - Time
# Run time on LeetCode: 
#
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        return 0 == num


#
# Method 4. Newton method.
# Run time on LeetCode: 
#
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        while x * x > num:
            x = (x + num/x) >> 1
        return x * x == num


if __name__ == "__main__":
    test_cases = [
            1, 2, 3, 4, 5, 6, 7, 16, 25, 10000,
    ]
    solu = Solution()
    for num in test_cases:
        res = solu.isPerfectSquare(num)
        print res
        print ""    
