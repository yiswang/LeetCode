#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        move-zeroes.py
# Create Date: 2017-02-27
# Usage:       move-zeroes.py
# Description:
#
# LeetCode problem 283. Move Zeroes Add to List
#
# Difficulty: Easy
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
# should be [1, 3, 12, 0, 0].
# 
# Note: You must do this in-place without making a copy of the array.  Minimize
# the total number of operations.
#
###############################################################################

# 
# n times of comparision, n times of value assignment.
# Run time on Leetcode: 59ms, beat 96.17%
# 
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """ 
        l = len(nums)
        insertPos = 0
        for n in nums:
            if n != 0:
                nums[insertPos] = n
                insertPos += 1
        nums[insertPos:l] = [0] * (l - insertPos)


if __name__ == "__main__":
    test_cases = [
        [],
        [0],
        [1],
        [1, 0],
        [0, 1],
        [0, 1, 2],
        [1, 0, 2],
        [1, 2, 0],
        [1, 0, 3, 12, 0],
    ]
    solu = Solution()
    for array in test_cases:
        print array
        res = solu.moveZeroes(array)
        print array
        print ""    
