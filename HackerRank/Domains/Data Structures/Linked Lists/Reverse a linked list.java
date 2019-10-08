/*
  Reverse a linked list and return pointer to the head
  The input list will have at least one element  
  Node is defined as  
  class Node {
     int data;
     Node next;
  }
*/
    // This is a "method-only" submission. 
    // You only need to complete this method. 
Node Reverse(Node head) {
    
    if(head != null){
        
        Node x = head;
        Node y = head.next;
        Node z = head.next;
        
        x.next = null;
        
        while(z != null){
            z = z.next;
            y.next = x;
            x = y;
            y = z;
        }
        
        head = x;
    }
    
    return head;
}

