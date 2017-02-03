#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        balanced-binary-tree.py
# Create Date: 2017-02-03
# Usage:       balanced-binary-tree
# Description:
#
# LeetCode problem 110. Balanced Binary Tree
#
# Difficulty: Easy
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
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
# This is a DFS recursive method. The time complexity is O(N).
# Run time on LeetCode: 89ms, beat 59.13%; 76ms, beat 80.68%
#
class Solution(object):
    def isBalanced_helper(self, root):
        if not root:
            return (0, True)
        (left_depth, left_balance) = self.isBalanced_helper(root.left)
        (right_depth, right_balance) = self.isBalanced_helper(root.right)
        return (max(left_depth, right_depth) + 1,
            (-1 <= left_depth - right_depth <= 1) and left_balance and right_balance)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBalanced_helper(root)[1]


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
    root.left.left.left = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    test_cases.append(root)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    test_cases.append(root)


    solu = Solution()
    for root in test_cases:
        print solu.isBalanced(root)
    print ""


