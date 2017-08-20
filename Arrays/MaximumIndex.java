package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * Given an array arr[], find the maximum j – i such that arr[j] >= arr[i]
 *
 * Examples:
 *
 * Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
 * Output: 6  (j = 7, i = 1)
 *
 * Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
 * Output: 8 ( j = 8, i = 0)
 *
 * Input:  {1, 2, 3, 4, 5, 6}
 * Output: 5  (j = 5, i = 0)
 *
 * Input:  {6, 5, 4, 3, 2, 1}
 * Output: -1
 *
 * Problem Link: http://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/
 */
public class MaximumIndex {

	/**
	 * Time Complexity: O(n^2)
	 * Space Complexity: O(1)
	 */
	private static int maximumIndexDifference(int size, int[] array) {
		for (int i = 0; i < size; i++) {
			for (int j = i; j >= 0; j--) {
				if (array[size - 1 - (i - j)] >= array[j]) {
					return size - 1 - i;
				}
			}
		}
		return 0;
	}

	/**
	 * Inspired by method 2 at http://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/
	 * Time Complexity: O(n)
	 * Space Complexity: O(n)
	 */
	private static int maximumIndexDifferenceUsingExtraSpace(int size, int[] array) {
		// prepare i values array
		int[] leftValue = new int[size];
		leftValue[0] = array[0];
		for (int i = 1; i < size; i++) {
			if (array[i] < leftValue[i - 1]) {
				leftValue[i] = array[i];
			}
			else {
				leftValue[i] = leftValue[i - 1];
			}
		}

		// prepare j values array
		int[] rightValue = new int[size];
		rightValue[size - 1] = array[size - 1];
		for (int j = size - 2; j >= 0; j--) {
			if (array[j] > rightValue[j + 1]) {
				rightValue[j] = array[j];
			}
			else {
				rightValue[j] = rightValue[j + 1];
			}
		}

		int i = 0;
		int j = 0;

		int maxDiff = 0;
		while (j < size && i < size) {
			if (rightValue[j] >= leftValue[i]) {
				maxDiff = Math.max(maxDiff, j - i);
				j += 1;
			}
			else {
				i += 1;
			}
		}

		return maxDiff;
	}

	public static void main(String[] args) throws IOException {
		//code
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(reader.readLine().trim());
		for (int i = 0; i < T; i++) {
			int N = Integer.parseInt(reader.readLine().trim());
			int[] A = Arrays.stream(reader.readLine().trim().split("\\s")).mapToInt(Integer::parseInt).toArray();
//			System.out.println(maximumIndexDifference(N, A));
			System.out.println(maximumIndexDifferenceUsingExtraSpace(N, A));
		}
	}
}
