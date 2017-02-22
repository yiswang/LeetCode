#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        invert-binary-tree.py
# Create Date: 2017-02-22
# Usage:       invert-binary-tree.py
# Description:
#
# LeetCode problem 226. Invert Binary Tree Add to List
#
# Difficulty: Easy
#
# Invert a binary tree.
# 
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
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
# Recursive method.
# Run time on LeetCode: 49ms, beat 29.63%; 46ms, beat 40.74%
#
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


#
# DFS method.
# Run time on LeetCode: 48ms, beat 37.59%
#
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.extend([node.left, node.right])
                node.left, node.right = node.right, node.left
        return root


#
# BFS method.
# Run time on LeetCode: 52ms, beat 22.47%
#
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                queue.extend([node.left, node.right])
                node.left, node.right = node.right, node.left
        return root


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
        print levelOrderTraverse(root)
        root = solu.invertTree(root)
        print levelOrderTraverse(root)
        print ""


