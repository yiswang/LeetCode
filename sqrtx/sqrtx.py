#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        sqrtx.py
# Create Date: 2017-01-27
# Usage:       sqrtx.py
# Description:
#
# LeetCode problem 69. Sqrt(x)
# 
# Difficulty: Easy
# 
# Implement int sqrt(int x).
# 
# Compute and return the square root of x.
# 
###############################################################################

import math

#
# Binary method. The precision: 1.
# Run Time on LeetCode: 52ms
#
class Solution1(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        res = x
        iter_count = 0
        while res>0:
            iter_count += 1
            sqr = res * res
            if sqr == x or (low + 1 == high):
                print "iterator count: %d, result: %s" % (iter_count, res)
                return res
            elif sqr > x:
                high = res
            else:
                low = res
            res = (low + high) / 2
        return res
                
#
# Newton method. Specify the decimal precision.
# Run Time on LeetCode: 59ms
#
class Solution2(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        iter_count = 0
        res = x
        while res>0:
            iter_count += 1
            if int(res * res) == x:
                print "iterator count: %d, result: %d" % (iter_count, res)
                return int(res)
            else:
                res = (res + x / res) / 2.0
        return x

#
# Binary method. Specify the decimal precision.
#
class Solution3(object):
    def mySqrt(self, x, decimal_prec):
        """
        :type x: int
        :type prec: float
        :rtype: float
        """
        low = float(0)
        res = high = float(x)
        iter_count = 0
        while res>0:
            iter_count += 1
            sqr = res * res
            if math.fabs(sqr - x) <= 10 ** (-decimal_prec-1):
                res = round(res,decimal_prec)
                print "iterator count: %d, result: %s" % (iter_count, res)
                return res
            elif sqr > x:
                high = res
            else:
                low = res
            res = (low + high) / 2
        return res

#
# Newton method. Specify the decimal precision.
#
class Solution4(object):
    def mySqrt(self, x, decimal_prec):
        """
        :type x: int
        :type prec: float
        :rtype: float
        """
        iter_count = 0
        res = float(x)
        while res>0:
            iter_count += 1
            sqr = res * res
            if math.fabs(sqr - x) <= 10 ** (-decimal_prec-1):
                res = round(res,decimal_prec)
                print "iterator count: %d, result: %s" % (iter_count, res)
                return res
            else:
                res = (res + x / res) / 2
        return res


if __name__ == "__main__":
    test_cases = [0, 1, 2, 3, 4, 5, 6, 9, 10, 16, 25, 26]
    test_cases = [20000]

    # Solution1: Binary method. Use default precision "1."
    print 'Solution1: Binary method. Use default precision "1."'
    solu = Solution1()
    for x in test_cases:
        print "sqrt(%d) = %d" % (x, solu.mySqrt(x))
    print ""

    # Solution2: Newton method. Use default precision "1."
    print 'Solution2: Newton method. Use default precision "1."'
    solu = Solution2()
    for x in test_cases:
        print "sqrt(%d) = %s" % (x, solu.mySqrt(x))
    print ""


    decimal_prec = 2

    # Solution3: Binary method. Specify the decimal precision through an argument.
    print 'Solution3: Binary method. Specify the decimal precision through an argument.'
    solu = Solution3()
    for x in test_cases:
        print "sqrt(%d) = %s" % (x, solu.mySqrt(x, decimal_prec))
    print ""

    # Solution4: Newton method. Specify the decimal precision through an argument.
    print 'Solution4: Newton method. Specify the decimal precision through an argument.'
    solu = Solution4()
    for x in test_cases:
        print "sqrt(%d) = %s" % (x, solu.mySqrt(x, decimal_prec))
    print ""
