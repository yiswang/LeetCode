#! /usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        convert-sorted-array-to-binary-search-tree.py
# Create Date: 2017-02-03
# Usage:       convert-sorted-array-to-binary-search-tree.py
# Description:
#
# LeetCode problem 108. Convert Sorted Array to Binary Search Tree
#
# Difficulty: Easy
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
# 
###############################################################################

def levelOrderTraverse(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    queue = [root]
    result = []
    max_number = 1
    while queue:
        nodes_cur_level = []
        count = 0
        next_max_number = 0
        while count < max_number:
            node = queue.pop(0)
            if node:
                nodes_cur_level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                nodes_cur_level.append(None)
                queue.append(None)
                queue.append(None)
            next_max_number += 2
            count += 1
        if len(set(nodes_cur_level)) == 1 and \
            list(set(nodes_cur_level))[0] == None:
            break
        result.append(nodes_cur_level)
        max_number *= 2
    return result


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
# A recursive method.
# Run time on LeetCode: 122ms, beat 16.44%; 95ms, beat 78.99%
#
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        low, high = 0, len(nums) - 1
        mid = (low + high) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:high+1])
        return root


if __name__ == "__main__":
    test_cases = [
        [1],
        [1,2],
        [1,2,3],
        [1,2,3,4],
        [1,2,3,4,5,6,7,8,9,10,11],
    ]

    solu = Solution()
    for nums in test_cases:
        res = solu.sortedArrayToBST(nums)
        print levelOrderTraverse(res)
    print ""

