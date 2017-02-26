#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        add-digits.py
# Create Date: 2017-02-26
# Usage:       add-digits.py
# Description:
#
# LeetCode problem 258. Add Digits
# 
# Difficulty: Easy
# 
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit.
# 
# For example:
# 
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only
# one digit, return it.
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime? 
# 
###############################################################################

#
# Method 1. Use loop. O(n)-time
# Run time on LeetCode: 49ms, 60.42%
#
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            x = num % 10
            num = num / 10 + x
        return num


#
# Method 2. This problem is known as digit root problem which has a congruence
# formula to solve it.
# Run time on LeetCode: 49ms, 60.42%; 45ms, 83.01%
#
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 0 if num == 0 else (num - 1) % 9 + 1


if __name__ == "__main__":
    test_cases = [
        0, 1, 10, 179,
    ]
    solu = Solution()
    for num in test_cases:
        res = solu.addDigits(num)
        print num, res
