#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        number-of-1-bits.py
# Create Date: 2017-02-17
# Usage:       number-of-1-bits.py
# Description:
#
# LeetCode problem 191. Number of 1 Bits
#
# Difficulty: Easy
#
# Write a function that takes an unsigned integer and returns the number of
# '1' bits it has (also known as the Hamming weight).
# 
# For example, the 32-bit integer '11' has binary representation
# 00000000000000000000000000001011, so the function should return 3.
#
###############################################################################

# Time complexity: O(logn).
# Run time on LeetCode: 66ms, beat 9.76%
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n % 2
            n /= 2
        return count

# Time complexity: O(m), m is the number of 1 bits.
# Run time on LeetCode: 49ms, beat 42.03%
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count


if __name__ == "__main__":
    test_cases = [
        0, 1, 2, 3, 4, 11,
    ]

    solu = Solution()
    for n in test_cases:
        print n
        print solu.hammingWeight(n)
        print ""
