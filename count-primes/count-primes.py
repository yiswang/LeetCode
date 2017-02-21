#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        count-primes.py
# Create Date: 2017-02-20
# Usage:       count-primes.py
# Description:
#
# LeetCode problem 204. Count Primes Add to List
#
# Difficulty: Easy
#
# Description:
# 
# Count the number of prime numbers less than a non-negative number, n.
#
###############################################################################

# Run time on LeetCode: Time Limit Exceeded.
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        if n == 3:
            return 1
        primes = [2, 3]
        index = 0
        maxTestNum = primes[index]
        count = 2
        for num in xrange(4, n):
            if primes[index+1] ** 2 <= num:
                index += 1
                maxTestNum = primes[index]
            flag = True
            for m in xrange(2, maxTestNum+1):
                if num % m == 0:
                    flag = False
                    break
            if flag == True:
                count += 1
                primes.append(num)
        return count


# Run time on LeetCode: 1082ms, beat 55.57%
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        isPrimes = [True] * n
        for i in xrange(2, n):
            if isPrimes[i]:
                for j in xrange(i*i, n, i):
                    isPrimes[j] = False
        return len(filter(lambda x: x, isPrimes)) - 2
        

if __name__ == "__main__":
    test_cases = range(0, 20)
    solu = Solution()
    for num in test_cases:
        res = solu.countPrimes(num)
        print "num: %d, res: %d" % (num, res)
