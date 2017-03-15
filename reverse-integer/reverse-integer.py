#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        reverse-integer.py
# Create Date: 2017-02-26
# Usage:       reverse-integer.py
# Description:
#
# LeetCode problem 7. Reverse Integer
# 
#     Difficulty: Easy
# 
# Reverse digits of an integer.
# 
# Example1: x = 123, return 321
# Example2: x = -123, return -321 
#
###############################################################################

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if -10 < x and x < 10:
            return x

        if x >= 0:
            factor = 1
        else:
            factor = -1
            x = -x

        MAXSIZE = 2 ** 31 - 1
        x2 = 0
        while x > 0:
            d = x % 10
            x = x / 10
            if factor == 1 and (MAXSIZE - d) / 10 < x2:
                return 0
            if factor == -1 and (MAXSIZE + 1 - d) / 10 < x2:
                return 0
            x2 = x2 * 10 + d

        return x2 * factor


if __name__ == "__main__":
    pass
