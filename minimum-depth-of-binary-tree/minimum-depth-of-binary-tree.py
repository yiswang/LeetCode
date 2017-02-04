#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        minimum-depth-of-binary-tree.py
# Create Date: 2017-02-04
# Usage:       minimum-depth-of-binary-tree.py
# Description:
#
# LeetCode problem 111. Minimum Depth of Binary Tree
#
# Difficulty: Easy
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
###############################################################################

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 
# A DFS recursive method. 
# Run time on LeetCode: 105ms, beat 8.70%; 72ms, beat 56.57%
#
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left_mindepth = right_mindepth = float("inf")
        if root.left:
            left_mindepth = self.minDepth(root.left)
        if root.right:
            right_mindepth = self.minDepth(root.right)
        return min(left_mindepth, right_mindepth) + 1

# 
# A BFS + queue non-recursive method. 
# Run time on LeetCode: 59ms, beat 94.20%; 72ms, 56.57%, 65ms, 81.05%
#
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]
        depth = 1
        queue_nodes_number = 1
        while True:
            count = 0
            for _ in xrange(queue_nodes_number):
                node = queue.pop(0)
                left_node = node.left
                right_node = node.right
                if not left_node and not right_node:
                    return depth
                else:
                    if left_node:
                        queue.append(left_node)
                        count += 1
                    if right_node:
                        queue.append(right_node)
                        count += 1
            queue_nodes_number = count
            depth += 1


if __name__ == "__main__":
    test_cases = [
        None,
        TreeNode(0),
    ]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
#     root.right.left = TreeNode(3)
#     root.right.right = TreeNode(3)
#     root.right.right.left = TreeNode(4)
    test_cases.append(root)

    root = TreeNode(1)
    root.left = TreeNode(2)
    test_cases.append(root)


    solu = Solution()
    for root in test_cases:
        print solu.minDepth(root)
    print ""


