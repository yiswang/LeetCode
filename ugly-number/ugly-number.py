#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        ugly-number.py
# Create Date: 2017-02-26
# Usage:       ugly-number.py
# Description:
#
# LeetCode problem  263. Ugly Number
# 
# Difficulty: Easy
# 
# Write a program to check whether a given number is an ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 6, 8 are ugly while 14 is not ugly since it includes another
# prime factor 7.
# 
# Note that 1 is typically treated as an ugly number. 
# 
###############################################################################

# Run time on LeetCode: Memory Limit Exceeded.
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num == 1:
            return True
        isPrime = [True] * (num+1)
        for i in xrange(2, num+1):
            if isPrime[i]:
                for j in xrange(i, num+1, i):
                    isPrime[j] = False
        for i in xrange(2, num+1):
            if isPrime[i] and not i in [2,3,5]:
                if num % i == 0:
                    return False
        return True


# Run time on LeetCode: Memory Limit Exceeded 
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num == 1:
            return True
        notUglyNums = []
        for i in xrange(7, num+1):
            if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
                continue
            for j in xrange(i, num+1, i):
                notUglyNums.append(j)
        return num not in notUglyNums


# Run time on LeetCode: 72ms, beat 10.51%
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for p in [2, 3, 5]:
            while num % p == 0 < num:
                num /= p
        return num == 1


if __name__ == "__main__":
    test_cases = [
        -1, 0, 1, 2, 3, 5, 6, 7, 10, 14, 15, 16
    ]
    solu = Solution()
    for num in test_cases:
        res = solu.isUgly(num)
        print num, res
