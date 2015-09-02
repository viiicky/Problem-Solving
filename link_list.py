#!/usr/bin/env python3
# Implement list data structure.
# Vikas Prasad

class link:
    '''Implement link.'''

    def __init__(self, key=None):
        self.key = key
        self.nxt = None
        self.prev = None

    def __gt__(self, other):
        return self.key > other.key

    def __str__(self):
        '''Print link.'''
        if self:
            return str(self.key)
        else:
            return '/'

class lList:
    '''Implement list of links.'''

    def __init__(self):
        self._head = None
        self._numberOfLinks = 0

    def list_insert(self, x):
        '''Insert link x at the beginning of list.'''
        x.nxt = self._head
        if self._head:
            self._head.prev = x
        self._head = x
        self._numberOfLinks += 1

    def get_data(self, position):
        '''Return link from list at position position from head.'''
        i = 0
        temp = self._head
        while i < position:
            temp = temp.nxt
            i += 1
        return temp

    def set_data(self, position, newLink):
        '''Overwrite link at position distance from head of list with newLink.'''
        i = 0
        temp = self._head
        while i < position:
            temp = temp.nxt
            i += 1

        newLink.nxt = temp.nxt  # create connection newLink--->
        if temp.nxt:    # if not last link, we need to create the backward connection too.
            temp.nxt.prev = newLink     # i.e. creating connection newLink<--- 
        if temp.prev:   # if not first link, then
            temp.prev.nxt = newLink     # create connection --->newLink
        else:   # if first link, then
            self._head = newLink        # make the newLink head of list
        newLink.prev = temp.prev        # create connection <---newLink

    def __getitem__(self, position):
        '''This piece of code is derived from stackoverflow. Actually written by someone called Walter Nissen.'''
        if type(position) is slice:
            return [self[i] for i in range(*position.indices(len(self)))]
        elif type(position) is int:
            if position < 0:
                position += len(self)   # handle negative indices
            if position >= len(self):
                raise IndexError("The index (%d) is out of range."%position)
            return self.get_data(position)
        else:
            raise TypeError("Invalid argument type.")

    def __setitem__(self, position, value):
        value = link(value.key) # it removes the prev and nxt links from value, thus making it a standalone link
        self.set_data(position, value)

    def __len__(self):
        return self._numberOfLinks

    def __str__(self):
        '''Print list of links.'''
        listFormat = ''
        temp = self._head
        while temp:
            listFormat += str(temp) + ' '
            temp = temp.nxt
        else:
            listFormat += '/ '
        return listFormat
