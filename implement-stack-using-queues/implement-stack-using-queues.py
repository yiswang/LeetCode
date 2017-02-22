#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################################
#
# Author:      Yishan Wang <wangys8807@gmail.com>
# File:        implement-stack-using-queues.py
# Create Date: 2017-02-22
# Usage:       implement-stack-using-queues.py
# Description:
#
# LeetCode problem 225. Implement Stack using Queues Add to List
#
# Difficulty: Easy
#
# Implement the following operations of a stack using queues.
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
#
# Notes:
# You must use only standard operations of a queue -- which means only push to
# back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may
# simulate a queue by using a list or deque (double-ended queue), as long as
# you use only standard operations of a queue.  You may assume that all
# operations are valid (for example, no pop or top operations will be called on
# an empty stack).
#
###############################################################################

#
# Method 1. Use two queues, push is O(1), pop and top is O(n).
# Run time on LeetCode: 42ms, beat 50.51%
#
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__queue = [[], []]
        self.activeQueueIdx = 0
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.__queue[self.activeQueueIdx].append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        l = len(self.__queue[self.activeQueueIdx])
        oldQueueIdx = self.activeQueueIdx
        self.activeQueueIdx = (self.activeQueueIdx + 1) % 2
        for _ in xrange(l-1):
            self.__queue[self.activeQueueIdx].append(self.__queue[oldQueueIdx].pop(0))
        return self.__queue[oldQueueIdx].pop(0)
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        element = self.pop()
        self.__queue[self.activeQueueIdx].append(element)
        return element
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.__queue[self.activeQueueIdx]) == 0
        

#
# Method 2. Use one queue, push is O(n), pop and top is O(1).
# Run time on LeetCode: 42ms, beat 50.51%
#
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__queue = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        q = self.__queue
        q.append(x)
        for _ in xrange(len(q) - 1):
            q.append(q.pop(0))

        
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.__queue.pop(0)
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.__queue[0]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.__queue) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    res = obj.pop()
    print res
    res = obj.top()
    print res
    print obj.empty()
    res = obj.pop()
    print res
    print obj.empty()
    pass
