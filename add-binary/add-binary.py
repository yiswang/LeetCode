#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        add-binary.py
# Create Date: 2017-01-27
# Usage:       add-binary.py
# Description:
#
# LeetCode problem 67. Add Binary
# 
# Difficulty: Easy
# 
# Given two binary strings, return their sum (also a binary string).
# 
# For example,
# a = "11"
# b = "1"
# Return "100". 
# 
###############################################################################

#
# Note: Take care of the case that the two strings have different length.
# Run Time on LeetCode: 65ms
#
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        if len_a > len_b:
            b = '0' * (len_a - len_b) + b
            i = len_a - 1
        else:
            a = '0' * (len_b - len_a) + a
            i = len_b - 1
        carry = 0
        res = ""
        while i>=0:
            cur_sum = int(a[i]) + int(b[i]) + carry
            if cur_sum == 3:
                carry = 1
                res = "1" + res
            elif cur_sum == 2:
                carry = 1
                res = "0" + res
            else:
                carry = 0
                res = str(cur_sum) + res
            i -= 1
        if carry == 1:
            res = "1" + res
        return res
                
        
if __name__ == "__main__":
    test_cases = [
        ("0", "0"),
        ("0", "1"),
        ("10", "1"),
        ("11", "1"),
        ("11", "11"),
        ("101", "11"),
    ]
    solu = Solution()
    for a, b in test_cases:
        print "%s + %s = %s" % (a, b, solu.addBinary(a, b))
