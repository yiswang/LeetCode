#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        reverse-bits.py
# Create Date: 2017-02-14
# Usage:       reverse-bits.py
# Description:
#
# LeetCode problem 190. Reverse Bits
#
# Difficulty: Easy
#
# Reverse bits of a given 32 bits unsigned integer.
# 
# For example, given input 43261596 (represented in binary as
# 00000010100101000001111010011100), return 964176192 (represented in binary as
# 00111001011110000010100101000000).
# 
# Follow up:
# If this function is called many times, how would you optimize it?
#
###############################################################################

#
# Run time on LeetCode: 62ms, beat 16.35%; 42ms, beat 82.31%; 49ms, beat 45.84%
#
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        bits_count = 0
        while n:
            remainder = n % 2
            n = n / 2
            res = res * 2 + remainder
            bits_count += 1
        res <<= 32 - bits_count
        return res


#
# An optimized version. Time complexity: O(1)
# Run time on LeetCode: 65ms, beat 14.61%; 59, beat 20.11%; 69ms, beat 10.59%
#
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n


if __name__ == "__main__":
    test_cases = [
        0,
        1,
        43261596,
    ]

    solu = Solution()
    for num in test_cases:
        print solu.reverseBits(num)
    print ""
