#!/usr/bin/python

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in xrange(0, len(nums)):
            if not d.has_key(nums[i]):
                d[target - nums[i]] = i
            else:
                return [d[nums[i]], i]


class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(0, len(nums)-1):
            for j in xrange(i+1, len(nums)):
                if target == (nums[i] + nums[j]):
                    return [i,j]


if __name__ == "__main__":
    nums = [1, 2, 7, 9]
    target = 9
    s1 = Solution()
    result = s1.twoSum(nums, target)
    print result
