#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        path-sum-ii.py
# Create Date: 2017-02-04
# Usage:       path-sum-ii.py
# Description:
#
# LeetCode problem 113. Path Sum II
#
# Difficulty: Easy
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
# 
# For example:
#
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
# 
###############################################################################

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 
# Inorder traverse by using DFS + recursive method.
# Pass two list parameter to the recursive function. One stores the current
# path, and the other one stores the final results.
#
# Run time on LeetCode: 72ms, beat 84.99%
#
class Solution(object):
    def pathSumHelper(self, root, sum, cur_path, final_paths):
        if not root:
            return
        if not root.left and not root.right:
            if sum == root.val:
                final_paths.append(cur_path + [root.val])
            return
        cur_path.append(root.val)
        new_sum = sum - root.val
        self.pathSumHelper(root.left, new_sum, cur_path, final_paths)
        self.pathSumHelper(root.right, new_sum, cur_path, final_paths)
        cur_path.pop()

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        cur_path = []
        final_paths = []
        self.pathSumHelper(root, sum, cur_path, final_paths)
        return final_paths


# 
# DFS + stack
# Run time on LeetCode: 
#
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return []
        final_paths = []
        stack = [(root, [root.val], root.val)]
        while stack:
            cur_node, cur_path, cur_sum = stack.pop()
            if not cur_node.left and not cur_node.right:
                if cur_sum == sum:
                    final_paths.append(cur_path)
            if cur_node.right:
                stack.append((cur_node.right,
                    cur_path + [cur_node.right.val],
                    cur_sum + cur_node.right.val))
            if cur_node.left:
                stack.append((cur_node.left,
                    cur_path + [cur_node.left.val],
                    cur_sum + cur_node.left.val))
        return final_paths


if __name__ == "__main__":
    test_cases = [
        (None, 0),
        (TreeNode(0), 0),
    ]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)
    root.right.right.left = TreeNode(4)
    test_cases.append((root, 10))

    root = TreeNode(1)
    root.left = TreeNode(2)
    test_cases.append((root, 3))


    solu = Solution()
    for root, sum in test_cases:
        print solu.pathSum(root, sum)
    print ""


