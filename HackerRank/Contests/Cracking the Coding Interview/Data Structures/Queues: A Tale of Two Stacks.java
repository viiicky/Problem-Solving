import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class MyQueue<T>{
		Stack<T> enqueueStack = new Stack<T>();
		Stack<T> dequeueStack = new Stack<T>();
		
		public void enqueue(T x){
			enqueueStack.push(x);
		}
		
		private void arrangeStacks()throws Exception{
			if(dequeueStack.isEmpty()){
				if(enqueueStack.isEmpty()){
					throw new Exception("Queue Underflow: No element is left in the queue.");
				}else{
					while(!enqueueStack.isEmpty()){
						dequeueStack.push(enqueueStack.pop());
					}
				}
			}
		}
		
		public T dequeue(){
			try{
				arrangeStacks();
				return dequeueStack.pop();
			}catch(Exception e){
				return null;
			}
			
		}
		
		public T peek(){
			try{
				arrangeStacks();
				return dequeueStack.peek();
			}catch(Exception e){
				return null;
			}
		}
	}

public class Solution {
    
    public static void main(String[] args) {
        MyQueue<Integer> queue = new MyQueue<Integer>();

        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        for (int i = 0; i < n; i++) {
            int operation = scan.nextInt();
            if (operation == 1) { // enqueue
              queue.enqueue(scan.nextInt());
            } else if (operation == 2) { // dequeue
              queue.dequeue();
            } else if (operation == 3) { // print/peek
              System.out.println(queue.peek());
            }
        }
        scan.close();
    }
}

