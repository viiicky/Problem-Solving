import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        Integer a[] = new Integer[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        
        List<Integer> aList = new ArrayList<Integer>(Arrays.asList(a));
        
        List<Integer> resultList = new ArrayList<Integer>(aList.subList(k, n));
        resultList.addAll(aList.subList(0, k));
        
        System.out.println(resultList.toString().replace(",", "").replace("[", "").replace("]", "").trim());
        
    }
}

