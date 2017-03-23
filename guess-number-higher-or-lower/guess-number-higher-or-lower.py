#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        guess-number-higher-or-lower.py
# Create Date: 2017-03-23
# Usage:       guess-number-higher-or-lower.py
# Description:
#
# LeetCode problem 374. Guess Number Higher or Lower
#
# Difficulty: Easy
# 
# We are playing the Guess Game. The game is as follows:
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I'll tell you whether the number is higher or
# lower.
# 
# You call a pre-defined API guess(int num) which returns 3 possible results
# (-1, 1, or 0):
# 
# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!
# 
# Example:
# 
# n = 10, I pick 6.
# 
# Return 6.
# 
###############################################################################

#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

#
# Method 1.
# Run time on LeetCode: 45ms, beat 36.81%; 42ms, beat 45.60%
#
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low < high:
            guessedNum = (low + high) / 2
            if 1 == guess(guessedNum):
                low = guessedNum + 1
            else:
                high = guessedNum

            # The following lines are right also.
#             low, high = [
#                     (low, guessedNum), 
#                     (low, guessedNum),
#                     (guessedNum+1, high)][guess(guessedNum)]

        return low


#
# Method 2. Use bisect module and python __getitem__ method.
# Run time on LeetCode: 42ms; 62ms
#
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        import bisect

        # Use the python __getitem__ method
        # C()[0] = -1, C()[1] = -1, ..., C()[m] = 0, C()[m+1] = 1, ..., where m
        # is equal to the right number.
        class C:
            def __getitem__(self, key):
                return -guess(key) 
#         class C: __getitem__ = lambda _, i: -guess(i) # This line is right also.

        return bisect.bisect(C(), -1, 0, n)

def guess(n):
    if 6 == n:
        return 0
    else:
        return -1 if 6 - n < 0 else 1


if __name__ == "__main__":
    test_cases = [10, 30, 100]
#     test_cases = [100]

    solu = Solution()
    for n in test_cases:
        res = solu.guessNumber(n)
        print res
    pass
