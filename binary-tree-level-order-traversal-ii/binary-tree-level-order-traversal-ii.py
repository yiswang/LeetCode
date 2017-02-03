#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        binary-tree-level-order-traversal-ii.py
# Create Date: 2017-02-03
# Usage:       binary-tree-level-order-traversal-ii.py
# Description:
#
# LeetCode problem 107. Binary Tree Level Order Traversal II
#
# Difficulty: Easy
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
# 
###############################################################################

import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
# BFS + Queue
# Run time on LeetCode: 46ms, beat 97.39%; 55ms, beat 57.77%; 82ms, 8.07%
#
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque()
        if root:
            queue.append(root)
        result = []
        max_number = 1
        while queue:
            nodes_cur_level = []
            count = 0
            next_max_number = 0
            while count < max_number:
                node = queue.popleft()
                nodes_cur_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                    next_max_number += 1
                if node.right:
                    queue.append(node.right)
                    next_max_number += 1
                count += 1
            if nodes_cur_level:
                result.insert(0, nodes_cur_level)
            max_number = next_max_number
        return result


if __name__ == "__main__":
    test_cases = [
        None,
        TreeNode(0),
    ]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    test_cases.append(root)

    root = TreeNode(1)
    root.left = TreeNode(2)
    test_cases.append(root)


    solu = Solution()
    for root in test_cases:
        print solu.levelOrderBottom(root)
    print ""
