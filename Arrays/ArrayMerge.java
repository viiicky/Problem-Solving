package com.company;

import java.util.Arrays;

/**
 * Merge an sorted array of size n into another sorted array of size m+n.
 * There are two sorted arrays. First one is of size m+n containing only m elements.
 * Another one is of size n and contains n elements.
 * Merge these two arrays into the first array of size m+n such that the output is sorted.

 * Problem Link: http://www.geeksforgeeks.org/merge-one-array-of-size-n-into-another-one-of-size-mn/
 *
 * The solution below will run in O(m+n) time.
 * Created by vikas.prasad on 7/7/2017.
 */
public class ArrayMerge {
    public void moveElementsToRight(int[] array) {
        int j = array.length - 1;
        for (int i = array.length - 1; i >= 0; i--) {
            // if current element is blank(-1), do nothing
            // else move it to the end, end maintained by j
            if (array[i] != -1) {
                array[j] = array[i];
                array[i] = -1;  // not necessary, just to visualize array better
                j -= 1;
            }
        }
    }

    // let A be the bigger one
    public void mergeArrays(int[] A, int[] B) {
        int p = B.length;
        int q = 0;

        for (int i = 0; i < A.length; i++) {
            // bounds check
            if (p == A.length) {
                while (q < B.length) {
                    A[i] = B[q];
                    i += 1;
                    q += 1;
                }
                break;
            }

            if (q == B.length) {
                while (p < A.length) {
                    A[i] = A[p];
                    i += 1;
                    q += 1;
                }
            }

            if (A[p] < B[q]) {
                A[i] = A[p];
                p += 1;
            } else {
                A[i] = B[q];
                q += 1;
            }
        }
    }

    public static void main(String[] args) {
        ArrayMerge arrayMerge = new ArrayMerge();
        int[] mPlusN = {2, -1, 7, -1, -1, 10, -1};  // -1 represents blank
        int[] n = {5, 8, 12, 14};

        System.out.println("Initial Arrays:");
        Arrays.stream(mPlusN).forEach(x -> System.out.print(" " + x));
        System.out.println();
        Arrays.stream(n).forEach(x -> System.out.print(" " + x));

        System.out.println();
        arrayMerge.moveElementsToRight(mPlusN);
        System.out.println("After moving elements to right in the bigger array.");
        Arrays.stream(mPlusN).forEach(x -> System.out.print(" " + x));
        System.out.println();
        Arrays.stream(n).forEach(x -> System.out.print(" " + x));

        System.out.println();
        arrayMerge.mergeArrays(mPlusN, n);
        System.out.println("Merged Array");
        Arrays.stream(mPlusN).forEach(x-> System.out.print(" " + x));
        System.out.println();
        Arrays.stream(n).forEach(x -> System.out.print(" " + x));
    }
}
