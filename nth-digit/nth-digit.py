#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        nth-digit.py
# Create Date: 2017-03-26
# Usage:       nth-digit.py
# Description:
#
# LeetCode problem 400. Nth Digit
# 
# Difficulty: Easy
# 
# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8,
# 9, 10, 11, ...
# 
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n <
# 2^31).
# 
# Example 1:
# 
# Input:
# 3
# 
# Output:
# 3
# 
# Example 2:
# 
# Input:
# 11
# 
# Output:
# 0
# 
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
# which is part of the number 10.
#
###############################################################################

#
# Run time on LeetCode: 45ms, beat 43.86%; 79ms, beat 71.14%
#
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        cumulate_digit_num = 0
        while i < 11:    # A 32-bit signed integer has a maximum of 10 digits.
            temp = cumulate_digit_num + 9 * (10 ** (i - 1)) * i
            if temp >= n:
                break
            cumulate_digit_num = temp
            i += 1
        temp = n - cumulate_digit_num - 1
        integer = temp / i + 10 ** (i - 1)
        m = temp % i
        return (integer / (10 ** (i - 1 - m))) % 10
        

if __name__ == "__main__":
    test_cases = [
            1, 11, 12, 188, 189, 190, 191, 192, 193, 194, 195
    ]

    solu = Solution()
    for n in test_cases:
        res = solu.findNthDigit(n)
        print "{}: {}".format(n, res)
        print ""    
