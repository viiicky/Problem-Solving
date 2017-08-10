package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * Equilibrium index of an array
 *
 * Equilibrium index of an array is an index such that the sum of elements at lower indexes
 * is equal to the sum of elements at higher indexes.
 *
 * For example, in an arrya A: A[0] = -7, A[1] = 1, A[2] = 5, A[3] = 2, A[4] = -4, A[5] = 3, A[6]=0
 * 3 is an equilibrium index, because: A[0] + A[1] + A[2] = A[4] + A[5] + A[6]
 * 6 is also an equilibrium index, because sum of zero elements is zero, i.e., A[0] + A[1] + A[2] + A[3] + A[4] + A[5]=0
 * 7 is not an equilibrium index, because it is not a valid index of array A.
 *
 * Write a function int equilibrium(int[] arr, int n); that given a sequence arr[] of size n,
 * returns an equilibrium index (if any) or -1 if no equilibrium indexes exist.
 *
 * Problem Link: http://www.geeksforgeeks.org/equilibrium-index-of-an-array/
 */
class EquilibriumPoint {
	/**
	 * Time: O(n)
	 * Space: O(1)
	 */
	private static int equilibrium(int[] arr, int n) {
		int leftSum = 0;
		int rightSum = Arrays.stream(arr, 1, n).sum();

		for (int i = 0; i < n; i++) {
			if (leftSum == rightSum) {
				return i + 1;
			}
			if (i == n - 1) {
				return -1;
			}

			leftSum += arr[i];
			rightSum -= arr[i + 1];
		}

		return -1;
	}

	public static void main(String[] args) throws IOException {
		//code
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(reader.readLine().trim());

		for (int i = 0; i < T; i++) {
			int n = Integer.parseInt(reader.readLine().trim());
			int[] arr = Arrays.stream(reader.readLine().split("\\s")).mapToInt(Integer::parseInt).toArray();
			System.out.println(EquilibriumPoint.equilibrium(arr, n));
		}
	}
}
