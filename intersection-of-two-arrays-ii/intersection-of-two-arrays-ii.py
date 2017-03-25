#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        intersection-of-two-arrays-ii.py
# Create Date: 2017-03-20
# Usage:       intersection-of-two-arrays-ii.py
# Description:
#
# LeetCode problem 350. Intersection of Two Arrays II
#
# Difficulty: Easy
#
# Given two arrays, write a function to compute their intersection.
# 
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
# 
# Note:
# Each element in the result should appear as many times as it shows in both
# arrays.
# The result can be in any order.
#
# Follow up:
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
# 
###############################################################################

#
# Method 1. O(n)-Time, O(n)-Space
# Run time on LeetCode: 79ms, beat 24.77%; 65ms, beat 42.61%
#
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        res = []
        for n in nums1:
            d[n] = d[n] + 1 if d.has_key(n) else 1
        for n in nums2:
            if d.has_key(n) and d[n] > 0:
                res.append(n)
                d[n] -= 1
        return res


#
# Method 2. Use datatype collections.Counter
# Run time on LeetCode: 55ms, beat 63.49%; 59ms, beat 51.76%
#
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        return list((c1 & c2).elements())


if __name__ == "__main__":
    test_cases = [
            ([], []),
            ([1,2,3], [2]),
            ([1,2,2,3], [2,2]),
            ([2,3], [1,2,2,3]),
            ([1,2,2,3], [2,4]),
    ]
    solu = Solution()
    for nums1, nums2 in test_cases:
        res = solu.intersect(nums1, nums2)
        print res
        print ""    
