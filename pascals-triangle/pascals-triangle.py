#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        pascals-triangle.py
# Create Date: 2017-02-06
# Usage:       pascals-triangle.py
# Description:
#
# LeetCode problem 118. Pascal's Triangle
#
# Difficulty: Easy
#
# Given numRows, generate the first numRows of Pascal's triangle.
# 
# For example, given numRows = 5,
# Return
# 
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
###############################################################################

#
# Method 1. Use the general formulas: the value of row n (n=0,1,...) and column
# m (m = 0,...,n) is f(n,m) = Cm,n = (n * (n-1) * ... * (n-m+1)) / m!
# Time complexity: O(n!*n^2)
# Run time on LeetCode: 45ms, beat 50.06%; 39ms, beat 80.57%
#
class Solution1(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for n in xrange(0, numRows):
            curRow = []
            for m in xrange(n+1):
                a = 1
                for i in xrange(n-m+1, n+1):
                    a *= i
                b = 1
                for i in xrange(1,m+1):
                    b *= i
                curRow.append(a / b)
            res += [curRow]
        return res

#
# Method 2. Use a queue.
# Time complexity: O(n^2)
# Run time on LeetCode: 49ms, beat 33.37%; 45ms, beat 50.06%; 39ms, beat 80.57%
#
class Solution2(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        queue = [0]
        curVal = 1
        row = 1
        while row <= numRows:
            curRow = []
            for _ in xrange(row):
                newVal = curVal + queue[0]
                curRow.append(newVal)
                queue.append(newVal)
                curVal = queue.pop(0)
            row += 1
            queue.append(0)
            res.append(curRow)
        return res


if __name__ == "__main__":
    import time

    test_cases = [1, 2, 3, 4, 5]
    test_cases = [1000]

    for Solution in [Solution1, Solution2]:
        solu = Solution()
        start_t = time.clock()
        for n in test_cases:
            res = solu.generate(n)
        end_t = time.clock()
        print "cpu time: %s" % (end_t - start_t)
        print ""
