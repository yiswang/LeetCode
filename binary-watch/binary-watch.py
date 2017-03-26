#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        binary-watch.py
# Create Date: 2017-03-26
# Usage:       binary-watch.py
# Description:
#
# LeetCode problem  401. Binary Watch
# 
# Difficulty: Easy
# 
# A binary watch has 4 LEDs on the top which represent the hours (0-11), and
# the 6 LEDs on the bottom represent the minutes (0-59).
# 
# Each LED represents a zero or one, with the least significant bit on the
# right.
# 
# For example, the above binary watch reads "3:25".
# 
# Given a non-negative integer n which represents the number of LEDs that are
# currently on, return all possible times the watch could represent.
# 
# Example:
# 
# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08",
# "0:16", "0:32"]
#
# Note:
# 
#     The order of output does not matter.
#
#     The hour must not contain a leading zero, for example "01:00" is not
#     valid, it should be "1:00".
#
#     The minute must be consist of two digits and may contain a leading zero,
#     for example "10:2" is not valid, it should be "10:02".
# 
#
###############################################################################

#
# Method 1. By calculating the hamming weight.
# Run time on LeetCode: 42ms, beat 87.25%; 46ms, beat 61.07%;
#
def hammingWeight(integer):
    count = 0
    while integer:
        integer &= integer - 1
        count += 1
    return count

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for h in xrange(0, 12):
            weight = hammingWeight(h)
            if weight <= num:
                for m in xrange(0, 60):
                    if num - weight == hammingWeight(m):
                        res.append("{}:{:02d}".format(h,m))
        return res

        
#
# Method 2.
# Run time on LeetCode: 42ms, beat 87.25%; 62ms, beat 22.49%
#
hour = [
    ["0"], 
    ["1", "2", "4", "8"],
    ["3", "5", "6", "9", "10"],
    ["7", "11"]
]
minute = [
    ["00"],
    ["01", "02", "04", "08", "16", "32"],
    ["03", "05", "06", "09", "10", "12", "17", "18", "20", "24", "33", "34", "36", "40", "48"],
    ["07", "11", "13", "14", "19", "21", "22", "25", "26", "28", "35", "37", "38", "41", "42", "44", "49", "50", "52", "56"],
    ["15", "23", "27", "29", "30", "39", "43", "45", "46", "51", "53", "54", "57", "58"],
    ["31", "47", "55", "59"]
]
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for i in xrange(0, 4):
            for j in xrange(0, 6):
                if num == i + j:
                    for h in hour[i]:
                        for m in minute[j]:
                            res.append(h + ":" + m)
        return res


#
# Method 3. A more pythonic method.
# Run time on LeetCode: 65ms, beat 19.05%; 45ms, beat 76.07%
#
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ["{}:{:02d}".format(h, m) \
                for h in range(12) for m in range(60) \
                if (bin(h) + bin(m)).count('1') == num]


if __name__ == "__main__":
    test_cases = range(0, 11)

    solu = Solution()
    for n in test_cases:
        res = solu.readBinaryWatch(n)
        print "{}: {}".format(n, res)
        print ""    
