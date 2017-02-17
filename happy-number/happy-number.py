#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        happy-number.pty
# Create Date: 2017-02-17
# Usage:       happy-number.py
# Description:
#
# LeetCode problem 202. Happy Number
#
# Difficulty: Easy
#
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Example: 19 is a happy number
# 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
###############################################################################

#
# Method 1.
# Main idea:
# For all numbers the process will end in one of the numbers of 1 ~ 6 at one
# time during the loop. And 2 ~ 6 are all not happy numbers.
#
# Run time on LeeCode: 58ms, beat 41.53%
#
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 6:
            s = 0
            while n:
                s += (n % 10) ** 2
                n = n / 10
            n = s
        if n == 1:
            return True
        else:
            return False


#
# Method 2.
# Main idea:
# The loop process will go ahead by 'one step' and 'two steps' respectively. It's
# like the problem of linked list cycle detection.
#
# Run time on LeeCode: 65ms, beat 24.67%
#
class Solution(object):
    def squareSumOfDigits(self, n):
        s = 0
        while n:
            s += (n % 10) ** 2
            n = n / 10
        return s

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = fast = n
        while True:
            slow = self.squareSumOfDigits(slow)
            fast = self.squareSumOfDigits(fast)
            fast = self.squareSumOfDigits(fast)
            if slow == fast:
                break
        if slow == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    test_cases = [1, 19, 37]
#     test_cases = [37]

    solu = Solution()
    for n in test_cases:
        print n
        print solu.isHappy(n)
        print ""
