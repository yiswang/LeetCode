#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        nim-game.py
# Create Date: 2017-02-28
# Usage:       nim-game.py
# Description:
#
# LeetCode problem 292. Nim Game Add to List
#
# Difficulty: Easy
#
# You are playing the following Nim Game with your friend: There is a heap of
# stones on the table, each time one of you take turns to remove 1 to 3 stones.
# The one who removes the last stone will be the winner. You will take the
# first turn to remove the stones.
# 
# Both of you are very clever and have optimal strategies for the game. Write a
# function to determine whether you can win the game given the number of stones
# in the heap.
# 
# For example, if there are 4 stones in the heap, then you will never win the
# game: no matter 1, 2, or 3 stones you remove, the last stone will always be
# removed by your friend.
# 
###############################################################################

#
# Method 1: Recursively.
# Run time on LeetCode: Time Limit Exceeded
#
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 3:
            return True
        return not (self.canWinNim(n - 1) and self.canWinNim(n - 2) and self.canWinNim(n - 3))


#
# Method 2: Determine directively by the value of "n % 4".
# Run time on LeetCode: 35ms, beat 91.53%; 42ms, beat 47.28%
#
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0


if __name__ == "__main__":
    test_cases = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ]
    solu = Solution()
    for n in test_cases:
        print n
        res = solu.canWinNim(n)
        print res
        print ""    
