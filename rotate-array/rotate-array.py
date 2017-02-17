#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        rotate-array.py
# Create Date: 2017-02-15
# Usage:       rotate-array.py
# Description:
#
# LeetCode problem 189. Rotate Array
#
# Difficulty: Easy
#
# Rotate an array of n elements to the right by k steps.
# 
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to
# [5,6,7,1,2,3,4].
# 
# Note:
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# 
# Hint:
# Could you do it in-place with O(1) extra space?
# Related problem: Reverse Words in a String II
#
###############################################################################

#
# Time complexity: O(n), space complexity: O(k)
# Run time on LeetCode: 72ms. Beats 83.81%
#
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        nums_temp = nums[-k:]
        for i in xrange(l - k - 1, -1, -1):
            nums[i+k] = nums[i]
        for i in xrange(k):
            nums[i] = nums_temp[i]


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5, 6], 1),
        ([1, 2, 3, 4, 5, 6], 2),
        ([1, 2, 3, 4, 5, 6], 3),
    ]

    solu = Solution()
    for array, n in test_cases:
        print array
        solu.rotate(array, n)
        print array
        print ""
    
