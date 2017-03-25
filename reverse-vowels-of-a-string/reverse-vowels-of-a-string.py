#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        reverse-vowels-of-a-string.py
# Create Date: 2017-03-17
# Usage:       reverse-vowels-of-a-string.py
# Description:
#
# LeetCode problem 345. Reverse Vowels of a String Add to List
#
# Difficulty: Easy
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# Example 1:
# Given s = "hello", return "holle".
# 
# Example 2:
# Given s = "leetcode", return "leotcede".
# 
# Note:
# The vowels does not include the letter "y".
# 
###############################################################################

#
# Method 1.
# Run time on LeetCode: 142ms, beat 39.59%; 98ms, 71.22%
#
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        indices = []
        for i in xrange(len(s)):
            if s[i].lower() in "aeiou":
                indices.append(i)
        indices_new = indices[::-1]
        res = list(s)
        for i in xrange(len(indices)):
            res[indices[i]] = s[indices_new[i]]
        return ''.join(res)


#
# Method 2.
# Run time on LeetCode: 112ms, beat 55.31%
#
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        indices = []
        count = 0
        for i in xrange(len(s)):
            if s[i].lower() in "aeiou":
                indices.append(i)
                count += 1
        res = list(s)
        i, j = 0, count - 1
        while i < j:
            res[indices[i]] = s[indices[j]]
            res[indices[j]] = s[indices[i]]
            i += 1
            j -= 1
        return ''.join(res)


#
# Method 3.
# Run time on LeetCode: 78ms, beat 95.61%
#
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        import re
        pattern = '(?i)[aeiou]'
#         return re.sub(pattern, lambda m, v=re.findall(pattern, s): v.pop(), s)
        vowels = re.findall(pattern, s)
        return re.sub(pattern, lambda m: vowels.pop(), s)


#
# Method 4.
# Run time on LeetCode: 
#
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j = 0, len(s) - 1
        l = list(s)
        while i < j:
            while i < j and not s[i].lower() in "aeiou": i += 1
            while i < j and not s[j].lower() in "aeiou": j -= 1
            l[i], l[j] = l[j], l[i]
            i, j = i+1, j-1
        return ''.join(l)


if __name__ == "__main__":
    test_cases = [
            "",
            "hello",
            "hello world",
    ]
    solu = Solution()
    for n in test_cases:
        res = solu.reverseVowels(n)
        print res
        print ""    
