#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        merge-sorted-array.py
# Create Date: 2017-01-29
# Usage:       merge-sorted-array.py
# Description:
#
# LeetCode problem 88. Merge Sorted Array
# 
# Difficulty: Easy
# 
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note: You may assume that nums1 has enough space (size that is greater or
# equal to m + n) to hold additional elements from nums2. The number of
# elements initialized in nums1 and nums2 are m and n respectively.
#
###############################################################################


#
# A method that uses extra spaces.
# Time complexity: O(n+m); Space complexity: O(n+m)
# Run time on LeetCode: 49ms. Beat 52%
#
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1_temp = [nums1[i] for i in xrange(0,m)]
        i = j = k = 0
        while i<m and j<n:
            if nums1_temp[i] <= nums2[j]:
                nums1[k] = nums1_temp[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        for num in nums1_temp[i:m]:
            nums1[k] = num
            k += 1
        for num in nums2[j:n]:
            nums1[k] = num
            k += 1
#
# A method that does not use extra spaces.
# Time complexity: O(n+m); Space complexity: O(1)
# Run time on LeetCode: 59ms. Beat 32%
#
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[0:n] = nums2[0:n]


if __name__ == "__main__":
    test_cases = [
        ([],0,[],0),
        ([None],0,[1],1),
        ([1],1,[None],0),
        ([1,None],1,[1,None],1),
        ([2,None],1,[1,None],1),
        ([1,None],1,[2,None],1),
        ([2,3,None],2,[1,None],1),
        ([2,None,None],1,[1,3,None],2),
        ([1,1,None,None],2,[2,2,None,None],2),
        ([1,3,None,None],2,[2,2,None,None],2),
        ([1,3,None,None],2,[2,4,None,None],2),
        ([2,2,None,None],2,[1,1,None,None],2),
        ([2,2,None,None],2,[1,2,None,None],2),
        ([2,2,None,None],2,[1,3,None,None],2),
        ([2,4,None,None],2,[1,3,None,None],2),
        ([1,2,3,None,None,None,None], 3, [2,2,3,4,None,None,None], 4),
    ]
    solu = Solution()
    for testcase in test_cases:
        print "Before merge:"
        print testcase
        solu.merge(*testcase)
        print "After merge:"
        print testcase[0]
        print "\n"
