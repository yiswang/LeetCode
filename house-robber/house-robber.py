#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        house-robber.py
# Create Date: 2017-02-17
# Usage:       house-robber.py
# Description:
#
# LeetCode problem 198. House Robber
#
# Difficulty: Easy
#
# robber planning to rob houses along a street. Each house has a certain amount
# of money stashed, the only constraint stopping you from robbing each of them
# is that adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
#
###############################################################################

#
# A recursive method.
# Run time on LeeCode: RuntimeError: maximum recursion depth exceeded
#
class Solution(object):
    def robHelper(self, nums, index):
        if index == 0:
            return nums[index]
        if index == 1:
            return nums[0] if nums[0] > nums[1] else nums[1]

        res1 = self.robHelper(nums, index - 2) + nums[index]
        res2 = self.robHelper(nums, index - 1)
        if res1 > res2:
            return res1
        return res2

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = len(nums) - 1
        return self.robHelper(nums, i)


#
# A non-recursive method. Time complexity: O(n)
# Run time on LeetCode: 39ms, beat 66.69%; 62ms, beat 6.86%
#
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for num in nums: last, now = now, max(last + num, now)
        return now


if __name__ == "__main__":
    test_cases = [
        [1],
        [1, 2],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [3, 2, 99, 300, 400],
        [1, 200, 2, 2, 100],
    ]

    solu = Solution()
    for array in test_cases:
        print array
        print solu.rob(array)
        print ""
