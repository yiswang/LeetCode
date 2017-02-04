#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        path-sum.py
# Create Date: 2017-02-04
# Usage:       path-sum.py
# Description:
#
# LeetCode problem 112. Path Sum
#
# Difficulty: Easy
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# 
###############################################################################

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 
# A DFS and bottom-up method. Use the Inorder Traversal.
# Run time on LeetCode: 89ms, beat 19.12%; 59ms, beat 97.04%
#
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        new_sum = sum - root.val
        return self.hasPathSum(root.left, new_sum) or self.hasPathSum(root.right, new_sum)


if __name__ == "__main__":
    test_cases = [
        (None, 0),
        (TreeNode(0), 0),
    ]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(4)
#     root.right.left = TreeNode(3)
#     root.right.right = TreeNode(3)
#     root.right.right.left = TreeNode(4)
    test_cases.append((root, 6))

    root = TreeNode(1)
    root.left = TreeNode(2)
    test_cases.append((root, 3))


    solu = Solution()
    for root, sum in test_cases:
        print solu.hasPathSum(root, sum)
    print ""


