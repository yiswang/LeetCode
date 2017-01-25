#!/usr/bin/python

###############################################################################
#
# LeetCode question 58. Length of Last Word
#
# Difficulty: Easy
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space
# characters only.
# 
# For example, Given s = "Hello World", return 5
#
###############################################################################

class Solution1(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        i = 0
        while i < len(s):
            ch = s[i]
            if ch == " " or ch == "\t" or ch == "\r" or ch == "\n":
                while i < len(s):
                    ch = s[i]
                    if not (ch == " " or ch == "\t" or ch == "\r" or ch == "\n"):
                        count = 1
                        break
                    i += 1
            else:
                count += 1
            i += 1
        return count
        

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        l = len(s)
        i = l - 1
        end_index = 0
        ch = s[i]
        while i >= 0 and (ch == " " or ch == "\t"):
            i -= 1
            ch = s[i]
        if i < 0:
            return 0
        end_index = i
        while i >= 0 and not (ch == " " or ch == "\t"):
            i -= 1
            ch = s[i]
        if i < 0:
            return end_index + 1
        else:
            return end_index - i


if __name__ == "__main__":
    test_cases = [
        "abc",
        "   abc",
        "abc   ",
        "Hello World",        
        "Hello   World",        
        "Hello   World 3rd",        
        "Hello\tWorld",        
        "Hello\t\t\tWorld",        
        "Hello\t\tWorld",        
        "Hello World ",        
        "Hello World  ",        
        "Hello World \t",        
        " ",        
        "",        
    ]

    solu = Solution()
    for s in test_cases:
        res = solu.lengthOfLastWord(s)
        print res

