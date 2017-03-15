#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        palindrome-number.py
# Create Date: 2017-02-26
# Usage:       palindrome-number.py
# Description:
#
# LeetCode problem  9. Palindrome Number
# 
#     Difficulty: Easy
# 
# Determine whether an integer is a palindrome. Do this without extra space.
#
###############################################################################

class Solution(object):
    def isPalindrome(self, x): 
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        x2 = x 
        digits_count = 0 
        while x2 > 0:
            x2 = x2 / 10
            digits_count += 1

        x2 = x 
        power = digits_count - 1 
        for i in xrange(0, digits_count / 2): 
            right_digit = x2 % 10
            left_digit = (x2 / (10 ** power)) % 10
            x2 = x2 / 10
            power -= 2
            if right_digit != left_digit:
                return False

        return True


if __name__ == "__main__":
    pass
