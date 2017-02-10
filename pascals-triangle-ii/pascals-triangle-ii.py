#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        pascals-triangle-ii.py
# Create Date: 2017-02-06
# Usage:       pascals-triangle-ii.py
# Description:
#
# LeetCode problem 119. Pascal's Triangle II
#
# Difficulty: Easy
#
# Given an index k, return the kth row of the Pascal's triangle.
# 
# For example, given k = 3,
# Return [1,3,3,1].
# 
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
#
###############################################################################

#
# Use a queue. At the end, just return the queue, so the extra space is O(k).
# Time complexity: O(n^2), Space complexity: O(n)
# Run time on LeetCode: 52ms, beat 23.24%; 42ms, beat 55.78%; 48ms, beat 37.58%
#
class Solution1(object):
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        queue = []
        curVal = 1
        row = 1
        while row <= rowIndex+1:
            queue.append(0)
            for _ in xrange(row):
                newVal = curVal + queue[0]
                queue.append(newVal)
                curVal = queue.pop(0)
            row += 1
        return queue

#
# A more pythonic method from someone else on the LeetCode.
#
class Solution2(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row


if __name__ == "__main__":
    import time

    test_cases = [1, 2, 3, 4, 5]
    test_cases = [1000]

    solu = Solution1()
    start_t = time.clock()
    for n in test_cases:
        res = solu.getRow(n)
        print res
    end_t = time.clock()
    print "cpu time: %s" % (end_t - start_t)
    print ""
