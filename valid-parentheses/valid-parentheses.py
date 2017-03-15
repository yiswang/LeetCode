#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        valid-parentheses.py
# Create Date: 2017-02-26
# Usage:       valid-parentheses.py
# Description:
#
# LeetCode problem  20. Valid Parentheses
# 
#     Difficulty: Easy
# 
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" are all valid
# but "(]" and "([)]" are not.
# 
###############################################################################

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        parenthese_map = { "(": ")", "[": "]", "{": "}" }
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif stack == []:
                return False
            else:
                if ch != parenthese_map.get(stack.pop()):
                    return False
        return stack == []


if __name__ == "__main__":
    pass
