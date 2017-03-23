#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        ransom-note.py
# Create Date: 2017-03-23
# Usage:       ransom-note.py
# Description:
#
# LeetCode problem 383. Ransom Note
#
# Difficulty: Easy
# 
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom
# note can be constructed from the magazines ; otherwise, it will return false.
# 
# Each letter in the magazine string can only be used once in your ransom note.
# 
# Note:
# You may assume that both strings contain only lowercase letters.
# 
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
# 
###############################################################################

#
# Method 1. Use collections.Counter module. O(n) - Time, O(n) - Space
# Run time on LeetCode: 245ms, beat 12.76%; 179ms, beat 38.67%; 186ms, beat 35.00%
#
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        import collections
        return not (collections.Counter(ransomNote) - collections.Counter(magazine))


#
# Method 2. Do not use hash tables.
# Run time on LeetCode: 132ms, beat 57.14%; 135ms, beat 56.92%
#
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = [0] * 26
        for ch in magazine:
            counts[ord(ch) - ord('a')] += 1
        for ch in ransomNote:
            counts[ord(ch) - ord('a')] -= 1
        for count in counts:
            if count < 0:
                return False
        return True



if __name__ == "__main__":
    test_cases = [
            ("a", "b"),
            ("aa", "ab"),
            ("ab", "aab"),
    ]

    solu = Solution()
    for  s1, s2 in test_cases:
        print '"{}", "{}"'.format(s1, s2)
        res = solu.canConstruct(s1, s2)
        print res
        print ""
    pass
