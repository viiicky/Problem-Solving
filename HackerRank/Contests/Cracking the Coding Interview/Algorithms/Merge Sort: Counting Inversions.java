import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
	static long inversionCount;

	static void mergeSort(int[] arr, int[] temp, int left, int right){
		if(left<right){
			Integer mid = (left+right) / 2;
			mergeSort(arr, temp, left, mid);
			mergeSort(arr, temp, mid+1, right);
			merge(arr, temp, left, mid, right);
		}
	}

	static void merge(int[] arr, int[] temp, int left, int mid, int right){
		int leftIndex = left;
		int rightIndex = mid + 1;
		int tempIndex = left;
		
		while(leftIndex <= mid && rightIndex <= right){
			if(arr[leftIndex] <= arr[rightIndex]){
				temp[tempIndex] = arr[leftIndex];
				leftIndex += 1;
			}else{
				// only this block gets executed in case of inversions
				temp[tempIndex] = arr[rightIndex];
				rightIndex += 1;
				inversionCount += mid - leftIndex + 1;
			}
			tempIndex += 1;
		}
		
		while(leftIndex <= mid){
			temp[tempIndex] = arr[leftIndex];
			leftIndex += 1;
			tempIndex += 1;
		}
		
		while(rightIndex <= right){
			temp[tempIndex] = arr[rightIndex];
			rightIndex += 1;
			tempIndex += 1;
		}
		// temp completely prepared till here
		
		// copy from temp to original now
		for(int i=left; i<=right; i++){
			arr[i] = temp[i];
		}
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int t = in.nextInt();
		for(int a0 = 0; a0 < t; a0++){
			int n = in.nextInt();
			int arr[] = new int[n];
			for(int arr_i=0; arr_i < n; arr_i++){
				arr[arr_i] = in.nextInt();
			}

			inversionCount = 0;
			mergeSort(arr, new int[n], 0, n-1);
			System.out.println(inversionCount);
		}
	}
}
