#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        contains-duplicate.py
# Create Date: 2017-02-21
# Usage:       contains-duplicate.py
# Description:
#
# LeetCode problem 217. Contains Duplicate Add to List
#
# Difficulty: Easy
#
# Given an array of integers, find if the array contains any duplicates. Your
# function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.
#
###############################################################################

#
# A pythonic methoc.
# Run time on LeetCode: 75ms, beat 28.42%
#
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


#
# Run time on LeetCode: 79ms, beat 23.07%
#
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for n in nums:
            if d.has_key(n):
                return True
            d[n] = 1
        return False


if __name__ == "__main__":
    test_cases = [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 1],
        [1, 2, 1],
        [1, 2, 1, 3],
    ]
    solu = Solution()
    for array in test_cases:
        print array
        res = solu.containsDuplicate(array)
        print res
        print ""
