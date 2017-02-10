#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        valid-palindrome.py
# Create Date: 2017-02-07
# Usage:       valid-palindrome.py
# Description:
#
# LeetCode problem 125. Valid Palindrome
#
# Difficulty: Easy
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# For example, "A man, a plan, a canal: Panama" is a palindrome.  "race a car"
# is not a palindrome.
# 
# Note: Have you consider that the string might be empty? This is a good
# question to ask during an interview.
# 
# For the purpose of this problem, we define empty string as valid palindrome.
#
###############################################################################

#
# Do not use extra space. Space complexity: O(1)
# Run time on LeetCode: 105ms, beat 28.73%
#
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        for c in s:
            if c.isalnum():
                l += 1
        ch_nums_to_compare = l / 2
        i = 0
        j = len(s) - 1
        count = 0
        while count < ch_nums_to_compare:
            c1 = s[i]
            c2 = s[j]
            while not c1.isalnum():
                i += 1
                c1 = s[i]
            while not c2.isalnum():
                j -= 1
                c2 = s[j]
            if c1.upper() == c2.upper():
                i += 1
                j -= 1
                count += 1
            else:
                return False
        return True

#
# A more pythonic method, but it uses extra space.
# Run time on LeetCode: 89ms, beat 59.50%; 115ms, beat 19.72%
#
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = filter(unicode.isalnum, s.decode('utf-8')).upper()
        return s1 == s1[::-1]

if __name__ == "__main__":
    import time

    test_cases = [
        "",
        " ",
        "*;;",
        "A man, a plan, a canal: Panama",
        u"A man, a plan, a canal: Panama",
        u"race a car",
    ]

    solu = Solution()
    start_t = time.clock()
    for s in test_cases:
        print s
        res = solu.isPalindrome(s)
        print res
        print ""
    end_t = time.clock()
    print "cpu time: %s" % (end_t - start_t)
    print ""
