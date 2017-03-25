#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        range-sum-query-immutable.py
# Create Date: 2017-02-28
# Usage:       range-sum-query-immutable.py
# Description:
#
# LeetCode problem 303. Range Sum Query - Immutable Add to List
#
# Difficulty: Easy
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ¡Ü j), inclusive.
# 
# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
#
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.
# 
###############################################################################

#
# Method 1:
# Run time on LeetCode: 989ms, beat 6.07%
#
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1])
        

#
# Method 2:
# Run time on LeetCode: 72ms, beat 85.10%; 116ms, 26.34%
#
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cumulativeSums = [0] + nums
        for i in xrange(len(nums)):
            self.cumulativeSums[i+1] += self.cumulativeSums[i]


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cumulativeSums[j+1] - self.cumulativeSums[i]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


if __name__ == "__main__":
    test_cases = [
        ([-2, 0, 3, -5, 2, -1], 0, 2),
        ([-2, 0, 3, -5, 2, -1], 2, 5),
        ([-2, 0, 3, -5, 2, -1], 0, 5),
    ]
    for nums, i, j in test_cases:
        print nums, i, j
        obj = NumArray(nums)
        res = obj.sumRange(i, j)
        print res
        print ""    
