#!/usr/bin/python

###############################################################################
#
# LeetCode question 6. ZigZag Conversion
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
#     string convert(string text, int nRows);
#
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
#
###############################################################################

import pdb
import math 

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        pdb.set_trace()

        if 0 >= numRows:
            return ""

        if 1 == numRows:
            return s

        numCharsPerUnit = numRows * 2 - 2
        numUnits = math.ceil(len(s) / float(numCharsPerUnit))
        numChars = len(s)

        s2 = ""
        for row in xrange(0, numRows):
            first_idx = row
            if 0 == row or (numRows-1) == row:
                idx = first_idx
                while idx < numChars:
                    s2 += s[idx]
                    idx += numCharsPerUnit
            else:
                for i in xrange(0, int(numUnits)):
                    idx = first_idx
                    if idx < numChars:
                        s2 += s[idx]
                        idx += (numRows - 1 - row) * 2
                        if idx < numChars:
                            s2 += s[idx]
                    first_idx += numCharsPerUnit

        return s2


            
class Solution1(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        pdb.set_trace()


        if 0 >= numRows:
            return ""

        if 1 == numRows:
            return s

        numCharsPerUnit = numRows * 2 - 2
        numUnits = math.ceil(len(s) / float(numCharsPerUnit))
        numColsPerUnit = numRows - 1
        numCharsLastUnit = len(s) % numCharsPerUnit
        if 0 == numCharsLastUnit:
            numColsLastUnit = numCharsPerUnit
        elif numRows >= numCharsLastUnit:
            numColsLastUnit = 1
        else:
            numColsLastUnit = numCharsPerUnit - numRows + 1

        numCols = (numUnits - 1) * numColsPerUnit + numColsLastUnit
        numCols = int(numCols)

        l = [0] * (numRows * numCols)
        for k in xrange(0, len(s)):
            firstCol = k / numCharsPerUnit * numColsPerUnit
            char_offsite = k % numCharsPerUnit
            offsite = char_offsite + 1 - numRows
            if 0 >= offsite:
                row = char_offsite
                col = firstCol
            else:
                row = numRows - 1 - offsite
                col = firstCol + offsite

            l[row * numCols + col] = s[k]

        retS = ""
        for elem in l:
            if not 0 == elem:
                retS += elem
        return retS
            

if __name__ == "__main__":
    s1 = "PAYPALISHIRINGNG"
    numRows = 4
    solu1 = Solution()
    res = solu1.convert(s1, numRows)
    print res
