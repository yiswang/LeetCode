#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        same-tree.py
# Create Date: 2017-01-30
# Usage:       same-tree.py
# Description:
#
# LeetCode problem 100. Same Tree
# 
# Difficulty: Easy
# 
# Given two binary trees, write a function to check if they are equal or not.
# 
# Two binary trees are considered equal if they are structurally identical and
# the nodes have the same value.
# 
###############################################################################

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
# A recursive method.
# Run time on LeetCode: 49ms. Beat 28.77%
#
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        if p.val == q.val and \
            self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right):
            return True
        else:
            return False

if __name__ == "__main__":
    test_cases = [
        (None, None),
        (None, TreeNode(0)),
        (TreeNode(0), None),
        (TreeNode(0), TreeNode(0)),
        (TreeNode(0), TreeNode(1)),
    ]

    solu = Solution()
    for p, q in test_cases:
        print solu.isSameTree(p, q)
    print ""
