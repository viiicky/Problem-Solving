/*
  Insert Node at the end of a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  class Node {
     int data;
     Node next;
  }
*/
Node Insert(Node head,int data) {
// This is a "method-only" submission. 
// You only need to complete this method.
    
    Node newNode = new Node();
    newNode.data = data;
    newNode.next = null;
    
    if(head == null){
        head = newNode;
    }else{
        Node current = head;
        Node previous = current;
        
        while(current != null){
            previous = current;
            current = current.next;
        }
        previous.next = newNode;
        
    }
    
    return head;
    
}

