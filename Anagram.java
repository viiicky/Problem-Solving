package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

import static java.util.function.Function.identity;
import static java.util.stream.Collectors.counting;
import static java.util.stream.Collectors.groupingBy;

/**
 * Given two strings, check whether two given strings are anagram of each other or not.
 * An anagram of a string is another string that contains same characters, only the order of characters can be different.
 * For example, “act” and “tac” are anagram of each other.
 * <p>
 * Input:
 * The first line of input contains an integer T denoting the number of test cases.
 * Each test case consist of two strings in 'lowercase' only, in a separate line.
 * <p>
 * Output:
 * Print "YES" without quotes if the two strings are anagram else print "NO".
 * <p>
 * Constraints:
 * 1 ≤ T ≤ 30
 * 1 ≤ |s| ≤ 100
 * <p>
 * Example:
 * <p>
 * Input:
 * 2
 * geeksforgeeks
 * forgeeksgeeks
 * allergy
 * allergic
 * <p>
 * Output:
 * YES
 * NO
 * <p>
 * Problem Link: http://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/
 */
class Anagram {
    public static void main(String[] args) throws IOException {
        //code
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(reader.readLine().trim());
        for (int i = 0; i < T; i++) {
            String stringA = reader.readLine().trim();
            String stringB = reader.readLine().trim();

//            System.out.println(Anagram.checkAnagram(stringA, stringB) ? "YES" : "NO");
            System.out.println(Anagram.checkAnagramInOneLoop(stringA, stringB) ? "YES" : "NO");
        }
    }

    /**
     * Time Complexity: O(1) if the two strings differ in length, O(n) otherwise
     * Space Complexity: O(n)
     * <p>
     * where n is the length of string
     */
    private static boolean checkAnagram(String strA, String strB) {
        if (strA.length() != strB.length()) {
            return false;
        }

        // create a map(set if the input strings are constrained to have all unique characters) of characters-count for strA
        // use codePoints() instead of chars() if string can have unicode characters
        Map<Integer, Long> charCount = strA.chars().boxed().collect(groupingBy(identity(), counting()));

        // traverse strB and assert the char count matches
        for (int i = 0; i < strB.length(); i++) {
            int c = strB.charAt(i);

            if (!charCount.containsKey(c)) {
                return false;
            }

            if (charCount.get(c) == 1) {
                charCount.remove(c);
                continue;
            }

            charCount.put(c, charCount.get(c) - 1);
        }

        return charCount.isEmpty();
    }

    /**
     * Time Complexity: O(1) if the two strings differ in length, O(n) otherwise
     * Space Complexity: O(n)
     * <p>
     * where n is the length of string
     *
     * Inspired by optimization suggested at http://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/
     */
    private static boolean checkAnagramInOneLoop(String strA, String strB) {
        if (strA.length() != strB.length()) {
            return false;
        }

        // create a map(set if the input strings are constrained to have all unique characters) of characters-count for strA
        Map<Integer, Integer> charCount = new HashMap<>();

        for (int i = 0; i < strA.length(); i++) {
            int a = strA.charAt(i);
            charCount.merge(a, 1, (x, y) -> x + y);

            int b = strB.charAt(i);
            charCount.merge(b, -1, (x, y) -> x + y);

            charCount.remove(a, 0);
            charCount.remove(b, 0);
        }

        return charCount.isEmpty();
    }
}
