#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        minimum-window-substring.py
# Create Date: 2017-02-16
# Usage:       minimum-window-substring.py
# Description:
#
# LeetCode problem 76. Minimum Window Substring
#
# Difficulty: Hard
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".
# 
# Note:
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# 
# If there are multiple such windows, you are guaranteed that there will always
# be only one unique minimum window in S.
#
###############################################################################

# A wrong solution.
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        q = []
        d = {}
        count = 0
        minL = 0
        minSubStr = ""
        lenT = len(t)
        lenS = len(s)
        for ch in t:
            d[ch] = 0
        for i in xrange(lenS):
            ch = s[i]
            if d.has_key(ch):
                q.append((ch, i))
                d[ch] += 1
                count += 1
                break
        if count == lenT:
            return s[i]

        for i in xrange(i, lenS):
            ch = s[i]
            if d.has_key(ch):
                if ch == q[-1][0]:
                    q.pop()
                elif d[ch] == 0:
                    count += 1
                    d[ch] = 1
                else:
                    d[ch] += 1
                q.append((ch, i))
                if count == lenT:
                    lenSubStr = q[-1][1] - q[0][1] + 1
                    if minL == 0 or lenSubStr < minL:
                        minL = lenSubStr
                        minSubStr = s[q[0][1] : q[-1][1]+1]
                    print q
                    first = q.pop(0)
                    d[first[0]] -= 1
                    print q
                    count -= 1
        return minSubStr

#
# Run time on LeetCode: 159ms. Beats 68.29%
#
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        chCountT = {}
        chCount = {}
        count = 0
        minL = 2**31 - 1
        minSubStr = ""
        lenT = len(t)
        lenS = len(s)
        for ch in t:
            chCountT[ch] = 1 if not chCountT.has_key(ch) else chCountT[ch] + 1
        for ch in s:
            chCount[ch] = 0

        j = 0
        for i in xrange(lenS):
            ch = s[i]
            if chCountT.has_key(ch):
                chCount[ch] += 1
                if chCount[ch] <= chCountT[ch]:
                    count += 1
            if count == lenT:
                while (not chCountT.has_key(s[j])) or (chCount[s[j]] > chCountT[s[j]]):
                    chCount[s[j]] -= 1
                    j += 1
                l = i - j + 1
                if l < minL:
                    minL = l
                    minSubStr = s[j:i+1]

        return minSubStr    

if __name__ == "__main__":
    test_cases = [
        ("", ""),
        ("", "N"),
        ("aa", ""),
        ("a", "a"),
        ("aa", "aa"),
        ("aab", "aab"),
        ("aacabaa", "aab"),
        ("baacabaa", "aabb"),
        ("babac", "abc"),
        ("ADOBECODEBANC", "N"),
        ("DAOBBCOAEBANC", "ABC"),
        ("DAOBBCOAEBANC", "ABCE"),
        ("DAOBBCOAEBANC", "ABCF"),
    ]

    solu = Solution()
    for s, t in test_cases:
        print s, t
        print solu.minWindow(s, t)
        print ""
