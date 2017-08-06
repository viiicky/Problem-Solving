package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Find the two repeating elements in a given array.
 *
 * Given an array of n+2 elements. All elements of the array are in range 1 to n.
 * And all elements occur once except two numbers which occur twice. Find the two repeating numbers.
 *
 * For example, array = {4, 2, 4, 5, 2, 3, 1} and n = 5
 * The above array has n + 2 = 7 elements with all elements occurring once except 2 and 4 which occur twice.
 * So the output should be 4 2.

 * Problem Link: http://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/
 */
public class TwoRepeatedElements {

	/**
	 * Time: O(n)
	 * Space: O(n)
	 *
	 * Order of output is guaranteed to be same as the order of input
	 */
	private static void printRepeatedNumbers(int[] array, int size) {
		List<Integer> outputList = new ArrayList<>();
		boolean[] countArray = new boolean[size + 1];
		for (int item : array) {
			if (countArray[item]) {
				outputList.add(item);
				if (outputList.size() == 2) {
					break;
				}
			}
			else {
				countArray[item] = true;
			}
		}

		System.out.print(outputList.get(0) + " " + outputList.get(1));
	}

	/**
	 * Time: O(n)
	 * Space: O(1)
	 *
	 * Order of output is not guaranteed to be same as the order of input
	 */
	private static void printRepeatedNumbersUsingFormulae(int[] array, int size) {
		// sum of first N numbers
		int sum = (size * (size + 1)) / 2;

		// product of first N numbers
		BigInteger prod = TwoRepeatedElements.factorial(BigInteger.valueOf(size));

		// sum of all array elements
		int arraySum = Arrays.stream(array).sum();

		// product of all array elements
		BigInteger arrayProd = Arrays.stream(array).mapToObj(BigInteger::valueOf).reduce(BigInteger.ONE,
				BigInteger::multiply);

		// form the equations
		// if the repeated numbers are x and y then,
		// x + y:
		int S = arraySum - sum;

		// x * y:
		int P = arrayProd.divide(prod).intValue();

		// solving the above two equations:
		// x - y:
		int D = (int) Math.sqrt(S * S - 4*P);

		int x = (S + D)/2;
		int y = (S - D)/2;

		System.out.print(x + " " + y);

	}

	private static BigInteger factorial(BigInteger n) {
		return n.compareTo(BigInteger.ONE) <= 0 ? BigInteger.ONE : n.multiply(factorial(n.subtract(BigInteger.ONE)));
	}

	public static void main(String[] args) throws IOException {
		//code
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(reader.readLine().trim());

		for (int i = 0; i < T; i++) {
			int N = Integer.parseInt(reader.readLine().trim());
			int[] array = Arrays.stream(reader.readLine().split("\\s")).mapToInt(Integer::parseInt).toArray();
//			TwoRepeatedElements.printRepeatedNumbers(array, N);
			TwoRepeatedElements.printRepeatedNumbersUsingFormulae(array, N);
			System.out.println();
		}
	}
}
