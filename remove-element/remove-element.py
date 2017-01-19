#!/usr/bin/python

###############################################################################
#
# LeetCode 27. Remove Element
#
# Difficulty: Easy
#
# Given an array and a value, remove all instances of that value in place and
# return the new length.
# 
# Do not allocate extra space for another array, you must do this in place with
# constant memory.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond
# the new length.
# 
# Example: Given input array nums = [3,2,2,3], val = 3
# 
#     Your function should return length = 2, with the first two elements of
#     nums being 2.
#
# Hint:
# 
#     Try two pointers.
#     Did you use the property of "the order of elements can be changed"?
#     What happens when the elements to remove are rare?
#
###############################################################################

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i<=j:
            while i<=j and nums[i] != val:
                i += 1
            while i<=j and nums[j] == val:
                j -= 1
            if i <= j:
                nums[i] = nums[j]
                j -= 1
        return i


if __name__ == "__main__":
    test_cases = [
        ([],3),
        ([2],3),
        ([3],3),
        ([3,3], 3),
        ([3,2], 3),
        ([3,3,3], 3),
        ([3,2,3], 3),
        ([3,2,2], 3),
        ([2,3], 3),
        ([2,2], 3),
        ([2,2,3], 3),
        ([2,3,2], 3),
        ([2,3,2,2], 3),
        ([2,2,3,3], 3),
        ([2,2,3,2], 3),
        ([2,3,3,2], 3),
        ([2,3,2,3], 3),
        ([2,3,4,5], 3),
        ([2,3,4,3], 3),
        ([1,2,3,4,5], 3),
        ([1,2,4,5], 3),
    ]
    solu = Solution()
    for nums, val in test_cases:
        result = solu.removeElement(nums, val)
        print result
