#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        single-number.py
# Create Date: 2017-02-08
# Usage:       single-number.py
# Description:
#
# LeetCode problem 136. Single Number
#
# Difficulty: Easy
#
# Given an array of integers, every element appears twice except for one. Find
# that single one.
# 
# Note: Your algorithm should have a linear runtime complexity. Could you
# implement it without using extra memory?
#
###############################################################################

#
# A method that have only one time of traverse. But it uses extra memory space
# and can only work for this case, that is, if there are elements appear more
# than twice, this method may fail.
# Time complexity: O(n), Space complexity: O(n)
#
# Run time on LeetCode: 62ms, 27.59%
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if d.has_key(i):
                del d[i]
            else:
                d[i] = 1
        return d.keys()[0]

#
# Use XOR operation. It has linear runtime and uses no extra memory.
# Run time on LeetCode: 52ms, 54.35%
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i in nums[1:]:
            res ^= i
        return res


if __name__ == "__main__":
    test_cases = [
        [1],
        [1, 2, 2],
        [2, 1, 2],
        [2, 2, 1],
        [1, 2, 2, 3, 3],
        [2, 1, 2, 3, 3],
        [2, 2, 1, 3, 3],
        [2, 2, 3, 3, 4],
    ]

    solu = Solution()
    for nums in test_cases:
        print solu.singleNumber(nums)
    print ""
