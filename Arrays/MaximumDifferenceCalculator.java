package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * Maximum difference between any two elements of an array such that larger element appears after the smaller number.
 * Given an array arr[] of integers, find out the difference between any two elements
 * such that larger element appears after the smaller number in arr[].
 *
 * Examples:
 * If array is [2, 3, 10, 6, 4, 8, 1] then returned value should be 8 (Diff between 10 and 2).
 * If array is [ 7, 9, 5, 6, 3, 2 ] then returned value should be 2 (Diff between 7 and 9)
 *
 * Problem Link: http://www.geeksforgeeks.org/maximum-difference-between-two-elements/
 *
 * Created by Vikas Prasad on 7/2/2017.
 */
public class MaximumDifferenceCalculator {
    public int maxDifference(int[] array) {
        if (array.length < 2){
            return -1;  // or throw any exception saying atelast two numbers required to find difference
        }

        int maxDiff = array[1] - array[0];
        int min = array[0];

        for (int i = 2; i < array.length; i++) {
            // update the min
            if (array[i-1] < min){
                min = array[i-1];
            }

            // update the max differece
            if (array[i] - min > maxDiff){
                maxDiff = array[i] - min;
            }
        }

        return Math.max(maxDiff, -1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(reader.readLine().trim());

        MaximumDifferenceCalculator mdc = new MaximumDifferenceCalculator();
        for (int i = 0; i < T; i++) {
            reader.readLine();
            int[] C = Arrays.stream(reader.readLine().split("\\s")).mapToInt(Integer::parseInt).toArray();  // read the array
            System.out.println(mdc.maxDifference(C));
        }
    }
}
