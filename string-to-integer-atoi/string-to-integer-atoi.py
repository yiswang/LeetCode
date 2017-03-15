#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        string-to-integer-atoi.py
# Create Date: 2017-02-26
# Usage:       string-to-integer-atoi.py
# Description:
#
# LeetCode problem 8. String to Integer (atoi)
# 
#     Difficulty: Medium
# 
# Implement atoi to convert a string to an integer.
# 
# Hint: Carefully consider all possible input cases. If you want a challenge,
# please do not see below and ask yourself what are the possible input cases.
# 
# Notes: It is intended for this problem to be specified vaguely (ie, no given
# input specs). You are responsible to gather all the input requirements up
# front.
# 
# Update (2015-02-10): The signature of the C++ function had been updated. If
# you still see your function signature accepts a const char * argument, please
# click the reload button to reset your code definition.
# 
# Requirements for atoi:
# 
# The function first discards as many whitespace characters as necessary until
# the first non-whitespace character is found. Then, starting from this
# character, takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
# 
# The string can contain additional characters after those that form the
# integral number, which are ignored and have no effect on the behavior of this
# function.
# 
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is empty or
# it contains only whitespace characters, no conversion is performed.
# 
# If no valid conversion could be performed, a zero value is returned. If the
# correct value is out of the range of representable values, INT_MAX
# (2147483647) or INT_MIN (-2147483648) is returned.
# 
###############################################################################

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        sign = 1
        int_value = 0
        MAXSIZE = 2 ** 31 - 1
        j = 0
        for i in xrange(len(str)):
            ch = str[i]
            if ch == " " or ch == "\t":
                continue

            if ch == "+" or ch == "-":
                sign = 1 if ch == "+" else -1
                j = i + 1
                break
            else:
                j = i
                break

        for ch in str[j:]:
            if not (ch >= '0' and ch <= '9'):
                break
            else:
                int_value = int_value * 10 + int(ch)
        
        int_value = int_value * sign
        if int_value > MAXSIZE:
            return MAXSIZE
        if int_value < -(MAXSIZE + 1):
            return -(MAXSIZE + 1)

        return int_value


if __name__ == "__main__":
    pass
