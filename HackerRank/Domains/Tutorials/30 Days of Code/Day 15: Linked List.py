    def insert(self,head,data): 
    #Complete this method
        node = Node(data)
    
        if head == None:
            head = node
            return head
    
        temp = head
        while temp.next:
            temp = temp.next
        
        temp.next = node
        return head
  
  
