#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        climbing-stairs.py
# Create Date: 2017-01-29
# Usage:       climbing-stairs.py
# Description:
#
# LeetCode problem 70. Climbing Stairs
# 
# Difficulty: Easy
# 
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# Note: Given n will be a positive integer. 
#
###############################################################################

#
# This is basically a Fabonacci sequence problem: f(n) = f(n-1) + f(n-2)
#

#
# A recursive method 
# Time complexity: O(n^2); Space complexity: O(n)
# Run time on LeetCode: TLE
#
class Solution1(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

#
# A non-recursive method
# Time complexity: O(n); Space complexity: O(1)
# Run time on LeetCode: 38ms
#
class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        last_res = 1
        cur_res = 2
        for _ in xrange(n-2):
            last_res, cur_res = cur_res, last_res + cur_res
        return cur_res


#
# Use the common function of Fabonacci sequence.
# Time complexity: O(1); Space complexity: O(1)
# Run time on LeetCode: 35ms. Beats 86%
#
class Solution3(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        sqrt_five = 5 ** 0.5
        return int(1 / sqrt_five * (((1+sqrt_five)/2)**(n+1) - ((1-sqrt_five)/2)**(n+1)))

if __name__ == "__main__":
    test_cases = [1, 2, 3, 4, 5, 6, 9, 10, 16, 25, 26, 35]

    solu = Solution3()
    for n in test_cases:
        print solu.climbStairs(n)
    print ""
