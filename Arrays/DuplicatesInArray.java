package com.company;

/**
 * Find duplicates in O(n) time and O(1) extra space
 *
 * Given an array of n elements which contains elements from 0 to n-1,
 * with any of these numbers appearing any number of times.
 * Find these repeating numbers in O(n) and using only constant memory space.
 *
 * For example, let n be 7 and array be {1, 2, 3, 1, 3, 6, 6}, the answer should be 1, 3 and 6.
 *
 * Problem Link: http://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
 */
public class DuplicatesInArray {
	private static void printDuplicates(int arr[], int n)
	{
		// traverse the array and replace all 0 with n
		// should think of something more elegant to handle 0
		for (int i=0; i<n ;i++){
			arr[i] = arr[i] == 0 ? n : arr[i];
		}

		//add code here.
		java.util.Set<Integer> duplicates = new java.util.LinkedHashSet<>();
		for (int item : arr){
			if(arr[Math.abs(item)%n] < 0){
				duplicates.add(Math.abs(item)%n);
			}else{
				arr[Math.abs(item)%n] = -1 * arr[Math.abs(item)%n];
			}
		}

		if (duplicates.isEmpty()){
			System.out.print("-1");
		}else{
			System.out.print(duplicates.toString().replace("[","").replace(",","").replace("]","").trim());
		}
	}

	public static void main(String[] args) {
		int[] arr = {0, 3, 1, 0, 3};
		DuplicatesInArray.printDuplicates(arr, 5);
	}
}
