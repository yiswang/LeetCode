#!/usr/bin/python

###############################################################################
#
# LeetCode 26. Remove Duplicates from Sorted Array
#
# Difficulty: Easy
#
# Given a sorted array, remove the duplicates in place such that each element
# appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this in place with
# constant memory.
# 
# For example,
# Given input array nums = [1,1,2],
# 
# Your function should return length = 2, with the first two elements of nums
# being 1 and 2 respectively. It doesn't matter what you leave beyond the new
# length.
#
###############################################################################

import pdb

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == []:
            return 0

        i = 0
        for j in xrange(1, len(nums)):
            if not nums[j] == nums[i]:
                nums[i+1] = nums[j]
                i += 1
        return i+1
            

if __name__ == "__main__":
#     pdb.set_trace()

    test_cases = [
        [],
        [1,1,2],
        [1,2,2],
        [1,1,2,2],
        [1,1,2,2,3],
        [1,1,2,2,3,4],
        [1,1,2,2,3,4,4],
        [1,1,2,2,3,4,4,5],
        [1,1,1,2,2,2],
        [1,1,1,2,2,2,3],
        [1,1,1,2,2,2,3,4,5,5,5],
        [1],
        [1,2],
        [1,2,3],
        [1,2,3,4]
    ]

    solu1 = Solution()
    for nums in test_cases:
        res = solu1.removeDuplicates(nums)
        print res
