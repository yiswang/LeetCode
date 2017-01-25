#!/usr/bin/python

###############################################################################
#
# LeetCode question 66. Plus One
#
# Difficulty: Easy
#
# Given a non-negative integer represented as a non-empty array of digits, plus
# one to the integer.
# 
# You may assume the integer do not contain any leading zero, except the number
# 0 itself.
# 
# The digits are stored such that the most significant digit is at the head of
# the list.
#
###############################################################################

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        i = l - 1
        while i >= 0:
            d = digits[i]
            if d == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                break
        if i < 0:
            digits = [1] + digits
        return digits
        

if __name__ == "__main__":
    test_cases = [
        [],
        [0],
        [9],
        [1, 9],
        [9, 9],
    ]

    solu = Solution()
    for digits in test_cases:
        res = solu.plusOne(digits)
        print res


