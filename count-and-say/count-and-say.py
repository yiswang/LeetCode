#!/usr/bin/python

###############################################################################
#
# LeetCode 38. Count and Say
# 
#     Difficulty: Easy
# 
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 
# 1 is read off as "one 1" or 11.  11 is read off as "two 1s" or 21.  21 is
# read off as "one 2, then one 1" or 1211.
# 
# Given an integer n, generate the nth sequence.
# 
# Note: The sequence of integers will be represented as a string. 
# 
###############################################################################

# A recursive method
class Solution2(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""
        if n == 1:
            return "1"
        lastSeq = self.countAndSay(n-1)
        seq = ""
        ch = lastSeq[0]
        count = 1
        i = 1
        while i < len(lastSeq):
            if lastSeq[i] == ch:
                count += 1
            else:
                seq += str(count) + ch
                ch = lastSeq[i]
                count = 1
            i += 1
        seq += str(count) + ch
        return seq

# A non-recursive method
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""
        lastN = 1
        seq = lastSeq = "1"
        while lastN < n:
            seq = ""
            ch = lastSeq[0]
            count = 1
            i = 1
            while i < len(lastSeq):
                if lastSeq[i] == ch:
                    count += 1
                else:
                    seq += str(count) + ch
                    ch = lastSeq[i]
                    count = 1
                i += 1
            seq += str(count) + ch
            lastSeq = seq
            lastN += 1
        return seq

if __name__ == "__main__":
    numbers = range(10)
    solu = Solution()
    for n in numbers:
        print solu.countAndSay(n)
