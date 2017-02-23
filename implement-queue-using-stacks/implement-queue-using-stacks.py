#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        implement-queue-using-stacks.py
# Create Date: 2017-02-23
# Usage:       implement-queue-using-stacks.py
# Description:
#
# LeetCode problem 232. Implement Queue using Stacks Add to List
#
# Difficulty: Easy
#
# Implement the following operations of a queue using stacks.
# 
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
#
# Notes:
# You must use only standard operations of a stack -- which means only push to
# top, peek/pop from top, size, and is empty operations are valid.  Depending
# on your language, stack may not be supported natively. You may simulate a
# stack by using a list or deque (double-ended queue), as long as you use only
# standard operations of a stack.  You may assume that all operations are valid
# (for example, no pop or peek operations will be called on an empty queue).
#
###############################################################################

#
# Method 1. Use one extra stack in push method.
# The space complexity and time complexity of the push operation is O(n) and
# O(2n).
#
# Run time on LeetCode: 55ms, beat 13.59%
#
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        tempStack = []
        for _ in xrange(len(self.stack)):
            tempStack.append(self.stack.pop())
        tempStack.append(x)
        for _ in xrange(len(tempStack)):
            self.stack.append(tempStack.pop())
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (not self.stack)


#
# Method 2. Use two stacks: inputStack for push operation, and outputStack for
# peek and pop operations.
# The total space complexity of the two stacks is O(n).
# The time complexity: For push operation, it is O(1). For peek and pop
# operations, it is O(n) only when the outputStack is empty.
#
# Run time on LeetCode: 39ms, beat 87.02%
#
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inputStack = []
        self.outputStack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.inputStack.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        return self.outputStack.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.outputStack:
            for _ in xrange(len(self.inputStack)):
                self.outputStack.append(self.inputStack.pop())
        return self.outputStack[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (not self.inputStack) and (not self.outputStack)
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    res = obj.pop()
    print res
    res = obj.peek()
    print res
    print obj.empty()
    res = obj.pop()
    print res
    print obj.empty()
    pass
