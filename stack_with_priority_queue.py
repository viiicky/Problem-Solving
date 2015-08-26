#!/usr/bin/env python3
# Implements stack with a Priority Queue
# by Vikas Prasad
# Date: 26 Ag 2015

try:
    from heap import *
except ImportError as e:
    # print(e)
    print('Module heap is required for this script.')
    print('You can download the same at: ')
    print('https://github.com/viiicky/Algorithms-Python/blob/master/heap.py')
    exit()

class data:
    '''Implement data for storing elemets of stack in x and their priority in priority.'''

    def __init__(self, x, p):
        self._x = x
        self._priority = p

    def __lt__(self, other):
        if type(other) is data:
            other = other._priority
        return self._priority < other

    def __gt__(self, other):
        if type(other) is data:
            other = other._priority
        return self._priority > other
 
    def __str__(self):
        return str(self._x)

class stack:
    '''Implemet stack using a max-heap priority queue.'''

    def __init__(self):
        S= []
        self._S = heap(S)      # this heap will contain the stack elements

        self._p = -1 # instance variable for setting priority for each element
        # a better approach would be perhaps setting the current timestmap as the priority.
        # as time never goes back

    def push(self, x):
        '''Add x to the end of S with its priority value greater than priority value of last element inserted.
        Remember we are using a max-heap, thus a higher priority value element has greater priority.
        '''
        self._p += 1
        d = data(x, self._p)
        self._S.max_heap_insert(d)
        print(x, 'pushed')

    def pop(self):
        '''Remove the element that entered S most recently.'''
        temp = self._S.heap_extract_max()
        return temp

if __name__ == '__main__':
    stack1 = stack()
    stack1.push(15)
    stack1.push(6)
    stack1.push(9)
    stack1.push(8)
    stack1.push(4)

    stack1.push(17)
    stack1.push(3)
    stack1.push(5)

    print(stack1.pop())
    stack1.push(17)
    stack1.push(3)
    stack1.push(5)

    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
