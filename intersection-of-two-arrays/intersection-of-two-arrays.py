#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        intersection-of-two-arrays.py
# Create Date: 2017-03-20
# Usage:       intersection-of-two-arrays.py
# Description:
#
# LeetCode problem 349. Intersection of Two Arrays
#
# Difficulty: Easy
#
# Given two arrays, write a function to compute their intersection.
# 
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
# 
# Note:
# Each element in the result must be unique.
# The result can be in any order.
# 
###############################################################################

#
# Method 1. O(n)-Time, O(n)-Space
# Run time on LeetCode: 52ms, beat 56.17%, 48ms, beat 76.51%
#
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Both of the following two methods are right.
#         return list(set(nums1).intersection(set(nums2)))
        return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    test_cases = [
            ([], []),
            ([1,2,3], [2]),
            ([1,2,2,3], [2,2]),
            ([1,2,2,3], [2,3]),
            ([1,2,2,3], [2,4]),
    ]
    solu = Solution()
    for nums1, nums2 in test_cases:
        res = solu.intersection(nums1, nums2)
        print res
        print ""    
