import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);
        Integer n = scanner.nextInt();
        
        Integer[] A = new Integer[n];
        
        for(int i=0; i<n; i++){
            A[i] = scanner.nextInt();
        }
        scanner.close();
        
        Integer numberOfSwaps = 0;
        
        for(int i=0; i<A.length-1; i++){
            for(int j=0; j<=A.length-2-i; j++){
                if (A[j] > A[j+1]){
                    Integer temp = A[j];
                    A[j] = A[j+1];
                    A[j+1] = temp;
                    numberOfSwaps += 1;
                }
            }
        }
        
        System.out.println("Array is sorted in "+numberOfSwaps+" swaps.");
        System.out.println("First Element: "+A[0]);
        System.out.println("Last Element: "+A[A.length-1]);
    }
}
