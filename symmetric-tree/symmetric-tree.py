#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        symmetric-tree.py
# Create Date: 2017-01-30
# Usage:       symmetric-tree.py
# Description:
#
# LeetCode problem 101. Symmetric Tree
#
# Difficulty: Easy
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 
# But the following [1,2,2,null,3,null,3] is not:
# 
#     1
#    / \
#   2   2
#    \   \
#    3    3
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively. 
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
# Run time on LeetCode: 46ms. Beat 74.69%
#
class Solution(object):
    def isMirror(self, p, q):
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        return p.val == q.val and \
            self.isMirror(p.left, q.right) and \
            self.isMirror(p.right, q.left)
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return not root or self.isMirror(root.left, root.right)

#
# Non-recursive method 1: Use a common array to store nodes in the same level.
# Run time on LeetCode: Time Limit Exceeded
#
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pre_node_list = [root]
        cur_node_list = []
        length = 1
        while True:
            none_count = 0
            for i in xrange(length):
                if pre_node_list[i]:
                    cur_node_list.append(pre_node_list[i].left)
                    cur_node_list.append(pre_node_list[i].right)
                else:
                    cur_node_list.append(None)
                    cur_node_list.append(None)
                    none_count += 2
            if none_count == length*2:
                break
            for i in xrange(length):
                node1 = cur_node_list[i]
                node2 = cur_node_list[-1-i]
                if not node1 and not node2:
                    continue
                if (node1 and not node2) or (not node1 and node2):
                    return False
                if not node1.val == node2.val:
                    return False
            length *= 2
            pre_node_list = cur_node_list
            cur_node_list = []

        return True


#
# Non-recursive method 2: Use a stack.
# Run time on LeetCode: 42ms, beat 92.84%
#
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = []
        leftNode = root.left
        rightNode = root.right
        if leftNode:
            if not rightNode or rightNode.val != leftNode.val:
                return False
            stack.append(leftNode)
            stack.append(rightNode)
        elif rightNode:
            return False

        while len(stack) != 0:
            leftNode = stack.pop()
            rightNode = stack.pop()
            if leftNode.left:
                if not rightNode.right or rightNode.right.val != leftNode.left.val:
                    return False
                stack.append(leftNode.left)
                stack.append(rightNode.right)
            elif rightNode.right:
                return False

            if leftNode.right:
                if not rightNode.left or rightNode.left.val != leftNode.right.val:
                    return False
                stack.append(leftNode.right)
                stack.append(rightNode.left)
            elif rightNode.left:
                return False
        return True


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
        print solu.isSymmetric(root)
    print ""


