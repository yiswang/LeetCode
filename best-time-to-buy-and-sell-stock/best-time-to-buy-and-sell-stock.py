#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        best-time-to-buy-and-sell-stock.py
# Create Date: 2017-02-06
# Usage:       best-time-to-buy-and-sell-stock.py
# Description:
#
# LeetCode problem 121. Best Time to Buy and Sell Stock
#
# Difficulty: Easy
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# If you were only permitted to complete at most one transaction (ie, buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
# 
# Example 1: Input: [7, 1, 5, 3, 6, 4] Output: 5
# 
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger
# than buying price)
#
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
# 
# In this case, no transaction is done, i.e. max profit = 0.
#
###############################################################################

#
# Just traverse the price list one time. Record the current minimum price and
# maximum profit; compute prices[i] - minimum price and compare it with the
# current maximum profit in each loop. The time complexity is O(n).
#
# Run time on LeetCode: 42ms, beat 94.67%; 45ms, beat 88.63%
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
        min_price = prices[0]
        for i in xrange(1, len(prices)):
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
            if prices[i] < min_price:
                min_price = prices[i]
        return max_profit


if __name__ == "__main__":
    import time

    test_cases = [
        [],
        [1],
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3],
        [1, 2, 3, 4, 5],
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
