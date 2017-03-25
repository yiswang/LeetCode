#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        first-bad-version.py
# Create Date: 2017-02-27
# Usage:       first-bad-version.py
# Description:
#
# LeetCode problem 278. First Bad Version Add to List
#
# Difficulty: Easy
#
# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the quality
# check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.
# 
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first
# bad one, which causes all the following ones to be bad.
# 
# You are given an API bool isBadVersion(version) which will return whether
# version is bad. Implement a function to find the first bad version. You
# should minimize the number of calls to the API.
#
###############################################################################

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def decoMaker(firstBadVersion):
    def deco(isBadVersion):
        def wrapper(version):
            return isBadVersion(version)
        return wrapper
    return deco


#
# Binary search
# Run time on LeetCode: 42ms, beat 46.57%
#
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low < high:
#             mid = (low + high) / 2
            # To avoid overflow, use the following line to get the middle value
            mid = low + (high - low) / 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return high if isBadVersion(high) else None
        

if __name__ == "__main__":
    test_cases = [
        (1, 1),
        (2, 1),
        (2, 2),
        (7, 3),
    ]
    solu = Solution()
    for n, firstBadVer in test_cases:
        print n, firstBadVer

        @decoMaker(firstBadVer)
        def isBadVersion(version):
            return version >= firstBadVer

        res = solu.firstBadVersion(n)
        print res
        print ""    
