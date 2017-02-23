#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        lowest-common-ancestor-of-a-binary-search-tree.py
# Create Date: 2017-02-23
# Usage:       ./lowest-common-ancestor-of-a-binary-search-tree.py
# Description:
#
# LeetCode problem 235. Lowest Common Ancestor of a Binary Search Tree Add to
# List
#
# Difficulty: Easy
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.
# 
# According to the definition of LCA on Wikipedia: ¡°The lowest common ancestor
# is defined between two nodes v and w as the lowest node in T that has both v
# and w as descendants (where we allow a node to be a descendant of itself).¡±
# 
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
#
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another
# example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of
# itself according to the LCA definition.
#
###############################################################################

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Run time on LeetCode: 135ms, beat 60.92%; 132ms, beat 65.45%
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root and (p.val - root.val) * (q.val - root.val) > 0:
            root = root.left if p.val < root.val else root.right
        return root


if __name__ == "__main__":
    pass
