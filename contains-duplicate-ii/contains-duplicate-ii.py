#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        contains-duplicate-ii.py
# Create Date: 2017-02-21
# Usage:       contains-duplicate-ii.py
# Description:
#
# LeetCode problem 219. Contains Duplicate II Add to List
#
# Difficulty: Easy
#
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
#
###############################################################################

#
# Run time on LeetCode: 58ms, beat 77.50%
#
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, n in enumerate(nums):
            if d.has_key(n) and i - d[n] <= k:
                return True
            d[n] = i
        return False



if __name__ == "__main__":
    test_cases = [
        ([], 0),
        ([1], 1),
        ([1, 2], 1),
        ([1, 2, 3], 1),
        ([1, 1], 0),
        ([1, 2, 1], 1),
        ([1, 2, 3, 4, 5, 3, 1], 2),
        ([1, 2, 1, 1], 1),
        ([1, 2, 1, 2, 3, 3, 1], 1),
        ([1, 2, 3, 4, 5, 3, 5, 1], 2),
    ]
    solu = Solution()
    for array, k in test_cases:
        print array, k
        res = solu.containsNearbyDuplicate(array, k)
        print res
        print ""
