#!/usr/bin/env python3
# Implements FIFO queue with a Priority Queue
# by Vikas Prasad

try:
    from heap import *
except ImportError as e:
    # print(e)
    print('Module heap is required for this script.')
    print('You can download the same at: ')
    print('https://github.com/viiicky/Interview-Preparation/blob/master/heap.py')
    exit()

class data:
    '''Implement data for storing elemets of queue in x and their priority in priority.'''

    def __init__(self, x, p):
        self._x = x
        self._priority = p

    def __gt__(self, other):
        if type(other) is data:
            other = other._priority
        return self._priority > other
    
    def __lt__(self, other):
        if type(other) is data:
            other = other._priority
        return self._priority < other

    def __str__(self):
        return str(self._x)

class queue(float):
    '''Implemets FIFO queue using a min-heap priority queue.'''

    def __init__(self):
        Q = []
        self._Q = heap(Q)      # this heap will contain the queue elements

        self._p = -1 # instance variable for setting priority for each element
        # a better approach would be perhaps setting the current timestmap as the priority.
        # as time never goes back

    def enqueue(self, x):
        '''Add x to the end of Q with its priority value greater than priority value of last element inserted.
        Remember we are using a min-heap, thus a lower priority value element has actually greater priority.
        '''
        self._p += 1
        d = data(x, self._p)
        self._Q.min_heap_insert(d)
        print(x, 'enqueued')

    def dequeue(self):
        '''Remove the element that had been longest in the Q.'''
        temp = self._Q.heap_extract_min()
        return temp
        
if __name__ == '__main__':
    queue1 = queue()
    queue1.enqueue(15)
    queue1.enqueue(6)
    queue1.enqueue(9)
    queue1.enqueue(8)
    queue1.enqueue(4)

    queue1.enqueue(17)
    queue1.enqueue(3)
    queue1.enqueue(5)

    print(queue1.dequeue())
    queue1.enqueue(17)
    queue1.enqueue(3)
    queue1.enqueue(5)

    print(queue1.dequeue())
    print(queue1.dequeue())
    print(queue1.dequeue())
    print(queue1.dequeue())
    print(queue1.dequeue())
    print(queue1.dequeue())
    print(queue1.dequeue())
    print(queue1.dequeue())
    print(queue1.dequeue())
    print(queue1.dequeue())
