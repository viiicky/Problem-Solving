import java.io.*;
import java.util.*;

public class Solution {
    
    public static Integer getFibonacciValue(Integer n){
        if (n==0){
            return 0;
        }else if(n==1){
            return 1;
        }else{
            return getFibonacciValue(n-1) + getFibonacciValue(n-2);
        }
    }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        Integer n = in.nextInt();
        
        System.out.println(Solution.getFibonacciValue(n));
    }
}
