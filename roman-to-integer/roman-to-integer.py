#!/usr/bin/python

###############################################################################
#
# LeetCode 13. Roman to Integer
#
# Difficulty: Easy
#
# Given a roman numeral, convert it to an integer.
# 
# Input is guaranteed to be within the range from 1 to 3999.
#
###############################################################################


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        base_symbol_numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        l = len(s)
        integer = 0
        i = 0
        while i < l:
            ch1 = s[i]
            if not ch1 in base_symbol_numbers.keys():
                return 0

            if i+1 < l:
                ch2 = s[i+1]
                temp = base_symbol_numbers[ch2] - base_symbol_numbers[ch1] 
                if temp > 0:
                    integer += temp
                    i += 1
                else:
                    integer += base_symbol_numbers[ch1]
            else:
                integer += base_symbol_numbers[ch1]
            i += 1

        return integer


if __name__ == "__main__":
    s1 = "VMV"
    solu = Solution()
    print solu.romanToInt(s1)
