import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class HeapsFindTheRunningMedian1 {
	
	private static void addElementToHeap(Integer element, PriorityQueue<Integer> lowerElementsMaxHeap,
			PriorityQueue<Integer> higherElementsMinHeap) {
		// TODO Auto-generated method stub
		
		// add the element to appropriate heap
		if(lowerElementsMaxHeap.isEmpty() || element < lowerElementsMaxHeap.peek()){
			lowerElementsMaxHeap.add(element);
		}else{
			higherElementsMinHeap.add(element);
		}
		
	}
	
	private static void rebalanceHeaps(PriorityQueue<Integer> lowerElementsMaxHeap,
			PriorityQueue<Integer> higherElementsMinHeap) {
		// TODO Auto-generated method stub
		
		// if the size varies by more than one then only do anything		
		if(Math.abs(lowerElementsMaxHeap.size() - higherElementsMinHeap.size()) > 1){
			// move the element from bigger size heap to smaller size heap
			
			if(lowerElementsMaxHeap.size() < higherElementsMinHeap.size()){
				lowerElementsMaxHeap.add(higherElementsMinHeap.poll());
			}else{
				higherElementsMinHeap.add(lowerElementsMaxHeap.poll());
			}
		}
		
	}
	
	private static Double getCurrentMedian(PriorityQueue<Integer> lowerElementsMaxHeap,
			PriorityQueue<Integer> higherElementsMinHeap) {
		// TODO Auto-generated method stub
		
		
		if(lowerElementsMaxHeap.size() == higherElementsMinHeap.size()){
			return (lowerElementsMaxHeap.peek() + higherElementsMinHeap.peek()) / (double) 2;
		}else{			
			if(lowerElementsMaxHeap.size() < higherElementsMinHeap.size()){
				return higherElementsMinHeap.peek()/(double) 1;
			}else{
				return lowerElementsMaxHeap.peek()/(double) 1;
			} 
		}
		
		
	}
	
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        
        Comparator<Integer> maxHeapComparator = new Comparator<Integer>() {	
			@Override
			public int compare(Integer o1, Integer o2) {
				// TODO Auto-generated method stub
				return -1 * o1.compareTo(o2);
			}
		};
		// bucket for lower half
        PriorityQueue<Integer> lowerElementsMaxHeap = new PriorityQueue<Integer>(maxHeapComparator);
        
        // bucket for higher half
        PriorityQueue<Integer> higerElementsMinHeap = new PriorityQueue<Integer>();
        
        for (Integer element : a) {
        	// add the element to either of the bucket
        	addElementToHeap(element, lowerElementsMaxHeap, higerElementsMinHeap);
            
            // rebalnce the buckets if necessary
        	rebalanceHeaps(lowerElementsMaxHeap, higerElementsMinHeap);
            
            // print the current median
        	System.out.println(getCurrentMedian(lowerElementsMaxHeap, higerElementsMinHeap));
			
		}
    }
    
}
