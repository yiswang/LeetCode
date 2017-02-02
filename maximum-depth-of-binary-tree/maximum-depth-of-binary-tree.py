#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        maximum-depth-of-binary-tree.py
# Create Date: 2017-02-2
# Usage:       maximum-depth-of-binary-tree.py
# Description:
#
# LeetCode problem 104. Maximum Depth of Binary Tree
# 
# Difficulty: Easy
# 
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
###############################################################################

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# A recursive method.
# Run time on LeetCode: 72ms, beat 38%; 62ms, beat 70.9%
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return leftDepth + 1 if leftDepth > rightDepth else rightDepth + 1

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
        print solu.maxDepth(root)
    print ""


