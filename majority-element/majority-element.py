#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        majority-element.py
# Create Date: 2017-02-10
# Usage:       majority-element.py
# Description:
#
# LeetCode problem 169. Majority Element
#
# Difficulty: Easy
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ? n/2 ? times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
#
###############################################################################

#
# Method 1. Use hashmap.
# Time complexity: O(n); space complexity: O(n)
# Run time on LeetCode: 78ms, beat 43.36%
#
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        n = len(nums)
        m = n / 2
        for i in xrange(n):
            num = nums[i]
            if d.has_key(num):
                d[num] += 1
            else:
                d[num] = 1
            if d[num] > m:
                return num
        return None


#
# Method 2. Do not use hashmap.
#
# Main idea:
# If remove every two different elements, then the major element must be the
# only remained element at the end.
# Time complexity: O(n); space complexity: O(1)
#
# Run time on LeetCode: 75ms, beat 46.52%
#
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        major = nums[0]
        for num in nums[1:]:
            if count == 0:
                count += 1
                major = num
            elif num == major:
                count += 1
            else:
                count -= 1
        return major

        
if __name__ == "__main__":
    test_cases = [
        [1,2,3],
        [1,1,2],
        [1,1,2,3],
        [1,1,1,2],
    ]
    solu = Solution()
    for nums in test_cases:
        res = solu.majorityElement(nums)
        print nums
        print res
