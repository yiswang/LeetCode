#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        binary-tree-paths.py
# Create Date: 2017-02-24
# Usage:       binary-tree-paths.py
# Description:
#
# LeetCode problem 257. Binary Tree Paths Add to List
#
# Difficulty: Easy
#
# Given a binary tree, return all root-to-leaf paths.
# 
# For example, given the following binary tree:
# 
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
# 
# ["1->2->5", "1->3"]
#
###############################################################################

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
# Method 1. Recursively.
# Run time on LeetCode: 78ms, beat 8.50%
#
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return ["{}".format(root.val)]
        paths = []
        if root.left:
            leftPaths = self.binaryTreePaths(root.left)
            for path in leftPaths:
                newPath = "{}->".format(root.val) + path
                paths.append(newPath)
        if root.right:
            rightPaths = self.binaryTreePaths(root.right)
            for path in rightPaths:
                newPath = "{}->".format(root.val) + path
                paths.append(newPath)
        return paths


#
# Method 2. dfs + stack
# Run time on LeetCode: 48ms, beat 77.79%
#
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        paths, stack = [], [(root, "")]
        while stack:
            node, path = stack.pop()
            newPath = path + "{}".format(node.val)
            if not node.left and not node.right:
                paths.append(newPath)
            if node.right:
                stack.append((node.right, newPath+"->"))
            if node.left:
                stack.append((node.left, newPath+"->"))
        return paths

#
# Method 3. bfs + queue
# Run time on LeetCode: 52ms, beat 51.38%
#
class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        paths, queue = [], [(root, "")]
        while queue:
            node, path = queue.pop(0)
            if not node.left and not node.right:
                paths.append(path+str(node.val))
            if node.left:
                queue.append((node.left, path+str(node.val)+"->"))
            if node.right:
                queue.append((node.right, path+str(node.val)+"->"))
        return paths


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
        res = solu.binaryTreePaths(root)
        print res
        print ""    
