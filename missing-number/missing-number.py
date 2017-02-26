#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        missing-number.py
# Create Date: 2017-02-26
# Usage:       missing-number.py
# Description:
#
# LeetCode problem 268. Missing Number
# 
# Difficulty: Easy
# 
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
# 
# For example, Given nums = [0, 1, 3] return 2.
# 
# Note: Your algorithm should run in linear runtime complexity. Could you
# implement it using only constant extra space complexity? 
# 
###############################################################################

#
# Method 1. Use SUM.
# Run time on LeetCode: 48ms, beat 94.23%
#
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = n * (n + 1) / 2
        return s - sum(nums)


#
# Method 2. Use XOR.
# Run time on LeetCode: 62, beat 48.72%
#
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in xrange(len(nums)):
            res = res ^ i ^ nums[i]
        return res ^ (i+1)


if __name__ == "__main__":
    solu = Solution()
    print solu.missingNumber([1,0,3])
    pass
