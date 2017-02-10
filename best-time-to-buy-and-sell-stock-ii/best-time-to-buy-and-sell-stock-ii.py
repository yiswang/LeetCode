#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        best-time-to-buy-and-sell-stock-ii.py
# Create Date: 2017-02-07
# Usage:       best-time-to-buy-and-sell-stock-ii.py
# Description:
#
# LeetCode problem 122. Best Time to Buy and Sell Stock II
#
# Difficulty: Easy
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times). However, you may not engage in multiple transactions at the
# same time (ie, you must sell the stock before you buy again).
#
###############################################################################

#
# Just traverse the price list one time. The time complexity is O(n).
#
# Basic idea:
# 1. See this price sequence: a, b, c, where c > a and c > b,
#    If b <= a, max profit for this sequence should be c - b, otherwise, it
#    should be c - a; So when there is a sequence like a, b1, b2, ..., bn, c,
#    where bn <= b(n-1) <= b1 <= a, the max profit for it should be c - bn
# 2. See this price sequence: a, b1, b2, ..., bn, where bn > ... > b1 > a,
#    The same as the case 1, the max profit for it should be bn - a
# 3. Now see another price sequence: a, b, c, d, where b > a, d > c and d > a
#    Obviously, the max profit can probably be d - a or (b - a) + (d - c).
#    If b <= c, then b - a + d - c >= d - a, the max profit should be b - a + d
#    - c; Otherwise, this case is the same as case 2, the max profit should be d
#    - a. Then, consider the following price values in the sequence: c, d, e, f,
#    ..., it's the same as case 3.
# According to above analysis, I have the following code to solve this problem.
#
# Run time on LeetCode: 43ms, beat 89.80%; 58ms, beat 30.70%
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0
        cur_max_profit = 0
        cur_min_price = prices[0]
        cur_max_price = 0
        for i in xrange(1, len(prices)):
            if prices[i] <= cur_max_price:
                max_profit += cur_max_profit
                cur_max_profit = 0
                cur_min_price = prices[i]
                cur_max_price = 0
            elif prices[i] <= cur_min_price:
                cur_min_price = prices[i]
            else:
                cur_max_price = prices[i]
                cur_max_profit = prices[i] - cur_min_price
        return max_profit + cur_max_profit


if __name__ == "__main__":
    import time

    test_cases = [
        [],
        [1],
        [7, 6, 4, 3],
        [7, 1, 5, 3, 6, 4],
        [7, 3, 5, 1, 6, 4],
        [7, 3, 2, 5, 1, 6, 4],
        [1, 2, 3, 4, 5],
        [6,1,3,2,4,7],
    ]

    solu = Solution()
    start_t = time.clock()
    for prices in test_cases:
        print prices
        res = solu.maxProfit(prices)
        print res
        print ""
    end_t = time.clock()
    print "cpu time: %s" % (end_t - start_t)
    print ""
