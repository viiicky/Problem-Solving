"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    '''
    if not head:
        return False
    
    current = head
    current.flag = False
    
    while current.next:
        if current:
            return True
        current.flag = True
        current = current.next
        
    return False
    '''
    
    currentNode = head
    
    for _ in range(101):
        if not currentNode:
            return False
        currentNode = currentNode.next
        
    return True
    

