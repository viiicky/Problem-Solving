#!/usr/bin/env python3
# Implements heap data structure along with various methods including heap-sort, another comparison sorting method.
# Heap-Sort Running Time: O(n lgn)
# Its running time is smae as merge sort, but it has one advantage over it, which is,
# unlike merge sort it sorts the list in place.
# by Vikas Prasad
from math import ceil

class heap:
    '''Implement heap data structure and relevent methods.'''

    def __init__(self, A, n=0):
        '''Create a heap of size n from A, if n is not given create a zero element heap instead.'''
        self._A = A
        self._heapSize = n

    def get_heap_size(self):
        return self._heapSize

    def parent(self, i):
        return ceil(i/2) - 1

    def left(self, i):
        return (i<<1) + 1

    def right(self, i):
        return (i<<1) + 2

    def max_heapify(self, i):
        '''Assume that subtrees rooted at left(i) and right(i) are max heaps,
        make subtree rooted at i a max heap.
        '''
        l = self.left(i)
        r = self.right(i)

        if l < self._heapSize and self._A[l] > self._A[i]:
            largest = l
        else:
            largest = i
        if r < self._heapSize and self._A[r] > self._A[largest]:
            largest = r

        if largest != i:
            self._A[i], self._A[largest] = self._A[largest], self._A[i]
            self.max_heapify(largest)

    def min_heapify(self, i):
        '''Assume that subtrees rooted at left(i) and right(i) are min heaps,
        make subtree rooted at i a min heap.
        '''
        l = self.left(i)
        r = self.right(i)

        if l < self._heapSize and self._A[l] < self._A[i]:
            smallest = l
        else:
            smallest = i
        if r < self._heapSize and self._A[r] < self._A[smallest]:
            smallest = r

        if smallest != i:
            self._A[i], self._A[smallest] = self._A[smallest], self._A[i]
            self.min_heapify(smallest)

    def iterative_max_heapify(self, i):
        '''Assume that subtrees rooted at left(i) and right(i) are max heaps,
        make subtree rooted at i a max heap.
        '''
        while True:
            l = self.left(i)
            r = self.right(i)

            if l < self._heapSize and self._A[l] > self._A[i]:
                largest = l
            else:
                largest = i
            if r < self._heapSize and self._A[r] > self._A[largest]:
                largest = r

            if largest == i:
                return

            self._A[i], self._A[largest] = self._A[largest], self._A[i]
            i = largest

    def build_max_heap(self):
        '''Build heap from unordered list A.'''
        self._heapSize = len(self._A)   # setting the heap size as the size of A
        
        n = len(self._A) - 1      # index of last element
        lastParentPosition = self.parent(n)       # index of parent of last node, i.e. index of the last parent

        # as all leaf nodes are already max-heap, starting from last parent all the way up to root
        for i in reversed(range(lastParentPosition+1)):
            self.max_heapify(i)

    def heapsort(self):
        '''Sort A using heap sort.'''
        self.build_max_heap()
        for i in reversed(range(1, len(self._A))):
            self._A[i], self._A[0] = self._A[0], self._A[i]
            self._heapSize -= 1
            self.max_heapify(0)
            
    def heap_maximum(self):
        '''Return the maximum element from the max-heap'''
        return self._A[0]

    def heap_extract_max(self):
        '''Return and remove the maximum element from the max-heap'''
        if self._heapSize < 1:
            exit('heap underflow')
        maximum = self._A[0]
        self._A[0] = self._A[self._heapSize - 1]
        self._heapSize -= 1
        self.max_heapify(0)
        return maximum

    def heap_increase_key(self, i, key):
        '''Increase the element at i in max-heap, by updating the element with key, if key is greater or equal to A[i],
        and then move it to correct position in the heap and then return that new position.
        '''
        if key < self._A[i]:
            exit('new key is smaller than current key')

        # this piece works like insertion sort, i.e. shifting in a series and then inserting
        while i > 0 and self._A[self.parent(i)] < key:
            self._A[i] = self._A[self.parent(i)]
            i = self.parent(i)
        self._A[i] = key

        # this piece works like bubble sort, i.e. inserting and then swapping in a series
        '''
        self._A[i] = key
        while i > 0 and self._A[self.parent(i)] < self._A[i]:
            self._A[self.parent(i)], self._A[i] = self._A[i], self._A[self.parent(i)]
            i = self.parent(i)
        '''

        return i

    def max_heap_insert(self, key):
        '''Insert the element with key in max-heap at the proper position and return that position.'''
        self._heapSize += 1
        if self._heapSize > len(self._A):
            self._A.append(None)
        self._A[self._heapSize - 1] = float('-Infinity')
        position = self.heap_increase_key(self._heapSize-1, key)
        return position

    def max_heap_delete(self, i):
        '''Delete the element at i from max-heap and return it.'''
        temp = self._A[i]
        self._A[i] = self._A[self._heapSize - 1]
        self._heapSize -= 1
        self.max_heapify(i)
        return temp

    def heap_minimum(self):
        '''Return minimum element from min-heap.'''
        return self._A[0]

    def heap_extract_min(self):
        '''Remove and return minimum element from min-heap.'''
        if self._heapSize < 1:
            exit('heap underflow')
        minimum = self._A[0]
        self._A[0] = self._A[self._heapSize - 1]
        self._heapSize -= 1
        self.min_heapify(0)
        return minimum

    def heap_decrease_key(self, i, key):
        '''Decrease the key at i in A, by updating it with key, if key is smaller or equal to A[i].'''
        if key > self._A[i]:
            exit('new key is greater than current key')
        self._A[i] = key
        while i > 0 and self._A[self.parent(i)] > self._A[i]:
            self._A[self.parent(i)], self._A[i] = self._A[i], self._A[self.parent(i)]
            i = self.parent(i)

    def min_heap_insert(self, key):
        '''Insert the key at proper place in min-heap.'''
        self._heapSize += 1
        if self._heapSize > len(self._A):
            self._A.append(None)
        self._A[self._heapSize - 1] = float('Infinity')
        self.heap_decrease_key(self._heapSize-1, key)

    def  heap_get_value(self, i):
        '''Return the value at index i from heap.'''
        return self._A[i]

    def __str__(self):
        '''Show the heap.'''
        string = ''
        for i in range(self._heapSize):
            string += str(self._A[i]) + ' '
        return string

    def show_list(self):
        '''Show the list A, remember it is not affected by heapSize.'''
        print()
        print(self._A)
        print()
 
