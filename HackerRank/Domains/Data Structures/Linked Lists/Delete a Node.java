/*
  Delete Node at a given position in a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  class Node {
     int data;
     Node next;
  }
*/
    // This is a "method-only" submission. 
    // You only need to complete this method. 

Node Delete(Node head, int position) {
  // Complete this method
    
    if(position == 0){
        head = head.next;
    }else{
        Node current = head;
        while (position > 1){
            current = current.next;
            position -= 1;
        }
        current.next = current.next.next;
    }
    
    return head;
}


