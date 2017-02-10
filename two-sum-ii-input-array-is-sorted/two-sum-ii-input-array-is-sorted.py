#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        two-sum-ii-input-array-is-sorted.py
# Create Date: 2017-02-09
# Usage:       two-sum-ii-input-array-is-sorted.py
# Description:
#
# LeetCode problem 167. Two Sum II - Input array is sorted
#
# Difficulty: Easy
#
# Given an array of integers that is already sorted in ascending order, find
# two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they
# add up to the target, where index1 must be less than index2. Please note that
# your returned answers (both index1 and index2) are not zero-based.
# 
# You may assume that each input would have exactly one solution and you may
# not use the same element twice.
# 
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
#
###############################################################################

#
# Use two pointers, traverse from two sides of the array respectively.
# Time complexity: O(n)
# Run time on LeetCode: 39 ms, beat 95.88%
#
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(numbers) - 1
        while low < high:
            temp = numbers[low] + numbers[high]
            if temp == target:
                return [low+1, high+1]
            elif temp > target:
                high -= 1
            else:
                low += 1
        return None

        
if __name__ == "__main__":
    test_cases = [
        ([], None),
        ([], 2),
        ([1], 1),
        ([1], 2),
        ([1,2], 2),
        ([1,2], 3),
        ([1,2,3,4], 3),
        ([1,2,3,4], 6),
        ([1,2,3,4], 9),
    ]
    solu = Solution()
    for numbers, target in test_cases:
        print numbers, target
        res = solu.twoSum(numbers, target)
        print res
        print "\n"