if __name__ == '__main__':
    # A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    # heap1 = heap(A, len(A))
    # print(heap1)
    # heap1.max_heapify(1)

    # A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    # heap1 = heap(A, len(A))
    # print(heap1)
    # heap1.iterative_max_heapify(2)

    # A = [0, 9, 5, 1, 12, 3, 8, 4, 10, 13, 16, 7, 17, 27]
    # heap1 = heap(A, len(A))
    # print(heap1)
    # heap1.min_heapify(1)
    # print(heap1)
    # print(heap1.heap_minimum())
    # print(heap1.heap_extract_min())

    # A = [0, 9, 5, 1, 12, 3, 8, 4, 10, 13, 16, 7, 17, 27]
    # heap1 = heap(A, len(A))
    # print(heap1)
    # heap1.min_heapify(1)
    # print(heap1)
    # heap1.heap_decrease_key(13, 0)

    # A = [0, 9, 5, 1, 12, 3, 8, 4, 10, 13, 16, 7, 17, 27]
    # heap1 = heap(A, len(A))
    # print(heap1)
    # heap1.min_heapify(1)
    # print(heap1)
    # heap1.min_heap_insert(4)

    # A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    # heap1 = heap(A)
    # print(heap1)
    # heap1.build_max_heap()

    # A = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    # A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
    # heap1 = heap(A)
    # print(heap1)
    # heap1.build_max_heap()
    # print(heap1)
    # print(heap1.heap_maximum())
    # print(heap1.heap_extract_max())

    # A = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
    # heap1 = heap(A, len(A))
    # print(heap1)
    # heap1.max_heap_insert(10)

    # A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    # heap1 = heap(A)
    # print(heap1)
    # heap1.heapsort()
    # heap1.show_list()

    # A = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    # heap1 = heap(A)
    # print(heap1)
    # heap1.heapsort()
    # heap1.show_list()

    A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    heap1 = heap(A, len(A))
    print(heap1)
    heap1.heap_increase_key(8, 15)
    pos = heap1.max_heap_insert(13)
    heap1.max_heap_delete(pos)

    print(heap1)
